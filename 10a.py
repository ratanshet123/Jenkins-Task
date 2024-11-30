from PyPDF2 import PdfWriter,PdfReader
num=int(input("Enter the number of page to combine:"))
pdf1=open("Internship Report(Ratan).pdf",'rb')
pdf2=open("Final Report.pdf",'rb')
pdf_writer=PdfWriter()
pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num-1]
pdf_writer.add_page(page)
pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num-1]
pdf_writer.add_page(page)
with open("output.pdf",'wb')as output:
    pdf_writer.write(output)
