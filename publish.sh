#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Create the HTML
python3 md2html.py

# Create the PDF
python3 md2pdf.py

# Run the Docker command with specified platform
docker run --platform linux/amd64 -it -v $PWD:$PWD -w $PWD skytapcmscripttools.azurecr.io/course_manual_manager
