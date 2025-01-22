import os
import yaml
import csv
from weasyprint import HTML, CSS
import re

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

# Load CSS from external file
css_file = 'styles.css'
css = CSS(filename=css_file)

# Read the HTML file
html_file = 'LabGuide.html'
with open(html_file, 'r') as f:
    html_content = f.read()

# Load Skytap variables from skytapvariables.csv
variables = {}
with open('skytapvariables.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        variables[rows[0]] = rows[1]

# Replace %{parametername} placeholders with corresponding values
for key, value in variables.items():
    html_content = html_content.replace(f"{key}", value)

# Replace ^^text^^ with <x-copy-text> tags for PDF generation
pdf_content = re.sub(r'\^\^([^\^]+)\^\^', r'<x-copy-text>\1</x-copy-text>', html_content)

# Write the modified content to a temporary file for PDF generation
temp_html_file = 'LabGuide_for_pdf.html'
with open(temp_html_file, 'w') as f:
    f.write(pdf_content)

# Convert HTML to PDF with CSS
HTML(temp_html_file).write_pdf(pdf_file, stylesheets=[css])
print(f"PDF file '{pdf_file}' has been created successfully.")

# Clean up the temporary file
os.remove(temp_html_file)
