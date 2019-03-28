#!/usr/bin/python3
import socket
import threading
from _thread import *
print_lock = threading.Lock()
 
ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind((socket.gethostname(), 10000))
ssFT.listen(5)

while True:
    (conn, address) = ssFT.accept()
    #pdf_file = 'my.txt'#'myld.pdf'    
 
    #Receive file name
    #data received from client
    name = conn.recv(1024) 
    #print("Hurray message")
    if not name: 
        #print('Bye')
        break
    print(name)
    
            
    #SendFile
#n=name+".pdf"
    with open(name, 'rb') as fs:
        conn.send(b'BEGIN')
        while True:
            data = fs.read(1024)
            #print('Sending data')
            conn.send(data)
            #print('Sent data')
            if not data:
                #print('Breaking from sending data')
                break
        conn.send(b'ENDED')
        fs.close()

    continue
    
    #break
conn.close()
