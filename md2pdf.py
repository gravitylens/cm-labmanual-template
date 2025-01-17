import os
import yaml
from weasyprint import HTML, CSS

# Load configuration from .publish.yml
pdf_config_file = '.pdf_config.yml'
pdf_file = None

if os.path.exists(pdf_config_file):
    with open(pdf_config_file, 'r') as file:
        config = yaml.safe_load(file)
        pdf_file = config.get('pdf_file')

# Prompt user for PDF file name if not found in config
if not pdf_file:
    pdf_file = input("Enter the name for the PDF file (e.g., LabGuide.pdf): ")
    # Save the PDF file name to .pdf_config.yml
    with open(pdf_config_file, 'w') as file:
        config = {'pdf_file': pdf_file}
        yaml.safe_dump(config, file)

# Define CSS to scale images
css = CSS(string='''
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
''')

# Convert HTML to PDF with CSS
html_file = 'LabGuide.html'
HTML(html_file).write_pdf(pdf_file, stylesheets=[css])
print(f"PDF file '{pdf_file}' has been created successfully.")
