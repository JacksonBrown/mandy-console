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
	print colored.yellow("Listing free ram in the system: ")
	subprocess.call(["free", "-h"])
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
	print colored.yellow("Listing available options: ");
	print colored.cyan("show") + ": displays the system info " #
	print colored.cyan("users") + ": displays the system users " #
	print colored.cyan("network") + ": reads the /etc/network/interfaces file" #
	print colored.cyan("bin") + ": show the bin directory " #
	print colored.cyan("repo") + ": show the repositories in aptitude " #
	print colored.cyan("directory") + ": display a input directory " #
	print colored.cyan("pci") + ": show all devices connected via PCI bus " #
	print colored.cyan("ram") + ": show all free ram in the system " #
	print colored.cyan("block") + ": show all block devices connected to the system " #
	print colored.cyan("exit") + ": exits Mandy Console " #
	print colored.cyan("ports") + ": show all open ports " #
	print colored.cyan("setufw") + ": sets up the ufw firewall to configuration " #
	print colored.cyan("update") + ": updates the system " #
	print colored.cyan("removeuser") + ": removes the specified 5 users " #
	print colored.cyan("removeage") + ": removes and replaces the chage of 5 users " #
	print colored.cyan("space") + ": show free disk space in the system " #
	print colored.cyan("editsudo") + ": edits the /etc/sudoers file " #
	print colored.cyan("groupsee") + ": view all of the users in a specified group " #
	print colored.cyan("changepass") + ": change password of specified 5 users " # 
	print colored.cyan("editsudoremove") + ": remove specified 5 users from the sudo group " #
	print colored.cyan("logsee") + ": view the tail of log files and create log_mesg.txt " #
	print colored.cyan("deldir") + ": delete a input directory " #
	print colored.cyan("cron") + ": view all the cron files in /etc/ " #
	print colored.cyan("editservice") + ": start, stop, or restart a service " #
	print colored.cyan("process") + ": show processes on the system " #
	print colored.cyan("services") + ": show services running on the system " #
	print colored.cyan("shells") +": show shells on the system " #
	print colored.cyan("editssh") + ": edit the sshd_config file " #
	print colored.cyan("editlightdm") + ": edit lightdm configuration file " #
	print colored.cyan("removereadablehome") + ": remove world readable perms on home dir files "
	print colored.cyan("dumptcp") + ": view tcp packets in new window " #
	print colored.cyan("howdoi") + ": opens google in firefox web browser " #
	print colored.cyan("openpam") + ": views the chosen pam file " #
	print colored.cyan("softwarescan") + ": scans for malicious software " #
	print colored.cyan("prompt") + ": displays the prompt at load up " #
	print colored.cyan("createuser") + ": creates specified 5 users " #
	print colored.cyan("editsysctl") + ": edits the sysctl.conf file if found. " #
	print colored.cyan("findtimestamp") + ": finds files edited within the last hour. " #
	print
	
	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"List all commands in MANDY, entry \"help\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: none\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DELETE USER FUNCTION
