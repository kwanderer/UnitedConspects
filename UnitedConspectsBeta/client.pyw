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
        quitButton.place(x=260, y=120)
        #Input Message and Send It
        self.entry = Entry(self)
        self.button = Button(self, text="Get File", command=self.GetFile)
        self.button.place(x=230, y=80)
        self.entry.place(x=50, y=80) 
        #Get list of files
        listButton = Button(self, text="Get list", command=self.GetList)
        listButton.place(x=0, y=120)
       
    def Text(self):
        T = Text(self, height=9)
        T.place(x=0, y=150)
        with open('listreceived.txt', 'r') as f:
            T.insert(INSERT, f.read())
        S = Scrollbar(self)
        S.pack(side=RIGHT, fill=Y)
        #S.place(in_=txtOutput, relx=1.0, relheight=1.0, bordermode="outside")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
            
    def ShowText(self):
        text = Label(self, text="Welcome to our program!")
        text.pack()
        text = Label(self, text="Please, write the full file name(with .pdf).")
        text.pack()
        text = Label(self, text="Downoaded file you will find in the folder where is client file.")
        text.pack()
        text = Label(self, text=" ")
        text.pack()
        text = Label(self, text=" ")
        text.pack()
        text = Label(self, text=" ")
        text.pack()
        text = Label(self, text=" ")
        text.pack()
        return

    def ClientExit(self):
        if os.path.exists('listreceived.txt'):
            os.remove('listreceived.txt')
        csFT.send(bytes(2))
        exit()
        return
        
    def Conect(self):
        csFT.connect(('127.0.0.1', 10003))
        return
    
    def GetFile(self):
        message=self.entry.get()
        #print(message)
        csFT.send(message.encode('ascii'))
        #print('Sended file name')
        #self.ReceiveFile()
        self.RFile()
        #print('File received')
        #pdf_file=message
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
                    #print(data)
                return data    
            fw.close()
            #print("Received..")
            return
    def RFile(self):
        with open(pdf_file, "wb") as fw:
            #print('Open file')
            while True:
                data = csFT.recv(1024)
                fw.write(data)
                #print('Save data')
                if data == bytes(1):
                    break
            fw.close()
            #print('File close')
            #print("Received..")
            if os.path.getsize(pdf_file) == 0 or os.path.getsize(pdf_file) == 1:
                os.remove(pdf_file)
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
                    #print(data)
                #return data
                #continue   
            fw.close()
            #print("Received..")
            if os.path.getsize(pdf_file) == 0:
                os.remove(pdf_file)
            return
            
        
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
