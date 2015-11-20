#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys
sys.path.insert(0, 'functions/')

## FILE IMPORTS
from prompt import *

os.system("echo > logs/log.txt")
os.system("echo > logs/show_directory_output.txt")
os.system("echo > logs/log_mesg.txt")
os.system("echo > logs/show_process.txt")

# CLASSES

## MANDYINIT CLASS
class mandyInit():

	## CREATE PROMPTCALL F()
	def promptCall(self):
		prompt()

	## CREATE PROMPTTWOCALL F()
	def promptTwoCall(self):
		promptTwo()


App = mandyInit()
App.promptCall()
App.promptTwoCall()
