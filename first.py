from PyPDF2 import PdfFileReader

pdf_document = "Fkko2019.pdf"
with open(pdf_document, "rb") as filehandle:
   pdf = PdfFileReader(filehandle)
   info = pdf.getDocumentInfo()
   pages = pdf.getNumPages()
   print (info)
   print ("number of pages: %i" % pages)
   page1 = pdf.getPage(0)
   print(page1)
   print(page1.extractText())
