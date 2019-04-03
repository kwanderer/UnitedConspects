#!/usr/bin/python3
import socket
import threading
import os
from _thread import *
print_lock = threading.Lock()
 
ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind(('127.0.0.1', 10003))
ssFT.listen(5)

def SendFile():
    if os.path.exists(name):
        with open(name, 'rb') as fs:
            #conn.send(b'BEGIN')
            while True:
                data = fs.read(1024)
                conn.send(data)
                #print(data)
                if not data:
                    break
            conn.send(bytes(1))
            fs.close()
            return
    else:
        conn.send(bytes(1))
        #break


def SendList():
    with open('list.txt', 'rb') as fs:
        conn.send(b'BEGIN')
        while True:
            data = fs.read(1024)
            conn.send(data)
            #print(data)
            if not data:
                break
        conn.send(b'ENDED')
        fs.close()
    return
       

while True:
    (conn, address) = ssFT.accept()
    print_lock.acquire()
    #Receive file name
    #data received from client
    while True:
        name = conn.recv(1024)
        #print("Hurray message")
        #print(name)
        if name == bytes(1):
            SendList()
        elif name == bytes(2): 
            break
        else:
            SendFile()
            
        #SendFile
        continue
    print_lock.release()


conn.close()
