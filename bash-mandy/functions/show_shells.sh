#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_shells(){
	printf "${YELLOW}Listing all the shells in system${NC}: \n"
	echo
	if(printf "${RED}`cat -n /etc/shells`${NC} \n"); then
		echo "OK."
	fi
	echo


	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Viewed shells in system via MANDY, entry \"bin\"." >> logs/log.txt
	echo "Commands Executed: cat -n /etc/shells" >> logs/log.txt
	echo >> logs/log.txt
}