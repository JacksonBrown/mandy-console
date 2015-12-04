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
	printf "${YELLOW}wlan0 or eth0?${NC} \n"
	read tcp_dump_option

	if [ "$tcp_dump_option" = "wlan0" ] || [ "$tcp_dump_option" = "eth0" ]; then

		## WRITING TO XTERM
		if (sudo xterm -hold -e "tcpdump -i $tcp_dump_option" &); then
			echo "OK."
		fi

	else
		printf "${RED}Input devie was not eth0 nor wlan0, exiting."
	fi

	##LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Viewed tcp via MANDY, entry \"dumptcp\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo tcpdump -i TCP_OPTION_VAR" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
