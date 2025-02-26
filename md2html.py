import markdown
import re
import os
import sys

def include_files(content, base_path, depth=0, max_depth=5):
    if depth > max_depth:
        print("Maximum include depth reached.")
        exit()

    include_pattern = re.compile(r'::: include (.+?) :::')
    while True:
        match = include_pattern.search(content)
        if not match:
            break
        filename = os.path.join(base_path, match.group(1))
        try:
            with open(filename, 'r') as f:
                included_content = f.read()
            included_content = include_files(included_content, base_path, depth + 1, max_depth)
            content = content[:match.start()] + included_content + content[match.end():]
        except FileNotFoundError:
            print(f"Warning: {filename} not found.")
            content = content[:match.start()] + content[match.end():]
    return content

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python md2html.py <path_to_markdown_file> [--debug]")
    exit()

markdown_file_path = sys.argv[1]
base_path = os.path.dirname(markdown_file_path)
debug = len(sys.argv) == 3 and sys.argv[2] == "--debug"

if debug:
    print(f"Debugging enabled. Processing file: {markdown_file_path}")

# Read the Markdown file
with open(markdown_file_path, "r") as f:
    markdown_content = f.read()

# Replace ::: include filename.md ::: with the content of the referenced file
markdown_content = include_files(markdown_content, base_path)

# Remove comment lines
markdown_content = re.sub(r'\[\\\\]: #.*', '', markdown_content)

# Replace ::: pagebreak ::: with <hr data-page-break=\"\">
markdown_content = markdown_content.replace("::: pagebreak :::", "<hr data-page-break=\"\">")

# Replace warn> lines with <x-block class="alert alert-danger">
markdown_content = re.sub(r'^warn>(.*)$', r'<x-block class="alert alert-danger">\1</x-block>', markdown_content, flags=re.MULTILINE)

# Replace info> lines with <x-block class="alert alert-warning">
markdown_content = re.sub(r'^info>(.*)$', r'<x-block class="alert alert-warning">\1</x-block>', markdown_content, flags=re.MULTILINE)

# Convert Markdown to HTML with table support, code highlighting, and fenced code blocks
html_content = markdown.markdown(markdown_content, extensions=['tables', 'codehilite', 'fenced_code'])

# Replace ^^text^^ with <x-copy-text> tags
html_content = re.sub(r'\^\^([^\^]+)\^\^', r'<x-copy-text>\1</x-copy-text>', html_content)

# Write the HTML to a file in the current directory
output_file_path = os.path.join(os.getcwd(), os.path.basename(os.path.splitext(markdown_file_path)[0]) + ".html")
with open(output_file_path, "w") as f:
    f.write(html_content)

if debug:
    print(f"HTML content written to: {output_file_path}")