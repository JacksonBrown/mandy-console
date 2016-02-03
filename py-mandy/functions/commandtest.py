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

		## ELIF EDIT SUDO REMOVE
		elif x == 'editsudoremove':
			promptSudoGroupRemove()
			conditionalTestSudoGroup()
			from prompt import *
			promptTwo()

		## ELIF CRON
		elif x == 'cron':
			showCron()
			from prompt import *
			promptTwo()

		## ELIF DELDIR
		elif x == 'deldir':
			dirDelete()
			from prompt import *
			promptTwo()

		## ELIF PROCESS
		elif x == 'process':
			showProcess()
			from prompt import *
			promptTwo()

		## ELIF SHELLS
		elif x == 'shells':
			showShells()
			from prompt import *
			promptTwo()

		## ELIF SERVICE
		elif x == 'services':
			showServices()
			from prompt import *
			promptTwo()

		## ELIF RMREADABLEHOME
		elif x == 'removereadablehome':
			rmReadableHomeDir()
			from prompt import *
			promptTwo()

		## ELIF DUMPTCP
		elif x =='dumptcp':
			tcpCapture()
			from prompt import *
			promptTwo()

		## ELIF HOWDOI
		elif x == 'howdoi':
			howdoi()
			from prompt import *
			promptTwo()

		## ELIF OPENPAM
		elif x == 'openpam':
			openPam()
			from prompt import *
			promptTwo()

		## ELIF SOFTWARESCAN
		elif x == 'softwarescan':
			softwareScan()
			from prompt import *
			promptTwo()

		## ELIF CREATEUSER
		elif x == 'createuser':
			createUser()
			from prompt import *
			promptTwo()

		## ELIF EDITSYSCTL
		elif x == 'editsysctl':
			editSysctl()
			from prompt import *
			promptTwo()

		## ELIF FINDTIMESTAMP
		elif x == 'findtimestamp':
			findTimestamp()
			from prompt import *
			promptTwo()

		## ELIF CHANGEHOSTNAME
		elif x == 'changehostname':
			changeHostName()
			from prompt import *
			promptTwo()

		## ELIF REDVERSION
		elif x == 'red':
			from prompt import *
			redPrompt()
			promptTwo()

		## ELIF MANDYHISTORY
		elif x == 'mandyhistroy':
			history_var_path = "../logs/log.txt"

			if os.path.exists(history_var_path):
				history_var = open(history_var_path)
				print history_var.read()
			else:
				print "history_var_path variable is invalid."

		## ELSE
		else:
			print "You're a " + x
			from prompt import *
			promptTwo()

		break