def deleteUser():
	print
	print colored.yellow('Enter usernames for deletion (there are five entries in total, type \"done\" on the extra entries): ')
	option_one_del = raw_input()
	option_two_del = raw_input()
	option_three_del = raw_input()
	option_four_del = raw_input()
	option_five_del = raw_input()

	# CONDITIONAL FOR OPTION VARS
	if option_one_del == 'done' or option_one_del == '':
		print colored.red("0: option skipped.");
	else:
		print colored.yellow('removing user ' + '"' + option_one_del + '":')
		os.system("sudo userdel " + option_one_del)
		print "OK."

	if option_two_del == 'done' or option_two_del == '':
		print colored.red("1: option skipped.");
	else:
		print colored.yellow('removing user ' + '"' + option_two_del + '":')
		os.system("sudo userdel " + option_two_del)
		print "OK."

	if option_three_del == 'done' or option_three_del == '':
		print colored.red("2: option skipped.");
	else:
		print colored.yellow('removing user ' + '"' + option_three_del + '":')
		os.system("sudo userdel " + option_three_del)
		print "OK."

	if option_four_del == 'done' or option_four_del == '':
		print colored.red("3: option skipped.");
	else:
		print colored.yellow('removing user ' + '"' + option_four_del + '":')
		os.system("sudo userdel " + option_four_del)
		print "OK."

	if option_five_del == 'done' or option_five_del == '':
		print colored.red("4: option skipped.");
	else:
		print colored.yellow('removing user ' + '"' + option_five_del + '":')
		os.system("sudo userdel " + option_five_del)
		print "OK."
	print


	print colored.yellow("Delete home directories (y/n)? ")
	option_homedir_del = raw_input()

	if option_homedir_del == 'y':

		if option_one_del != 'done':
			os.system("sudo rm -rf /home/" + option_one_del)
			print option_one_del + " home directory removed."
		else:
			print colored.red("0: option skipped.");

		if option_two_del != 'done':
			os.system("sudo rm -rf /home/" + option_two_del)
			print option_two_del + " home directory removed."
		else:
			print colored.red("1: option skipped.");

		if option_three_del != 'done':
			os.system("sudo rm -rf /home/" + option_three_del)
			print option_three_del + " home directory removed."
		else:
			print colored.red("2: option skipped.");

		if option_four_del != 'done':
			os.system("sudo rm -rf /home/" + option_four_del)
			print option_four_del + " home directory removed."
		else:
			print colored.red("3: option skipped.");

		if option_five_del != 'done':
			os.system("sudo rm -rf /home/" + option_five_del)
			print option_five_del + " home directory removed."
		else:
			print colored.red("4: option skipped.");

	else:
		print colored.red("option other than y specified, closing.")


	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove specified users in MANDY, entry \"removeuser\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo userdell USERVAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DIRECTORY DELETE FUNCTION
def directoryDelete():
	print
	print colored.yellow("Enter directory for deletion: ")
	dir_delete_option = raw_input()


	## IF EXISTS TEST
	if os.path.isdir(dir_delete_option):
		if os.path.exists(dir_delete_option):
			os.system("sudo rm -r -f " + dir_delete_option)
		else:
			print "The directory you entered is invalid or does not exist."
	print

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
	print
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

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Edit specified service in MANDY, entry \"deldir\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo service SERVICE VAR SERVICE OPT VAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## EDIT SSHD_CONFIG
def editSshd():
	print
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

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Open sshd_config file in MANDY, entry \"editssh\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: vi sshd_config_path\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## EDIT LIGHTDM CONF
def editLightdm():
	print
	print colored.yellow("Opening lightdm configuration file in vi: ")
	lightdm_path_one = "/usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf"
	lightdm_path_two = "/usr/share/lightdm/lightdm.conf"
	lightdm_path_three = "/etc/lightdm/lightdm.conf"

	if os.path.exists(lightdm_path_one):
		subprocess.call(["vi", lightdm_path_one])
	elif os.path.exists(lightdm_path_two):
		subprocess.call(["vi", lightdm_path_two])
	elif os.path.exists(lightdm_path_three):
		subprocess.call(["vi", lightdm_path_three])
	else:
		print colored.red("No lightdm config file was found ")

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Open lightdm configuration file in MANDY, entry \"editssh\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: vi lightdm_config_path\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


######################################################## ADD FROM HERE


## EDIT SUDOERS FILE
def editSudo():
	print
	print colored.yellow("Opening the sudoers file for editing: ")
	subprocess.call(["export", "EDITOR=nano"])
	os.system("sudo nano /etc/sudoers")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Opened the sudoers file via MANDY, entry \"editsudo\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo nano /etc/sudoers\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## VIEW LOG MESSAGES, WRITE TO TEXT FILES
