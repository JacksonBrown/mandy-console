#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys
from clint.textui import colored

def showFree():
	print
	print colored.yellow("Listing free ram in the system. \n")
	subprocess.call(["free"])
	print


	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"List all free RAM via MANDY, entry \"ram\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: free\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


