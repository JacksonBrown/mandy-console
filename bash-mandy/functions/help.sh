#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


help_info(){
	## LIST OPT PRO/FUNC
	echo "List of available options: "
	echo
	printf "${CYAN}show${NC}: displays the system info \n"
	printf "${CYAN}users${NC}: displays the system users \n"
	printf "${CYAN}network${NC}: reads the /etc/network/interfaces file\n"
	printf "${CYAN}bin${NC}: show the bin directory \n"
	printf "${CYAN}repo${NC}: show the repositories in aptitude \n"
	printf "${CYAN}directory${NC}: display a input directory \n"
	printf "${CYAN}pci${NC}: show all devices connected via PCI bus \n"
	printf "${CYAN}ram${NC}: show all free ram in the system \n"
	printf "${CYAN}block${NC}: show all block devices connected to the system \n"
	printf "${CYAN}exit${NC}: exits Mandy Console \n"
	printf "${CYAN}ports${NC}: show all open ports \n"
	printf "${CYAN}setufw${NC}: sets up the ufw firewall to configuration \n"
	printf "${CYAN}update${NC}: updates the system \n"
	printf "${CYAN}removeuser${NC}: removes the specified 5 users \n"
	printf "${CYAN}removeage${NC}: removes and replaces the chage of 5 users \n"
	printf "${CYAN}space${NC}: show free disk space in the system \n"
	printf "${CYAN}editsudo${NC}: edits the /etc/sudoers file \n"
	printf "${CYAN}groupsee${NC}: view all of the users in a specified group \n"
	printf "${CYAN}changepass${NC}: change password of specified 5 users \n"
	printf "${CYAN}editsudoremove${NC}: remove specified 5 users from the sudo group \n"
	printf "${CYAN}logsee${NC}: view the tail of log files and creat log_mesg.txt \n"
	printf "${CYAN}deldir${NC}: delete a input directory \n"
	printf "${CYAN}cron${NC}: view all the cron files in /etc/ \n"
	printf "${CYAN}editservice${NC}: start, stop, or restart a service \n"
	printf "${CYAN}process${NC}: show processes on the system \n"
	printf "${CYAN}services${NC}: show services running on the system \n"	
	printf "${CYAN}shells${NC}: show shells on the system \n"
	printf "${CYAN}editssh${NC}: edit the sshd_config file \n"
	printf "${CYAN}editlightdm${NC}: edit lightdm configuration files \n"
	printf "${CYAN}removereadablehome${NC}: remove world readable perms on home dir files \n"
	printf "${CYAN}scan${NC}: runs a scan on an input network \n"
	printf "${CYAN}dumptcp${NC}: view tcp packets in new window \n"
	printf "${CYAN}howdoi${NC}: opens google in firefox web browser \n"
	printf "${CYAN}openpam${NC}: views the chosen pam file \n"
	printf "${CYAN}softwarescan${NC}: scans for prohibited hacking tools \n"
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Listed all functions in MANDY, entry \"help\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: echo" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