def logView():
	print
	print colored.yellow("Listing log messages, exporting to file \"log_mesg.txt\":")
	print
	os.system("echo > logs/log_mesg.txt")
	print colored.yellow("which log file? ")
	print "\ngeneral=messages or syslog, \nboot=/var/log/boot.log, \ndebug=/var/log/debug, \nauth=/var/log/auth.log, \ndaemon=/var/log/daemon.log, \nkernel=/var/log/kern.log, \nother=specify a log file \n"
	log_view_option = raw_input()

	
	if log_view_option == 'general':

		## PRINT TO CONSOLE
		print colored.yellow("Tail of general log messages: ")

		syslog_path = "/var/log/syslog"
		if os.path.exists(syslog_path):
			syslog_open = open(syslog_path)

		messages_path = "/var/log/messages"
		if os.path.exists(messages_path):
			messages_open = open(messages_path)

		rsyslog_path = "/var/log/rsyslog"
		if os.path.exists(rsyslog_path):
			rsyslog_open = open(rsyslog_path)

		if os.path.exists(syslog_path):
			print syslog_open.read()
		elif os.path.exists(messages_path):
			print messages_open.read()
		elif os.path.exists(rsyslog_path):
			print rsyslog_open.read()
		else:
			print colored.red("syslog, messages, and rsyslog not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"GENERAL LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/syslog >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'boot':

		## PRINT TO CONSOLE
		print colored.yellow("Tail of boot log messages: ")

		boot_path = "/var/log/boot.log"
		if os.path.exists(boot_path):
			boot_open = open(boot_path)

		if os.path.exists(boot_path):
			print boot_open.read()
		else:
			print colored.red(boot_path + " not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"BOOT LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/boot.log >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'debug':
		## PRINT TO CONSOLE
		print colored.yellow("Tail of debug log messages: ")

		debug_path = "/var/log/debug"
		if os.path.exists(debug_path):
			debug_open = open(debug_path)

		if os.path.exists(debug_path):
			print debug_open.read()
		else:
			print colored.red(debug_path + " not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"DEBUG LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/debug >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'auth':

		## PRINT TO CONSOLE
		print colored.yellow("Tail of auth log messages (user login/authentication): ")

		auth_path = "/var/log/auth.log"
		if os.path.exists(auth_path):
			auth_open = open(auth_path)

		if os.path.exists(auth_path):
			print auth_open.read()
		else:
			print colored.red(auth_path + " not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"AUTH LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/auth.log >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'daemon':
		## PRINT TO CONSOLE
		print colored.yellow("Tail of daemon log messages: ")

		daemon_path = "/var/log/daemon.log"
		if os.path.exists(daemon_path):
			daemon_open = open(daemon_path)

		if os.path.exists(daemon_path):
			print daemon_open.read()
		else:
			print colored.red(daemon_path + " not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"DAEMON LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/daemon.log >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'kernel':
		## PRINT TO CONSOLE
		print colored.yellow("Tail of kernel log messages: ")

		kernel_path = "/var/log/kern.log"
		if os.path.exists(kernel_path):
			kernel_open = open(kernel_path)

		if os.path.exists(kernel_path):
			print kernel_open.read()
		else:
			print colored.red(kernel_path + " not found.")

		## PRINT TO TEXT FILE
		os.system("echo \"KERNEL LOG MESSAGES: \" >> logs/log_mesg.txt")
		os.system("sudo cat /var/log/kern.log >> logs/log_mesg.txt")
		os.system("echo >> logs/log_mesg.txt")

	elif log_view_option == 'other':
		print colored.red("enter log file name (not path): ")
		log_view_else = raw_input()

		lvp = "/var/log/" + log_view_else
		print lve.read()
	else:
		print colored.red("Option not found.")

	## TEST TO OPEN FILE
	print colored.yellow("View the file \"log_mesg.txt\" file now (y/n)?")
	log_view_option_two = raw_input()

	if log_view_option_two == 'y':
		os.system("gedit logs/log_mesg.txt")
	else:
		print colored.red("option other than y specified, closing.")

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Viewed log files via MANDY, entry \"logsee\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: cat/var/LOG_VAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW SYS INFO
def showSysInfo():
	print
	print colored.yellow("Listing system info: ")
	print

	print colored.red("User: ")
	print os.environ["USER"]
	print

	print colored.red("Architecture: ")
	os.system("uname -m")
	print

	print colored.red("System: ")
	subprocess.call(["uname"])
	print

	print colored.red("Uptime: ")
	subprocess.call(["uptime"])
	print

	print colored.red("Kernel Name: ")
	os.system("uname -s")
	print

	print colored.red("Network Host: ")
	os.system("uname -n")
	print

	print colored.red("Operating System: ")
	os.system("uname -o")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Viewed system info via MANDY, entry \"show\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: uname, print\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DISPLAY USERS
def showUsers():
	print
	passwd_var = "/etc/passwd"
	print colored.yellow("Listing users in system with BASH shell: ")

	# REVERT TO FOR SYSTEM COMMAND RUN INSTEAD OF PYTHON
	#os.system("cat /etc/passwd | grep -e \"bash\"")

	for line in open(passwd_var):
		if "bash" in line:
			sys.stdout.write(line)

	print colored.yellow("Listing users in system with KORN shell: ")

	# REVERT TO FOR SYSTEM COMMAND RUN INSTEAD OF PYTHON
	#os.system("cat /etc/passwd | grep -e \"ksh\"")

	for line in open(passwd_var):
		if "ksh" in line:
			sys.stdout.write(line)

	print colored.yellow("Listing users in system with C shell: ")
	
	# REVERT TO FOR SYSTEM COMMAND RUN INSREAD OF PYTHON
	#os.system("cat /etc/passwd | grep -e \"csh\"")

	for line in open(passwd_var):
		if "csh" in line:
			sys.stdout.write(line)

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show users in system via MANDY, entry \"users\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: cat /etc/passwd | grep -e \"expression\"\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## READ NETWORK INTERFACE
def showInterface():
	print
	print colored.yellow("Listing network interface: ")
	os.system("cat /etc/network/interfaces")

	print colored.yellow("Would you like to open the interfaces file (y/n)?")
	inter_opt = raw_input()
	if inter_opt == 'y':
		os.system("gedit /etc/network/interfaces")
	else:
		print colored.red("Option other than \"y\" specified.")

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show interfaces file via MANDY, entry \"network\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: cat /etc/network/interfaces\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW BIN FILES
def showBin():
	print
	print colored.yellow("Listing /bin and /sbin: ") + "\n"

	print colored.red("/bin directory: ")
	subprocess.call(["ls", "/bin"])

	print "\n ##### \n"

	print colored.red("/sbin directory: ")
	subprocess.call(["ls", "/sbin"])

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show bin and sbin dir via MANDY, entry \"bin\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: cat /etc/network/interfaces\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")
	

########################################################


## SHOW REPOSITORIES
def showRepositories():
	print
	print colored.yellow("Listing repositories: ") + "\n"

	sources_list = "/etc/apt/sources.list"
	if os.path.exists(sources_list):
		sources_open = open(sources_list)
		print sources_open.read()
	else:
		print colored.red(source_list + " not found.")

	sources_oprl = "/etc/apt/sources.list.d/official-package-repositories.list"
	if os.path.exists(sources_oprl):
		sources_oprl_open = open(sources_oprl)
		print sources_oprl_open.read()
	else:
		print colored.red(sources_oprl + " not found.")
	 
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show bin and sbin dir via MANDY, entry \"repo\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: cat /etc/network/interfaces\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")

	
########################################################


## SHOW DIRECTORY
def showDir():
	print
	print colored.yellow("Enter a directory: ")
	show_dir_var = raw_input()

	print colored.yellow("Listing all list of directory: ")
	subprocess.call(["ls", "-al", show_dir_var])

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Listing -al list of dir via MANDY, entry \"directory\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: ls -al\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")

	
########################################################


## SHOW PCI CONNECTED
def showPci():
	print
	print colored.yellow("Listing all devices connected via PCI: ")
	os.system("lspci")

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"All devices connected by pci via MANDY, entry \"pci\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: lspci\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")
	
	
########################################################


## SHOW BLOCK DEVICES
def showBlk():
	print
	print colored.yellow("Listing all block devices: ")
	subprocess.call(["lsblk", "-l"])

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"All block devices listed via MANDY, entry \"block\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: lsblk -l\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW OPEN PORTS
def showOpenPorts():
	print
	print colored.yellow("LIsting all open ports: ")
	subprocess.call(["netstat", "-auntpl"])

	print colored.yellow("Show IPTABLES enforeced rules (y/n)?")
	iptb_opt = raw_input()

	if iptb_opt == 'y':
		print "\n IP TABLE RULES ENFORECED: \n"
		subprocess.call(["iptables", "-L"])
	else:
		print colored.red("option other than \"y\" specified.")

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show all open ports via MANDY, entry \"ports\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: netstat -auntpl\" >> logs/log.txt")
	os.system("echo \"Commands Executed: iptables -L\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################

## SET UFW FUNCTION
def setUfwEnable():
	print
	print colored.yellow("Enabling UFW firewall: ")
	subprocess.call(["ufw", "enable"])

	print colored.cyan("UFW version used: ")
	subprocess.call(["ufw", "--version"])

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Enable UFW firewall via MANDY, entry \"setufw\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: ufw [enable/deny/default/allow/x]\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")

