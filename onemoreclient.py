#!/usr/bin/env python3

# client.py  
import socket
import ftplib
import urllib

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


# get local machine name
# local host IP '127.0.0.1' 
##host = socket.gethostname()
host = "127.0.0.1"
# Define the port on which you want to connect 
port = 9999


# connection to hostname on the port.
s.connect((host, port)) 

while True:
    
# message you send to server 
    message = input("Enter message or 'quit' -> ")


    while message != 'quit':
    # message sent to server 
        s.send(message.encode('ascii'))
        print("message send")

    # Receive no more than 1024 bytes
        data = s.recv(1024)
        print("message receive")
    
    # print the received message 
        print("The time got from the server is %s" % data.decode('ascii'))
    
        break
    
# ask the client whether he wants to continue 
    ans = input('\nDo you want to continue(y/n) :') 
    if ans == 'y': 
        continue
    else: 
        break
    
    
# close the connection when loop will end
s.close()