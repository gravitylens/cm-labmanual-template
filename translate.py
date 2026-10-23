import os
import re
import shutil
import sys

import yaml

import md2html

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_GLOSSARY_PATH = os.path.join(TOOL_DIR, "translation-glossary.default.yml")

SOURCE_LANG = "eng_Latn"

# ISO 639-1 (manifest `language`) -> NLLB FLORES-200 code. Add more pairs as needed.
LANGUAGE_CODES = {
    "de": "deu_Latn",
    "fr": "fra_Latn",
    "es": "spa_Latn",
    "it": "ita_Latn",
    "pt": "por_Latn",
    "nl": "nld_Latn",
    "pl": "pol_Latn",
    "ru": "rus_Cyrl",
    "sv": "swe_Latn",
    "da": "dan_Latn",
    "no": "nob_Latn",
    "fi": "fin_Latn",
    "cs": "ces_Latn",
    "tr": "tur_Latn",
    "ar": "arb_Arab",
    "hi": "hin_Deva",
    "vi": "vie_Latn",
    "id": "ind_Latn",
    "th": "tha_Thai",
    "ja": "jpn_Jpan",
    "ko": "kor_Hang",
    "zh": "zho_Hans",
    "zh-tw": "zho_Hant",
    "he": "heb_Hebr",
}

# Sentinel marker used to protect spans of text from translation. Plain ASCII (rather than
# special unicode brackets) survives the translation model's tokenizer far more reliably.
SENTINEL_OPEN = "zzzprotectz"
SENTINEL_CLOSE = "zendprotectz"
SENTINEL_RE = re.compile(SENTINEL_OPEN + r'\s*(\d+)\s*' + SENTINEL_CLOSE, re.IGNORECASE)

FENCE_RE = re.compile(r'```.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`\n]+`')
NOTRANSLATE_BLOCK_RE = re.compile(r'::: notranslate :::.*?::: /notranslate :::', re.DOTALL)
DIRECTIVE_RE = re.compile(r':::.*?:::')
BLOCK_MARKUP_PREFIX_RE = re.compile(r'^(warn>|info>)', re.MULTILINE)
COPY_TEXT_RE = re.compile(r'\^\^[^\^]+\^\^')
PLACEHOLDER_RE = re.compile(r'%\{[^}]+\}')
HTML_TAG_RE = re.compile(r'<[^>]+>')
IMAGE_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)')
LINK_SUFFIX_RE = re.compile(r'\]\([^)]+\)')
LINK_PREFIX_RE = re.compile(r'\[(?=[^\[\]]*\]\()')

HEADING_RE = re.compile(r'^(#{1,6}\s+)(.*)$')
LIST_RE = re.compile(r'^(\s*(?:[-*+]|\d+\.)\s+)(.*)$')

_PIPELINE_CACHE = {}


def nllb_code(language):
    code = LANGUAGE_CODES.get(language.lower())
    if not code:
        sys.exit(
            f"Unsupported translation language '{language}'. "
            "Add a FLORES-200 mapping for it to LANGUAGE_CODES in translate.py."
        )
    return code


def load_glossary(content_dir):
    terms = []
    for path in (DEFAULT_GLOSSARY_PATH, os.path.join(content_dir, "translation-glossary.yml")):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                terms.extend(yaml.safe_load(f) or [])

    # longest terms first so multi-word phrases match before their substrings
    return sorted(set(terms), key=len, reverse=True)


def _mask(pattern, text, protected):
    def repl(m):
        token = f"{SENTINEL_OPEN}{len(protected)}{SENTINEL_CLOSE}"
        protected.append(m.group(0))
        return token

    return pattern.sub(repl, text)


def _unmask(text, protected):
    def restore(m):
        index = int(m.group(1))
        if index >= len(protected):
            return m.group(0)
        return protected[index]

    # a later mask (e.g. an HTML tag) can wrap an earlier one (e.g. a placeholder inside it),
    # so keep substituting until no sentinels remain (or nothing changes, to avoid looping forever)
    for _ in range(len(protected) + 1):
        if not SENTINEL_RE.search(text):
            break
        new_text = SENTINEL_RE.sub(restore, text)
        if new_text == text:
            break
        text = new_text
    return text


