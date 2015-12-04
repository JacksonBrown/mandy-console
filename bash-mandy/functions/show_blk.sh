#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_blk(){
	printf "${YELLOW}Listing all block devices${NC}: \n"
	echo
	if(printf "${RED}`lsblk -l`${NC} \n"); then
		echo "OK."
	fi
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "List all block devices via MANDY, entry \"block\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: lsblk -l" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
