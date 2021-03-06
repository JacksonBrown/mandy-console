#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_cron(){
	printf "${YELLOW}Listing cron files in /etc${NC}: \n"
	echo
	if(printf "${RED}`ls /etc/cron.*`${NC} \n"); then
		echo "OK."
		ls /etc/cron.* > $mandy_dir/logs/cron_files.txt
	fi
	echo

    ## LOG UPDATER
    echo >> $mandy_dir/logs/log.txt
    echo "`date`" >> $mandy_dir/logs/log.txt
    echo "Viewed cron files via MANDY, entry \"cron\"." >> $mandy_dir/logs/log.txt
    echo "Commands Executed: ls /etc/cron.*" >> $mandy_dir/logs/log.txt
    echo >> $mandy_dir/logs/log.txt
}
