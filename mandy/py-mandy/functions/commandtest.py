#!/usr/bin/python

# IMPORTS
from mandyfunctions import *


def commandTest(x):
	while x != 'exit':
		if x == 'help':
			showHelp()
			from prompt import *
			promptTwo()
		elif x == 'ram':
			showFree()
			from prompt import *
			promptTwo()
		elif x == 'removeuser':
			deleteUser()
			from prompt import *
			promptTwo()
		else:
			print "Command entry not found."
			from prompt import *
			promptTwo()
		break
		print





