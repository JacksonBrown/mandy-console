#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_blk(){
	printf "${YELLOW}Listing all block devices${NC}: \n"
	echo
	if(printf "${RED}`lsblk -l`${NC} \n"); then
		echo "OK."
	fi
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "List all block devices via MANDY, entry \"block\"." >> logs/log.txt
	echo "Commands Executed: lsblk -l" >> logs/log.txt
	echo >> logs/log.txt
}
