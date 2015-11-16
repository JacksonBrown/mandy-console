#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys

# SET SYSTEM PATH TO ADD FUNCTIONS DIR
sys.path.insert(0, 'functions/')

## IMPORT HELP FUNCTION
from showhelp import *
## IMPORT PROMPT FUNCTION
from prompt import *
## IMPORT COMMANDTEST FUNCTION
from commandtest import *

# CLASSES

class mandyApp():

	## CREATE HELPCALL F()
	def helpCall(self):
		showHelp()


	## CREATE PROMPTCALL F()
	def promptCall(self):
		prompt()

	## CREATE PROMPTTWOCALL F()
	def promptTwoCall(self):
		promptTwo()

	def promptVarCall(self):
		import prompt
		print prompt.com_opt


App = mandyApp()
App.promptCall()
App.promptTwoCall()
App.promptVarCall()