def setUfwRuleset():
	print
	print colored.yellow("Setting defualt ruleset to deny: ")
	subprocess.call(["ufw", "default", "deny"])
	print "OK."

def setUfwDenyIn():
	print
	print colored.yellow("Enter service(s) to set a deny ruleset in: ")
	service_deny = raw_input("> ")

	if service_deny != "":
		print colored.yellow("Setting deny ruleset in " + service_deny)
		subprocess.call(["ufw", "deny", "in", service_deny])

	
def setAllowPort():
	print
	print colored.yellow("Enter port(s) to allow in: ")
	port_allow = raw_input("> ")

	if port_allow != "":
		print colored.yellow("Setting allow in port " + port_allow)
		subprocess.call(["ufw", "allow", "in", port_allow])


########################################################


## UPDATEME
def updateOs():
	print
	print colored.yellow("The updates will automatically be installed, continue(y/n)? ")
	option_update = raw_input()

	if option_update == 'y':

		print colored.cyan("Fedora or Debian distro (1/2)?")
		option_fod = raw_input()


		## FEDORA IF TEST
		if option_fod == "1":
			print colored.yellow("Running update: ")
			subprocess.call([
					"sudo", 
					"yum", 
					"-y", 
					"update"
					])

		## DEBIAN IF TEST
		elif option_fod == "2":
			print colored.yellow("Running update: ")
			subprocess.call([
					"sudo", 
					"apt-get", 
					"--yes", 
					"--force-yes",
					"upgrade"
					])
		else:
			print colored.red("Invalid option specified. ")
	else:
		print colored.red("Option other than \"y\" specified. ")


	print colored.yellow("Would you like to install crakclib (y/n)? ")
	ins_cracklib_opt = raw_input()

	if ins_cracklib_opt == "y":
		subprocess.call([
				"sudo", 
				"apt-get", 
				"--yes", 
				"--force-yes", 
				"install", 
				"libpam-cracklib"
				])
	else:
		print colored.red("Option other than \"y\" specified. ")

	print colored.yellow("Opening update manager: ")
	subprocess.call(["update-manager"])

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Updated system via MANDY, entry \"update\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: upgrade/install/update-manager\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW DISK SPACE
def showSpace():
	print
	print colored.yellow("Listing free disk space: ")
	subprocess.call(["df", "-h"])
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Listed free disk space via MANDY, entry \"space\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: df -h\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## DELETE USER FUNCTION
def removeAge():
	print
	print colored.yellow('Enter usernames for chage (there are five entries in total, type \"done\" on the extra entries): ')
	option_one_age = raw_input()
	option_two_age = raw_input()
	option_three_age = raw_input()
	option_four_age = raw_input()
	option_five_age = raw_input()

	# CONDITIONAL FOR OPTION VARS
	if option_one_age == 'done' or option_one_age == '':
		print colored.red("0: option skipped.");
	else:
		print colored.yellow('removing user age ' + '"' + option_one_age + '":')
		os.system("sudo chage -M 30 " + option_one_age)
		print "OK."

	if option_two_age == 'done' or option_two_age == '':
		print colored.red("1: option skipped.");
	else:
		print colored.yellow('removing user age ' + '"' + option_two_age + '":')
		os.system("sudo chage -M 30 " + option_two_age)
		print "OK."

	if option_three_age == 'done' or option_three_age == '':
		print colored.red("2: option skipped.");
	else:
		print colored.yellow('removing user age ' + '"' + option_three_age + '":')
		os.system("sudo chage -M 30 " + option_three_age)
		print "OK."

	if option_four_age == 'done' or option_four_age == '':
		print colored.red("3: option skipped.");
	else:
		print colored.yellow('removing user age ' + '"' + option_four_age + '":')
		os.system("sudo chage -M 30 " + option_four_age)
		print "OK."

	if option_five_age == 'done' or option_five_age == '':
		print colored.red("4: option skipped.");
	else:
		print colored.yellow('removing user age ' + '"' + option_five_age + '":')
		os.system("sudo chage -M 30 " + option_five_age)
		print "OK."
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove age of specified users in MANDY, entry \"removeage\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo chage -M 30 USERVAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW GROUP USERS FUNCTION
def showGroupUsersPrompt():
	print colored.yellow("\nEnter the group to be viewed (type \"a\" to view all groups with all users): ")

