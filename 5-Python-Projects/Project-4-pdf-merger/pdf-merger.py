from pypdf import PdfWriter

merger = PdfWriter()

merger.append("sample1.pdf")
merger.append("sample2.pdf")

merger.write("sample-1-and-2.pdf")