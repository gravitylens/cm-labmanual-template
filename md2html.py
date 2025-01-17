import markdown

# Read the Markdown file
with open("LabGuide.md", "r") as f:
    markdown_content = f.read()

# Replace ::: pagebreak ::: with <hr data-page-break="">
markdown_content = markdown_content.replace("::: pagebreak :::", "<hr data-page-break=\"\">")

# Convert Markdown to HTML
html_content = markdown.markdown(markdown_content)

# Write the HTML to a file
with open("LabGuide.html", "w") as f:
    f.write(html_content)