#!/usr/bin/python

# IMPORTS
import subprocess
import os
from clint.textui import colored
from commandtest import *

# TEXT VARIABLES
com_inp = ": Command input "
com_out = ": Error/Alert output "
com_inf = ": Information from devs "
com_act = ": Actions being commited or information needed "

# CREATE PROMPT FUNCTION

def prompt():
	subprocess.call(["clear"])
	subprocess.call(["cat", "logo-blue"])
	print
	print "Created by Jackson Brown "
	print "type \"help\" for a list of options. \n"
	print "COLOR CODING: "
	print colored.green("Green") + com_inp 
	print colored.red("Red") + com_out 
	print colored.cyan("Cyan") + com_inf 
	print colored.yellow("Yellow") + com_act
	print

# END MAIN PROMPT F()

def promptTwo():
	com_opt = 0
	com_opt = raw_input(colored.green(">"))
	commandTest(com_opt)
