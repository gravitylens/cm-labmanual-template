import argparse
import os
import markdown
import re


def include_files(content, base_dir, depth=0, max_depth=5):
    if depth > max_depth:
        print("Maximum include depth reached.")
        exit()

    include_pattern = re.compile(r'::: include (.+?) :::')
    while True:
        match = include_pattern.search(content)
        if not match:
            break
        # includes are resolved relative to the file that references them
        filename = os.path.join(base_dir, match.group(1))
        try:
            with open(filename, 'r', encoding='utf-8') as f:  # Ensure UTF-8 encoding
                included_content = f.read()
            included_content = include_files(included_content, os.path.dirname(filename), depth + 1, max_depth)
            content = content[:match.start()] + included_content + content[match.end():]
        except FileNotFoundError:
            print(f"Warning: {filename} not found.")
            content = content[:match.start()] + content[match.end():]
    return content


def convert(source_path, output_path):
    with open(source_path, "r", encoding='utf-8') as f:  # Ensure UTF-8 encoding
        markdown_content = f.read()

    # Replace ::: include filename.md ::: with the content of the referenced file
    markdown_content = include_files(markdown_content, os.path.dirname(source_path))

    # Remove comment lines
    markdown_content = re.sub(r'\[\\\\]: #.*', '', markdown_content)

    # Replace ::: pagebreak ::: with <hr data-page-break="">
    markdown_content = markdown_content.replace("::: pagebreak :::", "<hr data-page-break=\"\">")

    # Replace warn> lines with <x-block class="alert alert-danger">
    markdown_content = re.sub(r'^warn>(.*)$', r'<x-block class="alert alert-danger">\1</x-block>', markdown_content, flags=re.MULTILINE)

    # Replace info> lines with <x-block class="alert alert-warning">
    markdown_content = re.sub(r'^info>(.*)$', r'<x-block class="alert alert-warning">\1</x-block>', markdown_content, flags=re.MULTILINE)

    # Convert Markdown to HTML with table support, code highlighting, and fenced code blocks
    html_content = markdown.markdown(markdown_content, extensions=['tables', 'codehilite', 'fenced_code'])

    # Replace ^^text^^ with <x-copy-text> tags
    html_content = re.sub(r'\^\^([^\^]+)\^\^', r'<x-copy-text>\1</x-copy-text>', html_content)

    with open(output_path, "w", encoding='utf-8') as f:  # Ensure UTF-8 encoding
        f.write(html_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a lab guide markdown file to HTML.")
    parser.add_argument("--source", default="LabGuide.md", help="Path to the source markdown file")
    parser.add_argument("--output", default="LabGuide.html", help="Path to write the generated HTML file")
    args = parser.parse_args()

    convert(args.source, args.output)