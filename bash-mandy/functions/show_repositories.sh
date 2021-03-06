#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


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

	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "View current repositories via MANDY, entry \"repo\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat /etc/apt/sources.list" >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat /etc/apt/sources.list.d/official-package-repositories.list" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
