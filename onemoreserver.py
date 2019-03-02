#!/usr/bin/env python3

# server.py 
import socket                                         
import time
import ftplib
import urllib

# import thread module 
from _thread import *
import threading 
print_lock = threading.Lock() 

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# local host IP '127.0.0.1' 
##host = socket.gethostname()
host = "127.0.0.1"

port = 9999     

print("Socket created")

# bind to the port
s.bind((host, port))                                  

print("Socket binded to post", port) 

# queue up to 5 requests
s.listen(5)

print("Socket is listening")



while True:
    # establish a connection with client
    client,addr = s.accept()   
    
   
    
    # lock acquired by client 
    print_lock.acquire()
    
    print("Got a connection from %s" % str(addr))
    
    while True:
    
    # data received from client 
        data = client.recv(1024) 
        print("Hurray message")
        if not data: 
            print('Bye')
            break
        print(data)
    
    
    # lock released on exit 
    #   print_lock.release() 
    
    
    # send back reversed string to client 
    #client.send(data) 
        currentTime = time.ctime(time.time()) + "\r\n"
        client.send(currentTime.encode('ascii'))
        continue
        
   
        
# connection closed, but when loop will end 
client.close() 