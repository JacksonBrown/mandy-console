#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


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
	echo >> $mand_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Removed directory via MANDY, entry \"deldir\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo rm -r -f DIRECTORY VAR" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
