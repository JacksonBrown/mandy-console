#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_checklist(){
	printf "${CYAN}Mark off on piece of paper as you go along (note this is not fully determined)${NC}: \n"
	echo
	echo
	printf "${RED}################ CHECKLIST ################${NC} \n"
	echo
	printf "${YELLOW}"
	echo 'update linux kernel'
	echo 'max password age must be set'
	echo 'remove samba'
	echo 'remove telnet'
	echo 'disable root login ssh'
	echo 'remove netcat backdoor'
	echo 'check for hacking tools'
	echo 'update bash'
	echo 'auto check for updates daily'
	echo 'change insecure passwords ESPECIALLY ROOT'
	echo 'enable firewall'
	echo 'install updates'
	echo 'disable guest account'
	echo 'remove prohibited media files'
	echo 'check for php backdoor'
	echo 'two root accounts'
	echo 'user ID under 1000'
	echo 'configure DNS server'
	echo 'configure Web Server'
	echo 'check localhost files'
	echo 'remove unauthorized users'
	echo 'remove unauthorized groups'
	echo 'remove unauthorized administrators'
	echo 'make sure all users have passwords'
	printf "${NC}"
}