def showGroupUsers():
	option_group = raw_input()
	print colored.yellow("Listing all matches in the " + option_group + " group: ")

	if option_group == "a":
		all_groups_dir = "/etc/group"
		all_groups = open(all_groups_dir)
		print all_groups.read()
	else:
		all_groups_dir_second = "/etc/group"
		for line in open(all_groups_dir_second):
			if option_group in line:
				sys.stdout.write(line)
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"View specified group in MANDY, entry \"removeage\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: none\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## CHANGE PASS
def promptPass():
	print colored.yellow("\nEnter users for password change (fine entries total, type \"done\" if an entry is blank): ")


def conditionalTestPass():

	option_one_pass = raw_input()
	option_two_pass = raw_input()
	option_three_pass = raw_input()
	option_four_pass = raw_input()
	option_five_pass = raw_input()

	if option_one_pass == 'done' or option_one_pass == '':
		print colored.red("0: option skipped.")
	else:
		print colored.yellow("changing " + option_one_pass + " password: ")
		subprocess.call(["sudo", "passwd", option_one_pass])

	if option_two_pass == 'done' or option_two_pass == '':
		print colored.red("1: option skipped.")
	else:
		print colored.yellow("changing " + option_two_pass + " password: ")
		subprocess.call(["sudo", "passwd", option_two_pass])

	if option_three_pass == 'done' or option_three_pass == '':
		print colored.red("2: option skipped.")
	else:
		print colored.yellow("changing " + option_three_pass + " password: ")
		subprocess.call(["sudo", "passwd", option_three_pass])

	if option_four_pass == 'done' or option_four_pass == '':
		print colored.red("3: option skipped.")
	else:
		print colored.yellow("changing " + option_four_pass + " password: ")
		subprocess.call(["sudo", "passwd", option_four_pass])

	if option_five_pass == 'done' or option_five_pass == '':
		print colored.red("4: option skipped.")
	else:
		print colored.yellow("changing " + option_five_pass + " password: ")
		subprocess.call(["sudo", "passwd", option_five_pass])
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Change passwords in MANDY, entry \"changepass\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo passwd PWOPT\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## EDIT SUDO REMOVE
def promptSudoGroupRemove():
	print colored.yellow("\nEnter users for sudo group remove (five entries total, type \"done\" if an entry is blank): ")

