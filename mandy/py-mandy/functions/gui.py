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

	# VARAIABLES
	command_output = StringVar()
	img = ImageTk.PhotoImage(Image.open("images.duckduckgo.com.jpeg"))

	# CREATEGUI FUNCTIONS


	## CALLBACK TEST FUNCTION
	def helloCallBack():
		#tkMessageBox.showinfo("Command Output", os.system("ls"))
		import mandyfunctions
		command_output.set("command output here")
		output.pack()


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

	# SET WIDGET GEO.
	submit.pack()

	root.mainloop()
