#!/usr/bin/python3           
# This is client.py file
import socket
import PyPDF2 

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csFT.connect((socket.gethostname(), 10001))

# creating a pdf file object. We opened the example.pdf in binary mode. and saved the file object as pdfFileObj.
#pdfFileObj = open('MLD1.pdf', 'rb') 

#Send file
with open('MLD1.pdf', 'rb') as fs:
    #Using with, no file close is necessary,
    #with automatically handles file close
    csFT.send(b'BEGIN')
    while True:
        data = fs.read(1024)
        print('Sending data')
        csFT.send(data)
        print('Sent data')
        if not data:
            print('Breaking from sending data')
            break
    csFT.send(b'ENDED')
    fs.close()

    #Receive file
#print("Receiving..")
 #   while True:
  #      data = csFT.recv(1024)
   #     if not data:
    #        break
     #   print(data)
#print("Received..")

csFT.close()
    
# creating a pdf reader object 
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
#print(pdfReader.numPages) 

# creating a page object 
#pageObj = pdfReader.getPage(0) 

# extracting text from page 
#print(pageObj.extractText()) 

# closing the pdf file object 
#pdfFileObj.close() 
