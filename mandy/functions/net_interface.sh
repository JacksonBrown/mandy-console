#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

net_interface(){
	printf "${YELLOW}Listing network interface${NC}: \n"
	echo
	if (printf "${RED}`cat /etc/network/interfaces`${NC} \n"); then
		echo "OK."
		printf "${YELLOW}Would you like to open the interfaces file (y/n)?${NC} \n"
		read inter_opt
		if [ $inter_opt = "y" ]; then
			sudo gedit /etc/network/interfaces
		fi
	fi
	echo

	## LOG UPDATE
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Viewed network interfaces via MANDY, entry \"network\"." >> logs/log.txt
	echo "Commands Executed: cat /etc/network/interfaces" >> logs/log.txt
	echo >> logs/log.txt
}
