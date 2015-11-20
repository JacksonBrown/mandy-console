#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_space(){
	printf "${YELLOW}Listing free disk space${NC}: \n"
	
	printf "${RED}"
		df
	printf "${NC}"

	echo

	## VAR LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Views free disk space via MANDY, entry \"space\"." >> logs/log.txt
	echo "Commands Executed: df" >> logs/log.txt
	echo >> logs/log.txt
}
