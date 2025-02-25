from PyPDF2 import PdfWriter
import os
merger = PdfWriter()
files=[file for file in os.listdir() if file.endswitch(".pdf")]
# ["file1.pdf", "file2.pdf"]
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
