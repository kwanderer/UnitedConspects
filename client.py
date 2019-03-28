#!/usr/bin/python3
from tkinter import *
import socket
#import PyPDF2

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pdf_file = 'my.pdf'

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        #self.recaiveFile()
        return 
    
    def init_window(self):
        self.master.title("United Conspects") 
        self.pack(fill=BOTH, expand=1)

        #Show Introducing Text
        self.showText()
        #Conect to Server
        self.conect()
        #pdf_file = 'My.pdf'        
        
        #Exit Button
        quitButton = Button(self, text="Exit",command=self.client_exit)
        quitButton.place(x=0, y=100)
        
        #Input Message and Send It
        self.entry = Entry(self)
        self.button = Button(self, text="Get", command=self.on_button)
        self.button.place(x=50, y=100)
        self.entry.place(x=100, y=50)          
            
    def showText(self):
        text = Label(self, text="Welcome to our program! Please, write the file name.")
        text.pack()
        return

    def client_exit(self):
        exit()
        return
        
    def conect(self):
        csFT.connect((socket.gethostname(), 10000))
        return
    
    def on_button(self):
        message=self.entry.get()
        csFT.send(message.encode('ascii'))
        self.recaiveFile()
        return
        #print(a)
        
    #Receive, output and save file    
    def recaiveFile(self):        
        with open(pdf_file, "wb") as fw:
            #print("Receiving..")
            while True:
                #print('receiving')
                data = csFT.recv(1024)
                if data == b'BEGIN':
                    continue
                elif data == b'ENDED':
                    #print('Breaking from file write')
                    break
                else:
                    fw.write(data)
                    #print('Wrote to file')
        fw.close()
        print("Received..")
        return
            
        
root = Tk()
root.geometry("400x300")
app = Window(root)
        #return app
root.mainloop() 
