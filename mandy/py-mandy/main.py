#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys

# SET SYSTEM PATH TO ADD FUNCTIONS DIR
sys.path.insert(0, 'functions/')

## IMPORT HELP FUNCTION
from showhelp import *


# CLASSES

class mandyApp():

	def helpCall(self):
		showHelp();

	#def __init__(self):
	#	os.system("ls");

App = mandyApp()


App.helpCall()

