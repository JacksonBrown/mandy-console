#!/usr/bin/python

# IMPORTS
from prompt import *
from mandyfunctions import *

def commandTest(x):
	while x != 'exit':
		if x == 'help':
			showHelp()
			break
		elif x == 'ram':
			showFree()
			break


