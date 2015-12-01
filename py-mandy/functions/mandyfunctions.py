#!/usr/bin/python

# IMPORTS
import os
import subprocess
import sys
from clint.textui import colored
from array import *


# FUNCTIONS



## SHOW FREE RAM FUNCTION
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


########################################################


## SHOW HELP FUNCTION
def showHelp():
	print
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
	
	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"List all commands in MANDY, entry \"ram\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: none\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DELETE USER FUNCTION
def deleteUser():
	print colored.yellow('Enter usernames for deletion (there are five entries in total, type \"done\" on the extra entries): ')
	option_one_del = raw_input()
	option_two_del = raw_input()
	option_three_del = raw_input()
	option_four_del = raw_input()
	option_five_del = raw_input()
	print


	# CONDITIONAL FOR OPTION VARS
	if option_one_del == 'done':
		print "0: option one not set, skipping.";
	else:
		print colored.yellow('removing user ' + '"' + option_one_del + '":')
		os.system("sudo userdel " + option_one_del)
		print "OK."

	if option_two_del == 'done':
		print "0: option one not set, skipping.";
	else:
		print colored.yellow('removing user ' + '"' + option_two_del + '":')
		os.system("sudo userdel " + option_two_del)
		print "OK."

	if option_three_del == 'done':
		print "0: option one not set, skipping.";
	else:
		print colored.yellow('removing user ' + '"' + option_three_del + '":')
		os.system("sudo userdel " + option_three_del)
		print "OK."

	if option_four_del == 'done':
		print "0: option one not set, skipping.";
	else:
		print colored.yellow('removing user ' + '"' + option_four_del + '":')
		os.system("sudo userdel " + option_four_del)
		print "OK."

	if option_five_del == 'done':
		print "0: option one not set, skipping.";
	else:
		print colored.yellow('removing user ' + '"' + option_five_del + '":')
		os.system("sudo userdel " + option_five_del)
		print "OK."


	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove specified users in MANDY, entry \"removeuser\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo userdell USERVAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DIRECTORY DELETE FUNCTION
def directoryDelete():
	print colored.yellow("Enter directory for deletion: ")
	dir_delete_option = raw_input()


	## IF EXISTS TEST
	if os.path.isdir(dir_delete_option):
		if os.path.exists(dir_delete_option):
			os.system("sudo rm -r -f " + dir_delete_option)
		else:
			print "The directory you entered is invalid or does not exist."


	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove specified directory in MANDY, entry \"deldir\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo rm -r -f DIRVAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## ADD CLEAR
def clearFunc():
	os.system("clear")


########################################################


## EDIT SERVICE
def editService():
	print colored.yellow("Enter service to be configured: ")
	service_option_one = raw_input()
	print colored.yellow("Enter action to be taken on " + service_option_one + ": ")
	service_option_two = raw_input()

	if service_option_one == "apache2":
		if service_option_two == "restart":
			os.system ("sudo service apache2 restart")
		elif service_option_two == "start":
			os.system("sudo service apache2 start")
		elif service_option_two == "stop":
			os.system("sudo service apache2 stop")
		else:
			print colored.yellow("option not found")

	if service_option_one == "mysql":
		if service_option_two == "restart":
			os.system ("sudo service mysql restart")
		elif service_option_two == "start":
			os.system("sudo service mysql start")
		elif service_option_two == "stop":
			os.system("sudo service mysql stop")
		else:
			print colored.yellow("option not found")

	if service_option_one == "vsftpd":
		if service_option_two == "restart":
			os.system ("sudo service vsftpd restart")
		elif service_option_two == "start":
			os.system("sudo service vsftpd start")
		elif service_option_two == "stop":
			os.system("sudo service vsftpd stop")
		else:
			print colored.yellow("option not found")
		
	if service_option_one == "gdm":
		if service_option_two == "restart":
			os.system ("sudo service gdm restart")
		elif service_option_two == "start":
			os.system("sudo service gdm start")
		elif service_option_two == "stop":
			os.system("sudo service gdm stop")
		else:
			print colored.yellow("option not found")	

	if service_option_one == "lightdm":
		if service_option_two == "restart":
			os.system ("sudo service lightdm restart")
		elif service_option_two == "start":
			os.system("sudo service lightdm start")
		elif service_option_two == "stop":
			os.system("sudo service lightdm stop")
		else:
			print colored.yellow("option not found")
		
	if service_option_one == "mdm":
		if service_option_two == "restart":
			os.system ("sudo service mdm restart")
		elif service_option_two == "start":
			os.system("sudo service mdm start")
		elif service_option_two == "stop":
			os.system("sudo service mdm stop")
		else:
			print colored.yellow("option not found")	

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Edit specified service in MANDY, entry \"deldir\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo service SERVICE VAR SERVICE OPT VAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## EDIT SSHD_CONFIG
def editSshd():
	print colored.yellow("Opening sshd_config file in vi: ")
	sshd_path = "/etc/ssh/sshd_config"
	ssh_path = "/etc/ssh/ssh_config"

	if os.path.exists(sshd_path):
		subprocess.call(["vi", sshd_path])
	else:
		print colored.red("sshd_config file was not found, attempting to open ssh_config")
		if os.path.exists(ssh_path):
			subprocess.call(["vi", ssh_path])
		else:
			print colored.red("returning to prompt")

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Open sshd_config file in MANDY, entry \"editssh\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: vi sshd_config_path\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


