## PDFMerger
Merge pdfs together that need a specific first page with multiple additional pages.

## Usage
- You only need to download the main.py file and have Python downloaded. An IDE is not needed but would be helpful. 
- Run the main.py file once which will install dependencies and create directories and data.txt
> **IF THEY DON'T EXIST THEY ARE AUTOMATICALLY CREATED**
> 
> You need a txt editor like Notepad to edit the data.txt file. Add the names into the data.txt file, with each name on a new line.
- Drag and drop the pdfs you want to merge into the directories (folders).
> The pdfs you want for the first page of the merged pdfs go in the "Fpage_pdfs" directory.
> 
> All additional pages for any of the merged pdfs go in the "pdfpages" directory.
- Run program again to sort and merge the pdfs into new pdfs inside the Output folder
> You can just open the main.py file to run it, using IDLE from Python or other IDE's is an option.

## Depndencies
- Python
> https://www.python.org/downloads/
- PyPdf2
> This should be installed on first run if not already installed

# Python libraries part of Python
- os
- shutil
- subprocess
- sys
