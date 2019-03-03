#!/usr/bin/python3           
# This is client.py file

import socket
 
csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csFT.connect((socket.gethostname(), 8756))
 
text_file = 'send.txt'
 
#Send file
with open(text_file, 'rb') as fs:
    #Using with, no file close is necessary,
    #with automatically handles file close
    csFT.send(b'BEGIN')
    while True:
        data = fs.read(1024)
        print('Sending data', data.decode('utf-8'))
        csFT.send(data)
        print('Sent data', data.decode('utf-8'))
        if not data:
            print('Breaking from sending data')
            break
    csFT.send(b'ENDED')
    fs.close()
 
    #Receive file
print("Receiving..")
with open(text_file, 'wb') as fw:
    while True:
        data = csFT.recv(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
print("Received..")
 
csFT.close()