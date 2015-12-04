#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

prompt_show_group_users(){
	echo
	printf "${YELLOW}Enter the group to be viewed (type \"a\" to view all groups with all users)${NC}: \n"
}

show_group_users(){
	read option_group
	echo
	printf "${YELLOW}Listing all users in the $option_group group${NC}: \n"
	if [ $option_group = "a" ]; then
		printf "${RED}`cat /etc/group`${NC} \n"
	fi
	printf "${RED}`cat /etc/group | grep $option_group`${NC} \n"
	echo

	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "View all users of a group via MANDY, entry \"groupsee\"." >> logs/log.txt
	echo "Commands Executed: cat /etc/group" >> logs/log.txt
	echo "Commands Executed: cat /etc/group | grep $option_group" >> logs/log.txt
	echo >> logs/log.txt
}
