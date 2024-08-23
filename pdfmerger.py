from PyPDF2 import PdfWriter, PdfReader
import os
merger = PdfWriter()
files = [file for file in os.listdir("C:/Users/LENOVO/Desktop/python/pdfs") if file.endswith(".pdf")]
for pdf in files:
    with open(os.path.join("C:/Users/LENOVO/Desktop/python/pdfs", pdf), 'rb') as file:
        reader = PdfReader(file)
        merger.append(reader)

merger.write("merged-pdf.pdf")
merger.close() 