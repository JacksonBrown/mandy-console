#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


souce ../mconsole.sh


show_process(){
	printf "${YELLOW}Viewing processes currently running${NC}: \n"
	printf "${CYAN}Output will be OVERWRITTEN to logs/show_process.txt${NC}. \n"
	echo
	printf "${RED}"
		ps aux
		ps aux > logs/show_process.txt
	printf "${NC}"
		echo "OK."
	echo

    ## LOG UPDATER
    echo >> $mandy_dir/logs/log.txt
    echo "`date`" >> $mandy_dir/logs/log.txt
    echo "Viewed system processes via MANDY, entry \"cron\"." >> $mandy_dir/logs/log.txt
    echo "Commands Executed: ps aux" >> $mandy_dir/logs/log.txt
    echo >> $mandy_dir/logs/log.txt
}
