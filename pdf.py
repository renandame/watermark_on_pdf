import PyPDF2
import os
os.makedirs('./pdfs', exist_ok=True)
for file in os.listdir("."):
    if file.endswith(".pdf"):
        template = PyPDF2.PdfFileReader(open(file, 'rb'))
        watermark = PyPDF2.PdfFileReader(open("watermark.pdf", 'rb'))
        output = PyPDF2.PdfFileWriter()

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
        
        file = open('./pdfs/'+file, 'wb')
        output.write(file)
        print(file.name, " feito.")
