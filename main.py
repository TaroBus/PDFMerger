# Run once to check dependencies and create directories and data.txt
# Fill directories, first pages in first page directory and all other pages in the second
# Run program once again to sort and merge new pdfs into the Output folder

import os
import shutil
import subprocess
import sys

try:
    # Try to import PyPDF2
    import PyPDF2
except ImportError:
    print("PyPDF2 is not installed. Attempting to install...")

    # Attempt to install PyPDF2
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
        print("PyPDF2 has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install PyPDF2. Please install it manually.")

# Only PyPDF2 needs to be installed
from PyPDF2 import PdfMerger, PdfReader


def merge_pdfs(name, output_name):
    merger = PdfMerger()

    # Process first page
    for first_file_name in os.listdir(first):
        if first_file_name == name:
            first_page_path = os.path.join(first, first_file_name)
            with open(first_page_path, 'rb') as f:
                merger.append(PdfReader(f))
        else:
            print(f"First page not found for {name}")
            return

    # Add other pages
    other_pages_files = [f for f in os.listdir(pages) if name in f]
    if other_pages_files:
        for other_page_file in other_pages_files:
            other_page_path = os.path.join(pages, other_page_file)
            with open(other_page_path, 'rb') as f:
                merger.append(PdfReader(f))
    else:
        print(f"Other pages not found for {name}")
        return

    # Write the merged PDF
    output_path = os.path.join(output, output_name)
    merger.write(output_path)
    merger.close()

    print(f"Merged PDF saved as {output_path}")


# Directory names
first = "Fpage_pdfs"
pages = "pdfpages"
output = "output_pdfs"
# if the folders don't exist make them
os.makedirs(first, exist_ok=True)
os.makedirs(pages, exist_ok=True)
os.makedirs(output, exist_ok=True)
os.path.exists('data.txt') or open('data.txt', 'w').close()

# Remove and recreate the output directory
if os.path.exists(output):
    shutil.rmtree(output)
os.makedirs(output)

# Read names from data.txt
with open("data.txt", "r") as file:
    names = [line.rstrip() for line in file]
print("Names to process:", names)

# Process each name
for name in names:
    merge_pdfs(name, f"2023-2024 Interact Volunteer Hours {name}.pdf")
