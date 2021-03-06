#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_open_ports(){
	printf "${YELLOW}Listing all open ports${NC}: \n"
	echo
	if(printf "${RED}`netstat -auntpl`${NC} \n"); then
		echo "OK."
	fi
	echo
	echo "IP TABLE RULES ALLOWED"
	echo
	if(printf "${RED}`sudo iptables -L`${NC} \n"); then
		echo "OK."
	fi
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Shows all open ports via MANDY, entry \"update\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: netstat -auntpl" >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo iptables -L" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
