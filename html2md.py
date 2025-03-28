import html2text

def convert_html_to_markdown(html_file, markdown_file):
    """Converts an HTML file to a Markdown file."""
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    markdown_content = html2text.html2text(html_content)
    
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Conversion completed: {markdown_file}")

# Example usage
html_file = "input.html"  # Change this to your HTML file
markdown_file = "output.md"
convert_html_to_markdown(html_file, markdown_file)