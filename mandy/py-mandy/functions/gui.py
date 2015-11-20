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
	root.minsize(600, 840)
	root.maxsize(600, 840)
	#root.configure(background='white')
	root["bg"] = "white"

	# VARAIABLES
	img = ImageTk.PhotoImage(Image.open("images.duckduckgo.com.jpeg"))
	input_header_var = "Input: "
	output_header_var = "Output: "
	header_img = ImageTk.PhotoImage(Image.open("header.png"))

	# CREATEGUI FUNCTIONS


	## CALLBACK TEST FUNCTION
	def helloCallBack():
		#tkMessageBox.showinfo("Command Output", os.system("ls"))
		import mandyfunctions
		command_output = StringVar()
		command_output.set("command output here")
		outputWidget.insert(INSERT, "%s" % (command_output))

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
		command = helloCallBack, 
		width = 10, 
		relief=RAISED
 		)

	## OUTPUT LABEL
	outputWidget = Text( 
		root, 
		height = "20", 
		relief=RAISED
		)
	#output = make_label(root, 0, 0, 500, 600, textvariable=command_output, foreground="black")

	## INPUT TEXT
	inputWidget = Text(
		root, 
		height="20",
		relief=RAISED
		)

	## HEADER LABEL
	header = Label(
		root, 
		image = header_img,
		bg = "white",
		borderwidth = 0,
		highlightthickness = 0, 
		relief=RAISED
		)

	## INPUT HEADER LABEL
	inputHeader = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		text = input_header_var, 
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)

	## INPUT HEADER LABEL
	outputHeader = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		text = output_header_var, 
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)

	## SPACER LABELS
	spacer_one = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)

	spacer_two = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)

	spacer_three = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)

	spacer_four = Label(
		root, 
		bg = "white", 
		font = ('helv36'),
		borderwidth = 0,
		highlightthickness = 0, 
		height = 1, 
		relief=RAISED
		)


	# SET WIDGET GEO.
	header.pack()
	inputHeader.pack()
	spacer_one.pack()
	inputWidget.pack()
	spacer_four.pack()
	outputHeader.pack()
	spacer_two.pack()
	outputWidget.pack()
	spacer_three.pack()
	submit.pack()

	root.mainloop()

createGui()

