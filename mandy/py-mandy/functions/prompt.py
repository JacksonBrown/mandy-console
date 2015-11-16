#!/usr/bin/python

# IMPORTS
import subprocess
from clint.textui import colored

# TEXT VARIABLES
com_inp = ": Command input "
com_out = ": Output of command being run "
com_inf = ": Information from devs "
com_act = ": Actions being commited or information needed "
com_opt = 0

# CREATE PROMPT FUNCTION

def prompt():
	subprocess.call(["clear"])
	subprocess.call(["cat", "logo"])
	print "Welcome to the Mandy Console. "
	print "type \"help\" for a list of options. \n"
	print colored.cyan("Current version 0.5.1 \n")
	print "COLOR CODING: "
	print colored.green("Green") + com_inp 
	print colored.red("Red") + com_out 
	print colored.cyan("Cyan") + com_inf 
	print colored.yellow("Yellow") + com_act

# END MAIN PROMPT F()

def promptTwo():
	com_opt = raw_input(colored.green(">"))
	return com_opt
	print
