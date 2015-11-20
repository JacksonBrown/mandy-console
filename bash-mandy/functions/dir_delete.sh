#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

dir_delete(){
	printf "${YELLOW}Enter directory for deletion${NC}: \n"
	read option_one_dir

	if [ -d $option_one_dir ]; then
		if(printf "${RED}`sudo rm -r -f $option_one_dir`${NC}"); then
			echo "OK."
		fi
	else
		printf "${RED}The directory you entered is invalid or does not exist.${NC} \n"
	fi

	##LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Removed directory via MANDY, entry \"deldir\"." >> logs/log.txt
	echo "Commands Executed: sudo rm -r -f DIRECTORY VAR" >> logs/log.txt
	echo >> logs/log.txt
}
