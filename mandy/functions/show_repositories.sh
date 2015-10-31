#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_repositories(){
	printf "${YELLOW}Listing repositories${NC}: "
	echo
	if (printf "${RED}`cat /etc/apt/sources.list`${NC} \n"); then
		echo "OK."
	fi
	echo
	if (printf "${RED}`cat /etc/apt/sources.list.d/official-package-repositories.list`${NC} \n"); then
		echo "OK."
	fi
	echo

	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "View current repositories via MANDY, entry \"repo\"." >> logs/log.txt
	echo "Commands Executed: cat /etc/apt/sources.list" >> logs/log.txt
	echo "Commands Executed: cat /etc/apt/sources.list.d/official-package-repositories.list" >> logs/log.txt
	echo >> logs/log.txt
}
