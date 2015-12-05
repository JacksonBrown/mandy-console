#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_free(){
	printf "${YELLOW}Listing free RAM in system${NC}: \n"
	echo
	if(printf "${RED}`free -h`${NC} \n"); then
		echo "OK."
	fi
	echo

	##LOG UPDATER

	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "List all free RAM via MANDY, entry \"ram\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: free" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
