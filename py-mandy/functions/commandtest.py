#!/usr/bin/python

# IMPORTS
from mandyfunctions import *
import os
import sys


# VARIABLES
log_path = "logs/log.txt"

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
			from prompt import *
			promptTwo()

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

		## ELIF EDITSERVICE
		elif x == 'editservice':
			editService()
			from prompt import *
			promptTwo()

		## ELIF EDITSSH
		elif x == 'editssh':
			editSshd()
			from prompt import *
			promptTwo()

		## ELIF EDITLIGHTDM
		elif x == 'editlightdm':
			editLightdm()
			from prompt import *
			promptTwo()

		## ELIF EDITSUDO
		elif x == 'editsudo':
			editSudo()
			from prompt import *
			promptTwo()

		## ELIF LOGSEE
		elif x == 'logsee':
			logView()
			from prompt import *
			promptTwo()

		## ELIF SHOW
		elif x == 'show':
			showSysInfo()
			from prompt import *
			promptTwo()

		## ELIF USERS
		elif x == 'users':
			showUsers()
			from prompt import *
			promptTwo()

		## ELIF NETWORK
		elif x == 'network':
			showInterface()
			from prompt import *
			promptTwo()

		## ELIF BIN
		elif x == 'bin':
			showBin()
			from prompt import *
			promptTwo()

		## ELIF REPO
		elif x == 'repo':
			showRepositories()
			from prompt import *
			promptTwo()

		## ELIF DIRECTORY
		elif x == 'directory':
			showDir()
			from prompt import *
			promptTwo()

		## ELIF PCI
		elif x == 'pci':
			showPci()
			from prompt import *
			promptTwo()

		## ELIF BLOCK
		elif x == 'block':
			showBlk()
			from prompt import *
			promptTwo()

		## ELIF PORTS
		elif x == 'ports':
			showOpenPorts()
			from prompt import *
			promptTwo()

		## ELIF SETUFW
		elif x == 'setufw':
			setUfwEnable()
			setUfwRuleset()
			setUfwDenyIn()
			setAllowPort()
			from prompt import *
			promptTwo()

		## ELIF UPDATE
		elif x == 'update':
			updateOs()
			from prompt import *
			promptTwo()

		## ELIF PROMPT
		elif x == 'prompt':
			from prompt import *
			prompt()
			promptTwo()

		## ELIF LS
		elif x == 'ls':
			os.system("ls")
			from prompt import *
			promptTwo()

		## ELIF SPACE
		elif x == 'space':
			showSpace()
			from prompt import *
			promptTwo()

		## ELIF REMOVEAGE
		elif x == 'removeage':
			removeAge()
			from prompt import *
			promptTwo()

		## ELIF GROUPSEE
		elif x == 'groupsee':
			showGroupUsersPrompt()
			showGroupUsers()
			from prompt import *
			promptTwo()

		## ELIF CHANGEPASS
		elif x == 'changepass':
			promptPass()
			conditionalTestPass()
			from prompt import *
			promptTwo()

		## ELSE
		else:
			print "You're a " + x
			from prompt import *
			promptTwo()

		break
