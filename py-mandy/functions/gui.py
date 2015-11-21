#!/usr/bin/python

# IMPORTS
from Tkinter import *
import tkMessageBox
import os
from mandyfunctions import *
import Image 
import ImageTk


class Application(Frame):

	# FUNCTIIONS

	## CALLBACK TEST FUNCTION
	def helloCallBack(self):
		#tkMessageBox.showinfo("Command Output", os.system("ls"))
		import mandyfunctions
		command_output = StringVar()
		command_output.set("command output here")
		outputWidget.insert(INSERT, "%s" % (command_output))


	## CREATE GUI FUNCTION
	def createGui(self):

		# VARAIABLES

		## COSBY PATH VARIABLE SET
		self.cosby_path = "images/images.duckduckgo.com.jpeg"
		self.img = ImageTk.PhotoImage(Image.open(self.cosby_path))


		## INPUT LABEL VARIABLES
		self.input_header_var = "Input: "
		self.output_header_var = "Output: "


		## IMAGE PATH VARIABLE SET
		self.image_path = "images/header.png"
		self.header_img = ImageTk.PhotoImage(Image.open(self.image_path))


		## SUBMIT BUTTON
		self.submit            = Button(self)
		self.submit["text"]    = "Run"
		self.submit["command"] = self.helloCallBack
		self.submit["width"]   = 10
		self.submit["relief"]  = RAISED


		## QUIT BUTTON
		self.QUIT            = Button(self)
		self.QUIT["text"]    = "QUIT"
		self.QUIT["fg"]      = "red"
		self.QUIT["command"] = self.quit
		self.QUIT["width"]   = 10
		self.QUIT["relief"]  = RAISED


		## INPUT LABEL
		self.inputWidget           = Text(self)
		self.inputWidget["height"] = 20
		self.inputWidget["relief"] = RAISED
		self.inputWidget["bg"]     = "white"


		## OUTPUT LABEL
		self.outputWidget           = Text(self)
		self.outputWidget["height"] = 20
		self.outputWidget["relief"] = RAISED
		self.outputWidget["bg"]     = "white"


		## HEADER LABEL
		self.headerLabel 	   	       = Label(self)
		self.headerLabel["relief"] 	       = RAISED
		self.headerLabel["image"] 	       = self.header_img
		self.headerLabel["borderwidth"]        = 0
		self.headerLabel["highlightthickness"] = 0


		## INPUT HEADER LABEL
		self.inputHeaderLabel 			    = Label(self)
		self.inputHeaderLabel["relief"]		    = RAISED
		self.inputHeaderLabel["text"]               = self.input_header_var
		self.inputHeaderLabel["borderwidth"]        = 0
		self.inputHeaderLabel["highlightthickness"] = 0

		## OUTPUT HEADER LABEL
		self.outputHeaderLabel 			     = Label(self)
		self.outputHeaderLabel["relief"]	     = RAISED
		self.outputHeaderLabel["text"]               = self.output_header_var
		self.outputHeaderLabel["borderwidth"]        = 0
		self.outputHeaderLabel["highlightthickness"] = 0


		# PACKING ORDER

		## SET HEADER LABEL
		self.headerLabel.pack()


		## PACK INPUT
		self.inputHeaderLabel.pack()
		self.inputWidget.pack()


		## PACK OUTPUT
		self.outputHeaderLabel.pack()
		self.outputWidget.pack()


		## PACK QUIT BUTTON
		self.QUIT.pack(pady=20)


		## PACK RUN BUTTON
		self.submit.pack()

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.master.minsize(600, 850)
		self.master.maxsize(600, 850)
		self.master.title("Mandy")
		self.createGui()


root = Tk()
mandyGui = Application(master=root)
mandyGui.mainloop()
root.destroy()