def conditionalTestSudoGroup():
	option_one_sudoers = raw_input()
	option_two_sudoers = raw_input()
	option_three_sudoers = raw_input()
	option_four_sudoers = raw_input()
	option_five_sudoers = raw_input()

	if option_one_sudoers == 'done' or option_one_sudoers == '':
		print colored.red("0: option skipped")
	else:
		print colored.yellow("removing " + option_one_sudoers + " from sudo group: " )
		subprocess.call(["sudo", "deluser", option_one_sudoers, "sudo"])

	if option_two_sudoers == 'done' or option_two_sudoers == '':
		print colored.red("1: option skipped")
	else:
		print colored.yellow("removing " + option_two_sudoers + " from sudo group: " )
		subprocess.call(["sudo", "deluser", option_two_sudoers, "sudo"])

	if option_three_sudoers == 'done' or option_three_sudoers == '':
		print colored.red("2: option skipped")
	else:
		print colored.yellow("removing " + option_three_sudoers + " from sudo group: " )
		subprocess.call(["sudo", "deluser", option_three_sudoers, "sudo"])

	if option_four_sudoers == 'done' or option_four_sudoers == '':
		print colored.red("3: option skipped")
	else:
		print colored.yellow("removing " + option_four_sudoers + " from sudo group: " )
		subprocess.call(["sudo", "deluser", option_four_sudoers, "sudo"])

	if option_five_sudoers == 'done' or option_five_sudoers == '':
		print colored.red("4: option skipped")
	else:
		print colored.yellow("removing " + option_five_sudoers + " from sudo group: " )
		subprocess.call(["sudo", "deluser", option_five_sudoers, "sudo"])
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove sudoers in MANDY, entry \"editsudoremove\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo deluser OPT sudo\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")

########################################################


## SHOW CRON
def showCron():
	print colored.yellow("\nListing cron files in /etc/: ")
	os.system("ls -l /etc/cron.*")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show cron files in MANDY, entry \"cron\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: ls -l CPV\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")

########################################################


