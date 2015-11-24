#!/usr/bin/python

# IMPORTS
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import os
from mandyfunctions import *
import Image 
import ImageTk

E = tk.E
W = tk.W
N = tk.N
S = tk.S


def main():
	root = Tk()
	mandyGui = Application(master=root)
	mandyGui.mainloop()
	root.destroy()


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
		self.input_header_path = "images/input.png"
		self.input_header_var = ImageTk.PhotoImage(Image.open(self.input_header_path))

		self.output_header_path = "images/output.png"
		self.output_header_var = ImageTk.PhotoImage(Image.open(self.output_header_path))


		## IMAGE PATH VARIABLE SET
		self.image_path = "images/header.png"
		self.header_img = ImageTk.PhotoImage(Image.open(self.image_path))


		## CREATE INPUT VARIABLE
		self.input_var = StringVar()


		## MENU CREATE
		self.menu 	     = Menu(self)
		self.menu["tearoff"] = 0

		self.menu.add_command(label="file", command=None)



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
		self.inputWidget["height"] = 10
		self.inputWidget["width"]  = 80
		self.inputWidget["relief"] = RAISED
		self.inputWidget["bg"]     = "white"


		## OUTPUT LABEL
		self.outputWidget           = Text(self)
		self.outputWidget["height"] = 10
		self.outputWidget["width"]  = 80
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
		self.inputHeaderLabel["image"]               = self.input_header_var
		self.inputHeaderLabel["borderwidth"]        = 0
		self.inputHeaderLabel["highlightthickness"] = 0

		## OUTPUT HEADER LABEL
		self.outputHeaderLabel 			     = Label(self)
		self.outputHeaderLabel["relief"]	     = RAISED
		self.outputHeaderLabel["image"]              = self.output_header_var
		self.outputHeaderLabel["borderwidth"]        = 0
		self.outputHeaderLabel["highlightthickness"] = 0


		# PACKING ORDER

		## MENU 
		#self.menu.pack()

		## SET HEADER LABEL
		self.headerLabel.grid(row=0, sticky=W)


		## PACK INPUT
		self.inputHeaderLabel.grid(row=1, column=0, sticky=W)
		self.inputWidget.grid(row=2, column=0, sticky=W)


		## PACK OUTPUT
		self.outputHeaderLabel.grid(row=3, column=0, sticky=W)
		self.outputWidget.grid(row=4, column=0, sticky=W)


		## PACK QUIT BUTTON
		self.QUIT.grid(sticky=E, pady=20, row=5)


		## PACK RUN BUTTON
		self.submit.grid(sticky=W, pady=20, row=5)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		#self.master.minsize(600, 850)
		#self.master.maxsize(600, 850)
		self.master.title("Mandy")


		#w = self.master.winfo_screenwidth()
		#h = self.master.winfo_screenheight()

		#self.master.overrideredirect(1)
		#self.master.geometry("%dx%d+0+0" % (w, h))


		self.createGui()


if __name__ == "__main__":
	main()



