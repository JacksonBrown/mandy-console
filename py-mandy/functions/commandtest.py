#!/usr/bin/python

# IMPORTS
from mandyfunctions import *
import os


# VARIABLES
log_path = "../logs/log.txt"

def commandTest(x):
	while x != 'exit':

		## IF HELP
		if x == 'help':
			showHelp()
			from prompt import *
			promptTwo()

		## ELIF RAM
		elif x == 'ram':
			showFree()
			from prompt import *
			promptTwo()

		## ELIF REMOVEUSER
		elif x == 'removeuser':
			deleteUser()
			from prompt import *
			promptTwo()

		## ELIF GUI
		elif x == 'gui':
			from gui import *
			createGui()
			from prompt import *
			promptTwo()

		## ELIF CLEAR
		if x == 'clear':
			os.system("clear")

		## ELIF MANDYHISTORY
		elif x == 'mandyhistory':
			log_var = open(log_path)
			print log_var.read()

		## ELSE
		else:
			print "You're a " + x + "."
			from prompt import *
			promptTwo()
		break
		print " "
		





