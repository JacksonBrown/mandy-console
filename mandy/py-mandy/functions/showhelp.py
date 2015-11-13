#!/usr/bin/python

# IMPORTS
import subprocess
from clint.textui import colored

# CREATE HELP FUNCTION

def showHelp():
	print "List of available options: ";
	print colored.cyan("show") + ": displays the system info "
	print colored.cyan("users") + ": displays the system users "
	print colored.cyan("network") + ": reads the /etc/network/interfaces file"
	print colored.cyan("bin") + ": show the bin directory "
	print colored.cyan("repo") + ": show the repositories in aptitude "
	print colored.cyan("directory") + ": display a input directory "
	print colored.cyan("pci") + ": show all devices connected via PCI bus "
	print colored.cyan("ram") + ": show all free ram in the system "
	print colored.cyan("block") + ": show all block devices connected to the system "
	print colored.cyan("exit") + ": exits Mandy Console "
	print colored.cyan("ports") + ": show all open ports "
	print colored.cyan("setufw") + ": sets up the ufw firewall to configuration "
	print colored.cyan("update") + ": updates the system "
	print colored.cyan("removeuser") + ": removes the specified 5 users "
	print colored.cyan("removeage") + ": removes and replaces the chage of 5 users "
	print colored.cyan("space") + ": show free disk space in the system "
	print colored.cyan("editsudo") + ": edits the /etc/sudoers file "
	print colored.cyan("groupsee") + ": view all of the users in a specified group "
	print colored.cyan("changepass") + ": change password of specified 5 users "
	print colored.cyan("editsudoremove") + ": remove specified 5 users from the sudo group "
	print colored.cyan("logsee") + ": view the tail of log files and creat log_mesg.txt "
	print colored.cyan("deldir") + ": delete a input directory "
	print colored.cyan("cron") + ": view all the cron files in /etc/ "
	print colored.cyan("editservice") + ": start, stop, or restart a service "
	print colored.cyan("process") + ": show processes on the system "
	print colored.cyan("services") + ": show services running on the system "
	print