## DEL DIR
def dirDelete():
	print colored.yellow("\nEnter directory for deletion: ")
	option_dir = raw_input()

	if os.path.exists(option_dir):
		subprocess.call(["sudo", "rm", "-r", "-f", option_dir])
		print "OK."
	else:
		print colored.red("The directory you entered is invalid or does not exist.")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove directory via MANDY, entry \"deldir\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo rm -rf DIR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW PROCESS
def showProcess():
	print colored.yellow("\nViewing proccesses currently running: ")
	print colored.cyan("Output will be OVERWRITTEN to logs/showprovess.txt")

	subprocess.call(["ps", "aux"])
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show system processes via MANDY, entry \"process\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: ps aux\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW SERVICES
def showServices():
	print colored.yellow("\nListing services currently running: ")
	os.system("sudo service --status-all")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show services via MANDY, entry \"services\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo service --status-all\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SHOW SHELLS
def showShells():
	print colored.yellow("\nListing all the shells in the system: ")
	shell_path = "/etc/shells"
	if os.path.exists(shell_path):
		shell_open = open(shell_path)
	else:
		print colored.red("/etc/shells file not found")

	print shell_open.read()

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Show services via MANDY, entry \"service\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo service --status-all\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")
	

########################################################


## REMOVE READABLE HOME DIRECTORIES
def rmReadableHomeDir():
	print colored.yellow("\nEnter users to remove world readable permissions (five entries total, type \"done\" for blanke entries): ")

	option_one_readable = raw_input()
	option_two_readable = raw_input()
	option_three_readable = raw_input()
	option_four_readable = raw_input()
	option_five_readable = raw_input()


	if option_one_readable == 'done' or option_one_readable == '':
		print colored.red("0: option skipped.")
	else:
		os.system("sudo chmod 0750 /home/" + option_one_readable)
		print "Other permissions changed."

	if option_two_readable == 'done' or option_two_readable == '':
		print colored.red("1: option skipped.")
	else:
		os.system("sudo chmod 0750 /home/" + option_two_readable)
		print "Other permissions changed."

	if option_three_readable == 'done' or option_three_readable == '':
		print colored.red("2: option skipped.")
	else:
		os.system("sudo chmod 0750 /home/" + option_three_readable)
		print "Other permissions changed."

	if option_four_readable == 'done' or option_four_readable == '':
		print colored.red("3: option skipped.")
	else:
		os.system("sudo chmod 0750 /home/" + option_four_readable)
		print "Other permissions changed."

	if option_five_readable == 'done' or option_five_readable == '':
		print colored.red("4: option skipped.")
	else:
		os.system("sudo chmod 0750 /home/" + option_five_readable)
		print "Other permissions changed."

	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Remove world perms via MANDY, entry \"removereadablehome\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo chmod 0750 /home/USERVAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## TCP CAPTURE
def tcpCapture():
	print colored.yellow("\nCapturing tcp output in xterm window. Enter interface to scan: ")
	tcp_dump_option = raw_input()


	os.system("sudo tcpdump -i " + tcp_dump_option)
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"View TCP via MANDY, entry \"dumptcp\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo xterm HOLD OPT DUMP OPT\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## HOW DO I
def howdoi():
	print colored.yellow("\nOpening google in web browser.")

	subprocess.call(["firefox", "www.google.com"])
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Open google via MANDY, entry \"howdoi\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: firefox www.google.com\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## OPEN PAM
def openPam():
	print colored.yellow("\nOpening input pam file: \n1=common-auth, \n2=common-password, \n3=common-account, \nother=enter specific pam file")

	option_pam = raw_input()

	if option_pam == "1":
		subprocess.call(["gedit", "/etc/pam.d/common-auth"])
	elif option_pam == "2":
		subprocess.call(["gedit", "/etc/pam.d/common-password"])
	elif option_pam == "3":
		subprocess.call(["gedit", "/etc/pam.d/common-account"])
	elif option_pam == "other":
		print colored.yellow("Enter the specified pam file: ")
		pam_spec_option = raw_input()
		os.system("gedit /etc/pam.d/" + pam_spec_option)
	else:
		print colored.red("Invalid input.")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Open pam files via MANDY, entry \"openpam\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: gedit PAM OPT\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## SOFTWARE SCAN
