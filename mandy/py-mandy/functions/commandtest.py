#!/usr/bin/python

# IMPORTS
from prompt import *
from showhelp import *
from showfree import *

def commandTest(x):
	while x != 'exit':
		if x == 'help':
			showHelp()
			break
		elif x == 'ram':
			showFree()
			break


