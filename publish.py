#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

import yaml
from dotenv import load_dotenv

import md2html

DOCKER_IMAGE = "course_manual_manager:local"
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))


def build_image():
    command = [
        "docker", "build", "--platform", "linux/amd64",
        "-t", DOCKER_IMAGE, os.path.join(TOOL_DIR, "course_manual_manager"),
    ]
    result = subprocess.run(command)
    if result.returncode != 0:
        sys.exit("Failed to build course_manual_manager Docker image")


def load_manifest(content_dir):
    manifest_path = os.path.join(content_dir, "manifest.yml")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    if "targets" not in manifest:
        sys.exit("manifest.yml is missing required key: targets")

    for target in manifest["targets"]:
        for key in ("name", "source", "course_id"):
            if key not in target:
                sys.exit(f"manifest.yml target is missing required key: {key}")

        for translation in target.get("translations", []):
            for key in ("language", "course_id"):
                if key not in translation:
                    sys.exit(f"manifest.yml translation is missing required key: {key}")

    return manifest


def publish_target(content_dir, html_path, target, app_hostname, api_key, api_secret, draft):
    abs_content_dir = os.path.abspath(content_dir)
    abs_html_path = os.path.abspath(html_path)

    command = [
        "docker", "run", "--platform", "linux/amd64", "-i",
        "-v", f"{abs_content_dir}:{abs_content_dir}",
        "-w", abs_content_dir,
        DOCKER_IMAGE,
        "--html-file", abs_html_path,
        "--app-hostname", app_hostname,
        "--course-id", str(target["course_id"]),
        "--api-key", api_key,
        "--api-secret", api_secret,
    ]

    if draft:
        command.append("--upload")
    else:
        command += ["--delete", "--upload", "--publish"]

    result = subprocess.run(command)
    return result.returncode == 0


def convert_and_publish(content_dir, source_path, course, app_hostname, api_key, api_secret, draft):
    fd, output_path = tempfile.mkstemp(suffix=".html", dir=content_dir)
    os.close(fd)

    try:
        print(f"Converting {source_path} -> {output_path}")
        md2html.convert(source_path, output_path)
        return publish_target(content_dir, output_path, course, app_hostname, api_key, api_secret, draft)
    finally:
        os.remove(output_path)


def main():
    parser = argparse.ArgumentParser(description="Convert a content folder's lab guide to HTML and publish it to its manifest-defined Skytap Course Manager targets.")
    parser.add_argument("--content-dir", required=True, help="Path to the content folder containing manifest.yml")
    parser.add_argument("--target", action="append", help="Name of a target to publish (repeatable). Defaults to all targets in the manifest.")
    parser.add_argument("--draft", action="store_true", help="Upload without publishing, for previewing the draft")
    args = parser.parse_args()

    if shutil.which("docker") is None:
        sys.exit("docker is required to publish to Skytap Course Manager")

    build_image()

    load_dotenv()
    api_key = os.environ.get("SKYTAP_API_KEY")
    api_secret = os.environ.get("SKYTAP_API_SECRET")
    app_hostname = os.environ.get("SKYTAP_APP_HOSTNAME")
    if not api_key or not api_secret or not app_hostname:
        sys.exit("SKYTAP_API_KEY, SKYTAP_API_SECRET and SKYTAP_APP_HOSTNAME must be set (see .env.example)")

    manifest = load_manifest(args.content_dir)

    targets = manifest["targets"]
    if args.target:
        selected_names = set(args.target)
        targets = [t for t in targets if t["name"] in selected_names]
        missing = selected_names - {t["name"] for t in targets}
        if missing:
            sys.exit(f"Unknown target(s): {', '.join(sorted(missing))}")

    results = {}
    for target in targets:
        print(f"\nPublishing to target '{target['name']}' ({app_hostname}, course {target['course_id']})...")
        source_path = os.path.join(args.content_dir, target["source"])
        results[target["name"]] = convert_and_publish(args.content_dir, source_path, target, app_hostname, api_key, api_secret, args.draft)

        if args.draft or not target.get("translations"):
            continue

        import translate

        for translation in target["translations"]:
            language = translation["language"]
            result_key = f"{target['name']} ({language})"
            print(f"\nTranslating '{target['name']}' to '{language}'...")

            translated_source_path = translate.translate_target_language(args.content_dir, target, translation)

            print(f"\nPublishing to target '{result_key}' ({app_hostname}, course {translation['course_id']})...")
            results[result_key] = convert_and_publish(args.content_dir, translated_source_path, translation, app_hostname, api_key, api_secret, draft=False)

    print("\nPublish summary:")
    all_succeeded = True
    for name, succeeded in results.items():
        status = "OK" if succeeded else "FAILED"
        print(f"  {name}: {status}")
        all_succeeded = all_succeeded and succeeded

    sys.exit(0 if all_succeeded else 1)


if __name__ == "__main__":
    main()
