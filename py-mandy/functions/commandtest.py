#!/usr/bin/python

# IMPORTS
from mandyfunctions import *
import os
import sys


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

		## ELIF MANDYHISTORY
		elif x == 'mandyhistory':
			log_var = open(log_path)
			print log_var.read()

		## ELIF DIRDELETE
		elif x == 'deldir':
			directoryDelete()
			from prompt import *
			promptTwo()

		## ELIF DIRSCAN
		elif x == 'dirscan':
			directoryScan()
			from prompt import *
			promptTwo()

		## ELIF CLEAR
		elif x == 'clear':
			clearFunc()
			from prompt import *
			promptTwo()

		## ELSE
		else:
			print "You're a " + x


		break
