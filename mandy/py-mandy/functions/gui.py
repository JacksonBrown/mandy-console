#!/usr/bin/python

# IMPORTS
import Tkinter
import tkMessageBox

# GUI SETS
top = Tkinter.Tk()
top.title("Mandy")
top.minsize(600, 500)

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()
