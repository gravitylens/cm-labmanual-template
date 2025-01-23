# Skytap Course Manager Lab Manual Template

This repository provides a template for creating lab manuals for Skytap Course Manager in markdown format.

## Purpose
The purpose of this repository is to help you create structured and well-formatted lab manuals using markdown. The provided cheatsheet will guide you through the process of authoring markdown files.

## Description of Files and Folders

- **LabGuide.md**: The main markdown file for the lab manual. This file contains the content of the lab manual, including instructions, steps, and placeholders for dynamic content.  You may create other md files to include within the main file, but the conversion scripts expect to start rendering the lab manual in this file.
- **Cheatsheet.md**: A markdown file that provides a reference for markdown syntax and conventions used in the lab manual.
- **readme.md**: This file. It provides an overview of the project, instructions for usage, and a description of the files and folders.
- **md2html.py**: A Python script that converts the markdown file (`LabGuide.md`) to an HTML file (`LabGuide.html`). It also processes includes and page breaks.
- **md2pdf.py**: A Python script that converts the HTML file (`LabGuide.html`) to a PDF file. It also processes placeholders and applies CSS for styling.  It will prompt for a PDF filename on first run and store that filename in (`.pdf_config.yml`) for future runs.
- **styles.css**: A CSS file that defines the styles for the PDF output. It includes styles for fonts, tables, images, and other elements.
- **skytapvariables.csv**: A CSV file that contains placeholders and their corresponding values. These values are used to replace placeholders in the markdown and HTML files.
- **images/**: A folder to store images used in the lab manual. The images can be referenced in the markdown file using relative paths.
- **publish.sh**: A shell script to upload the lab manual to a Skytap Course Manager title. It processes the markdown file, converts it to HTML and PDF, and uploads the files to Skytap.
- **course_manual_manager/**: This folder is provided by Skytap and contnains the code to upload an HTML manual, and any attachments it references, to a particular Skytap Course Manager Title.  It will prompt you for details on first run and store those details in (`.publish.yml`) for future runs.

## Instructions
1. Refer to the [Cheatsheet](./Cheatsheet.md) for instructions on how to author a markdown file.
2. Edit the LabGuide.md to create your lab manual.  You may include images and the contents of other files to build a structured lab manual.
3. Create a local python virtual environment and install the (`requirements.txt`).
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
4. Once you have created your lab manual, run the following script to upload it to a Skytap Course Manager title:
    ```sh
    ./publish.sh
    ```
    This will publish your lab manual to the specified Skytap Course Manager title.

## Useful Tools
To simplify pasting images into markdown files, consider installing the Markdown Sync Image extension in VSCode. This extension allows you to easily paste images directly into your markdown files, and it will handle the image file management for you. You can configure Markdown Sync Image to automatically generate, or prompt you for an image file name when pasting. You can also configure it to automatically put pasted images into the ./images folder for a better organized project.
