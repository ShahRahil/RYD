# importing required modules 
import PyPDF2 
import re

# creating a pdf file object 
pdfFileObj = open('The_Living_World.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object # extracting text from page 
page=0
print("THE TEXT CONTENT IN THE GIVEN PDF IS AS BELOW: ")

while page<17:
    page+=1
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())
    for line in pageObj:
        line=line.rstrip()
        #fiNDING QUESTIONS
        if re.search('^[0-9].+',line):
            print(line)


 

# closing the pdf file object 
pdfFileObj.close() 
