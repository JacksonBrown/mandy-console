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

	blue_logo_path = "logo-blue"
	if os.path.exists(blue_logo_path):
		blue_logo_open = open(blue_logo_path)
	else:
		print "logo-blue not found."

	print blue_logo_open.read()

	print
	print "Created by Jackson Brown "
	print "type \"help\" for a list of options. \n"
	print "COLOR CODING: "
	print colored.green("Green") + com_inp 
	print colored.red("Red") + com_out 
	print colored.cyan("Cyan") + com_inf 
	print colored.yellow("Yellow") + com_act
	print

def redPrompt():
	subprocess.call(["clear"])

	red_logo_path = "logo-red"
	if os.path.exists(red_logo_path):
		red_logo_open = open(red_logo_path)
	else:
		print "logo-red not found."

	print red_logo_open.read()

	#subprocess.call(["cat", "logo-red"])
	print
	print "Created by Jackson Brown "
	print "type \"help\" for a list of the red-version options. \n"
	print "COLOR CODING: "
	print colored.green("Green") + com_inp 
	print colored.red("Red") + com_out 
	print colored.cyan("Cyan") + com_inf 
	print colored.yellow("Yellow") + com_act
	print

# END MAIN PROMPT F()

def promptTwo():
	com_opt = 0

	prompt_conf_path =  "prompt"
	if os.path.exists(prompt_conf_path):
		prompt_conf_var = open(prompt_conf_path)
		com_opt = raw_input(prompt_conf_var.read())
		commandTest(com_opt)
	else:
		print "prompt conf not found"