def _mask_protected_spans(content, glossary):
    protected = []
    masked = content
    masked = _mask(FENCE_RE, masked, protected)
    masked = _mask(INLINE_CODE_RE, masked, protected)
    masked = _mask(NOTRANSLATE_BLOCK_RE, masked, protected)
    masked = _mask(DIRECTIVE_RE, masked, protected)
    masked = _mask(BLOCK_MARKUP_PREFIX_RE, masked, protected)
    masked = _mask(COPY_TEXT_RE, masked, protected)
    masked = _mask(PLACEHOLDER_RE, masked, protected)
    masked = _mask(HTML_TAG_RE, masked, protected)
    # images are never translated (alt text included); protect them whole, before generic links
    masked = _mask(IMAGE_RE, masked, protected)
    # protect the markdown link syntax `[` and `](url)` so translation can't corrupt it,
    # while still allowing the visible link text in between to be translated
    masked = _mask(LINK_PREFIX_RE, masked, protected)
    masked = _mask(LINK_SUFFIX_RE, masked, protected)

    if glossary:
        glossary_re = re.compile(r'\b(' + '|'.join(re.escape(term) for term in glossary) + r')\b')
        masked = _mask(glossary_re, masked, protected)

    return masked, protected


def _get_pipeline():
    model_name = os.environ.get("TRANSLATION_MODEL", "facebook/nllb-200-distilled-600M")
    if model_name not in _PIPELINE_CACHE:
        from transformers import pipeline

        print(f"Loading translation model '{model_name}' (first run may take a while)...")
        _PIPELINE_CACHE[model_name] = pipeline("translation", model=model_name, device=-1)
    return _PIPELINE_CACHE[model_name]


def _translate_string(text, target_code):
    translator = _get_pipeline()
    result = translator(text, src_lang=SOURCE_LANG, tgt_lang=target_code, max_length=1024)
    return result[0]["translation_text"]


def _is_blank_after_unmask(text):
    return not SENTINEL_RE.sub('', text).strip()


def _has_translatable_text(text):
    return bool(re.search(r'[A-Za-z]', SENTINEL_RE.sub('', text)))


def _translate_line(line, target_code):
    if not line.strip() or _is_blank_after_unmask(line) or not _has_translatable_text(line):
        return line

    prefix, text = "", line
    for pattern in (HEADING_RE, LIST_RE):
        m = pattern.match(line)
        if m:
            prefix, text = m.group(1), m.group(2)
            break

    if not text.strip() or _is_blank_after_unmask(text) or not _has_translatable_text(text):
        return prefix + text

    # table rows (including the header) are left untouched; cell-by-cell translation was
    # unreliable and author-maintained tables are often meant to stay structurally exact
    if text.count("|") >= 2:
        return prefix + text

    return prefix + _translate_string(text, target_code)


def translate_text(content, target_code, glossary):
    masked, protected = _mask_protected_spans(content, glossary)
    translated_lines = [_translate_line(line, target_code) for line in masked.split("\n")]
    return _unmask("\n".join(translated_lines), protected)


def _collect_source_files(path, seen=None):
    if seen is None:
        seen = []

    abs_path = os.path.abspath(path)
    if abs_path in seen:
        return seen
    seen.append(abs_path)

    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()

    base_dir = os.path.dirname(abs_path)
    for included in md2html.find_included_files(content):
        _collect_source_files(os.path.join(base_dir, included), seen)

    return seen


def _copy_images(content_dir, translations_dir):
    images_src = os.path.join(content_dir, "images")
    if not os.path.isdir(images_src):
        return

    images_dst = os.path.join(translations_dir, "images")
    os.makedirs(images_dst, exist_ok=True)
    for name in os.listdir(images_src):
        src_file = os.path.join(images_src, name)
        dst_file = os.path.join(images_dst, name)
        if os.path.isfile(src_file) and not os.path.exists(dst_file):
            shutil.copy2(src_file, dst_file)


def slugify(name):
    return re.sub(r'[^A-Za-z0-9._-]+', '-', name).strip('-') or "target"


def translate_target_language(content_dir, target, translation):
    language = translation["language"]
    target_code = nllb_code(language)
    glossary = load_glossary(content_dir)

    translations_dir = os.path.join(content_dir, slugify(target["name"]), "translations", language)
    os.makedirs(translations_dir, exist_ok=True)

    source_path = os.path.abspath(os.path.join(content_dir, target["source"]))
    translated_source_path = None

    for file_path in _collect_source_files(source_path):
        out_path = os.path.join(translations_dir, os.path.basename(file_path))
        print(f"  Translating {os.path.relpath(file_path, content_dir)} -> {os.path.relpath(out_path, content_dir)} [{language}]")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        translated = translate_text(content, target_code, glossary)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(translated)

        if file_path == source_path:
            translated_source_path = out_path

    _copy_images(content_dir, translations_dir)

    return translated_source_path
