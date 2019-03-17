#!/usr/bin/python3

from tkinter import *
import socket

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    
    def init_window(self):
        self.master.title("United Conspects") 
        self.pack(fill=BOTH, expand=1)

        
        self.showText()
       
        quitButton = Button(self, text="Start",command=self.conect)
        quitButton.place(x=50, y=100)
        
        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)
        quitButton.place(x=0, y=100)
        
        
        
#input message
    def showText(self):
        text = Label(self, text="Welcome!")
        text.grid()    

    def client_exit(self):
        exit()        
        
    def conect(self):
        csFT.connect((socket.gethostname(), 10002))
        
        #input message
        Label(self, text="Course Name").grid(row=0)
        #self.entry = Entry(self)
        #self.entry.grid(row=0, column=1)
        
        v = StringVar()
        e = Entry(self, textvariable=v)
        e.grid()

        v.set("a default value")
        s = v.get()
        
        print(s)
        Button(self, text='Send', command=self.se).grid(row=3, column=1, sticky=W, pady=4)
        #send message
        #s.send(message.encode('ascii'))

       
 #send        
    def se(self):
        message="hello!"
        csFT.send(message.encode('ascii'))

        
root = Tk()

root.geometry("400x300")

app = Window(root)
root.mainloop() 