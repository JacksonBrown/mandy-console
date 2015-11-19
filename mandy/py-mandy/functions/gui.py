#!/usr/bin/python

# IMPORTS
from Tkinter import *
import tkMessageBox
import os
from mandyfunctions import *
import Image 
import ImageTk


# FUNCTIIONS

def createGui():
	
	# GUI SETS
	root = Tk()
	root.title("Mandy")
	root.minsize(600, 500)
	root.maxsize(600, 500)
	#root.configure(background='white')
	root["bg"] = "white"

	# VARAIABLES
	command_output = StringVar()
	img = ImageTk.PhotoImage(Image.open("images.duckduckgo.com.jpeg"))
	header_var = "Mandy Console"

	# CREATEGUI FUNCTIONS


	## CALLBACK TEST FUNCTION
	def helloCallBack():
		#tkMessageBox.showinfo("Command Output", os.system("ls"))
		import mandyfunctions
		command_output.set("command output here")
		output.pack()

	## MAKE LABEL FUNCTION
	def make_label(master, x, y, h, w, *args, **kwargs):
		f = Frame(master, height=h, width=w)
		f.pack_propagate(0)
		f.place(x=x, y=y)
		label = Label(f, *args, **kwargs)
		#label.pack(fill=BOTH, expand=1)
		label.pack()
		return label

	# SET WIDGET ATT.


	## SUBMIT BUTTON
	submit = Button(
		root, 
		text ="Run", 
		command = helloCallBack
 		)

	## OUTPUT LABEL
	output = Label( 
		root, 
		textvariable=command_output, 
		image = img, 
		relief=RAISED 
		)
	#output = make_label(root, 0, 0, 500, 600, textvariable=command_output, foreground="black")

	## HEADER LABEL
	header = Label(
		root, 
		text = header_var, 
		bg = "white", 
		font = ('helv36')
		)


	# SET WIDGET GEO.
	header.place(x=20, y=20)
	header.pack()
	submit.pack()

	root.mainloop()

createGui()

