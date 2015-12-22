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
	print "List of available options: ";
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
	print colored.cyan("setufw") + ": sets up the ufw firewall to configuration "
	print colored.cyan("update") + ": updates the system "
	print colored.cyan("removeuser") + ": removes the specified 5 users " #
	print colored.cyan("removeage") + ": removes and replaces the chage of 5 users "
	print colored.cyan("space") + ": show free disk space in the system "
	print colored.cyan("editsudo") + ": edits the /etc/sudoers file " #
	print colored.cyan("groupsee") + ": view all of the users in a specified group "
	print colored.cyan("changepass") + ": change password of specified 5 users "
	print colored.cyan("editsudoremove") + ": remove specified 5 users from the sudo group "
	print colored.cyan("logsee") + ": view the tail of log files and create log_mesg.txt " #
	print colored.cyan("deldir") + ": delete a input directory " #
	print colored.cyan("cron") + ": view all the cron files in /etc/ "
	print colored.cyan("editservice") + ": start, stop, or restart a service " #
	print colored.cyan("process") + ": show processes on the system "
	print colored.cyan("services") + ": show services running on the system "
	print colored.cyan("shells") +": show shells on the system "
	print colored.cyan("editssh") + ": edit the sshd_config file " #
	print colored.cyan("editlightdm") + ": edit lightdm configuration file " #
	print colored.cyan("removereadablehome") + ": remove world readable perms on home dir files "
	print colored.cyan("scan") + ": runs a scan on an input network "
	print colored.cyan("prompt") + ": displays the prompt at load up "
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
	print

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
		else: 
			print colored.red("No Bash shell users found.")

	print colored.yellow("Listing users in system with KORN shell: ")

	# REVERT TO FOR SYSTEM COMMAND RUN INSTEAD OF PYTHON
	#os.system("cat /etc/passwd | grep -e \"ksh\"")

	for line in open(passwd_var):
		if "ksh" in line:
			sys.stdout.write(line)
		else:
			print colored.red("No Korn shell users found.")

	print colored.yellow("Listing users in system with C shell: ")
	
	# REVERT TO FOR SYSTEM COMMAND RUN INSREAD OF PYTHON
	#os.system("cat /etc/passwd | grep -e \"csh\"")

	for line in open(passwd_var):
		if "csh" in line:
			sys.stdout.write(line)
		else:
			print colored.red("No C shell users found.")

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

# YOLO

