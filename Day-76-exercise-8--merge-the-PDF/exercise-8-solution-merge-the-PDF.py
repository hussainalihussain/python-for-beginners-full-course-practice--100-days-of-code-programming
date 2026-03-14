import os
from pypdf import PdfWriter

pdfs = os.listdir('pdf')

merger = PdfWriter()
fileName = "pdf/merged-pdf.pdf"

for pdf in pdfs:
    print(f"Appending pdf/{pdf} to {fileName}")
    merger.append(f"pdf/{pdf}")

merger.write(fileName)