def softwareScan():
	print colored.yellow("\nScanning for: \nhydra \njtr \nnmap \nwireshark \naircrack \nsqlmap \nmetasploit \nnetcat \n")

	print colored.yellow("Hydra: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"hydra\"")
	print "LOCATE OUTPUT: "
	os.system("locate hydra | head -n 5")
	print "\n--------\n"

	print colored.yellow("John The Ripper: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"john\"")
	print "LOCATE OUTPUT: "
	os.system("locate john | head -n 5")
	print "\n--------\n"

	print colored.yellow("Nmap: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"nmap\"")
	print "LOCATE OUTPUT: "
	os.system("locate nmap | head -n 5")
	print "\n--------\n"

	print colored.yellow("Wireshark: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"wireshark\"")
	print "LOCATE OUTPUT: "
	os.system("locate wireshark | head -n 5")
	print "\n--------\n"

	print colored.yellow("Aircrack: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"aircrack\"")
	print "LOCATE OUTPUT: "
	os.system("locate aircrack | head -n 5")
	print "\n--------\n"

	print colored.yellow("Sqlmap: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"sqlmap\"")
	print "LOCATE OUTPUT: "
	os.system("locate sqlmap | head -n 5")
	print "\n--------\n"

	print colored.yellow("Metasploit: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"metasploit\"")
	print "LOCATE OUTPUT: "
	os.system("locate metasploit | head -n 5")
	print "\n--------\n"

	print colored.yellow("Netcat: ")
	print "DPKG OUTPUT: "
	os.system("dpkg -l | grep \"netcat\"")
	print "LOCATE OUTPUT: "
	os.system("locate netcat | head -n 5")
	os.system("ls /bin/nc")
	print "\n--------\n"

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Software scan via MANDY, entry \"softwarescan\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: locate, dpkg -l, grep\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## CREATE USER
def createUser():
	print colored.yellow("\nEnter users to be created (five entries total, type \"done\" if an entry is blank): ")
	option_one_create = raw_input()
	option_two_create = raw_input()
	option_three_create = raw_input()
	option_four_create = raw_input()
	option_five_create = raw_input()


	if option_one_create == 'done' or option_one_create == '':
		print colored.red("0: option skipped.");
	else:
		os.system("sudo adduser " + option_one_create)
		print "User created."

	if option_two_create == 'done' or option_two_create == '':
		print colored.red("1: option skipped.");
	else:
		os.system("sudo adduser " + option_two_create)
		print "User created."

	if option_three_create == 'done' or option_three_create == '':
		print colored.red("2: option skipped.");
	else:
		os.system("sudo adduser " + option_three_create)
		print "User created."
		
	if option_four_create == 'done' or option_four_create == '':
		print colored.red("3: option skipped.");
	else:
		os.system("sudo adduser " + option_four_create)
		print "User created."
		
	if option_five_create == 'done' or option_five_create == '':
		print colored.red("4: option skipped.");
	else:
		os.system("sudo adduser " + option_five_create)
		print "User created."
		

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Add users via MANDY, entry \"createuser\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo adduser VAR\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")
		

########################################################


## EDIT SYSCTL
def editSysctl():
	print colored.yellow("\nOpening sysctl for editing in vi: ")

	sysctl_path = "/etc/sysctl.conf"

	if os.path.exists(sysctl_path):
		subprocess.call(["sudo", "vi", sysctl_path])
	else:
		print colored.red("sysctl.conf file not found.")
	print

	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Edit sysctl.conf via MANDY, entry \"editsysctl\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo vi sysctl_path\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


########################################################


## FIND TIMESTAMP
def findTimestamp():
	print colored.yellow("\nEnter directory: ")
	find_directory = raw_input()

	if os.path.exists(find_directory):
		print colored.yellow("Listing files edited within the last hour in the " + find_directory + " directory.")
		os.system("sudo find " + find_directory + " -type f -mmin -60 | xargs ls -l")
	else:
		print colored.red("The directory you entered is invalid or does not exist.")
	print
	
	##LOG UPDATER
	os.system("echo >> logs/log.txt")
	os.system("echo `date` >> logs/log.txt")
	os.system("echo \"Find edited files within last hour via MANDY, entry \"findtimestamp\".\" >> logs/log.txt")
	os.system("echo \"Commands Executed: sudo find DIRVAR -type f -mmin 60 | xargs ls -l\" >> logs/log.txt")
	os.system("echo >> logs/log.txt")


# YOLO

