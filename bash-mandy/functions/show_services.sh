#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_services(){
	printf "${YELLOW}Listing services currently running (will require root login)${NC}: \n"
	echo
	if (printf "${RED}`sudo service --status-all`${NC} \n"); then
		echo "OK."
	fi
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "View running services via MANDY, entry \"editservice\"." >> logs/log.txt
	echo "Commands Executed: sudo service --status-all" >> logs/log.txt
	echo >> logs/log.txt
}