#!/usr/bin/python3
from tkinter import *
import socket
import os

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pdf_file = 'my.pdf'
txt_file = 'listreceived.txt'

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        return 
    
    def init_window(self):
        self.master.title("United Conspects") 
        self.pack(fill=BOTH, expand=1)
        #Show Introducing Text
        self.ShowText()
        #Conect to Server
        self.Conect()       
        #Exit Button
        quitButton = Button(self, text="Exit",command=self.ClientExit)
        quitButton.place(x=250, y=100)
        #Input Message and Send It
        self.entry = Entry(self)
        self.button = Button(self, text="Get File", command=self.GetFile)
        self.button.place(x=200, y=50)
        self.entry.place(x=50, y=50) 
        #Get list of files
        listButton = Button(self, text="Get list", command=self.GetList)
        listButton.place(x=0, y=100)
       
    def Text(self):
        S = Scrollbar(self)
        T = Text(self, height=10)
        T.place(x=0, y=140)
        S.pack(side=RIGHT, fill=Y)
        #S.place(in_=txtOutput, relx=1.0, relheight=1.0, bordermode="outside")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        with open('listreceived.txt', 'r') as f:
            T.insert(INSERT, f.read())
            
    def ShowText(self):
        text = Label(self, text="Welcome to our program! Please, write the file name.")
        text.pack()
        return

    def ClientExit(self):
        if os.path.exists('listreceived.txt'):
            os.remove('listreceived.txt')
        csFT.send(bytes(2))
        exit()
        return
        
    def Conect(self):
        csFT.connect(('127.0.0.1', 10005))
        return
    
    def GetFile(self):
        message=self.entry.get()
        csFT.send(message.encode('ascii'))
        self.ReceiveFile()
        return
        
    def GetList(self):
        csFT.send(bytes(1))
        self.ReceiveList()
        self.Text()
        
    def ReceiveList(self):
        with open(txt_file, "wb") as fw:
            while True:
                data = csFT.recv(1024)
                if data == b'BEGIN':
                    continue
                elif data == b'ENDED':
                    break
                else:
                    fw.write(data)
            fw.close()
            #print("Received..")
            return 
        
    def ReceiveFile(self):        
        with open(pdf_file, "wb") as fw:
            while True:
                data = csFT.recv(1024)
                if data == bytes(1):
                    break
                elif data == b'BEGIN':
                    continue
                elif data == b'ENDED':
                    break
                else:
                    fw.write(data)
            fw.close()
            #print("Received..")
            if os.path.getsize(pdf_file) == 0:
                os.remove(pdf_file)
            return
            
        
root = Tk()
root.geometry("300x300")
app = Window(root)
root.mainloop()
