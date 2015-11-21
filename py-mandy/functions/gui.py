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

	def closeWindow(self):
		root.destroy()

	## CREATE GUI FUNCTION
	def createGui(self):
		# VARAIABLES
		img = ImageTk.PhotoImage(Image.open("images/images.duckduckgo.com.jpeg"))
		input_header_var = "Input: "
		output_header_var = "Output: "
		header_img = ImageTk.PhotoImage(Image.open("images/header.png"))


		## SUBMIT BUTTON
		self.submit            = Button(self)
		self.submit["text"]    = "Run"
		self.submit["command"] = self.helloCallBack
		self.submit["width"]   = 10
		self.submit["relief"]  = RAISED

		self.submit.pack({"side": "left"})

		## QUIT BUTTON
		self.QUIT            = Button(self)
		self.QUIT["text"]    = "QUIT"
		self.QUIT["fg"]      = "red"
		self.QUIT["command"] = self.closeWindow()
		self.QUIT["width"]   = 10
		self.QUIT["relief"]  = RAISED

		self.QUIT.pack({"side": "left"})

		## OUTPUT LABEL
		self.outputWidget           = Text(self)
		self.outputWidget["height"] = 20
		self.outputWidget["relief"] = RAISED

		self.outputWidget.pack({"side": "left"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createGui()

root = Tk()
mandyGui = Application(master=root)
mandyGui.mainloop()
root.destroy()

