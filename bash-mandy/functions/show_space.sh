#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_space(){
	printf "${YELLOW}Listing free disk space${NC}: \n"
	
	printf "${RED}"
		df -h
	printf "${NC}"

	echo

	## VAR LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Views free disk space via MANDY, entry \"space\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: df" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
