#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_services(){
	printf "${YELLOW}Listing services currently running (will require root login)${NC}: \n"
	echo
	if (printf "${RED}`sudo service --status-all`${NC} \n"); then
		echo "OK."
	fi
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "View running services via MANDY, entry \"editservice\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo service --status-all" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
