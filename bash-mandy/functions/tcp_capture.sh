#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


tcp_capture(){
	printf "${YELLOW}Capture tcp in new xterm window.${NC} \n"
	printf "${YELLOW}enter interface to scan${NC} \n"
	read tcp_dump_option

	## WRITING TO XTERM
	if (sudo xterm -hold -e "tcpdump -i $tcp_dump_option" &); then
		echo "OK."
	fi

	##LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Viewed tcp via MANDY, entry \"dumptcp\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo tcpdump -i TCP_OPTION_VAR" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
