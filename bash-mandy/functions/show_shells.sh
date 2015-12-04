#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_shells(){
	printf "${YELLOW}Listing all the shells in system${NC}: \n"
	echo
	if(printf "${RED}`cat -n /etc/shells`${NC} \n"); then
		echo "OK."
	fi
	echo


	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Viewed shells in system via MANDY, entry \"bin\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat -n /etc/shells" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
