#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys

# SET SYSTEM PATH TO ADD FUNCTIONS DIR
sys.path.insert(0, 'functions/')

## IMPORT HELP FUNCTION
from showhelp import *
from prompt import *

# CLASSES

class mandyApp():

	## CREATE HELPCALL F()
	def helpCall(self):
		showHelp();


	## CREATE PROMPTCALL F()
	def promptCall(self):
		prompt();

	## CREATE PROMPTTWOCALL F()
	def promptTwoCall(self):
		promptTwo();

	#def __init__(self):
	#	os.system("ls");

App = mandyApp()


App.promptCall()


while com_opt != exit:
	App.promptTwoCall();
	break
