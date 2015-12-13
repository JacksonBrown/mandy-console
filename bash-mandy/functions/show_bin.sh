#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_bin(){
	printf "${YELLOW}Listing /bin directory${NC}: \n"
	echo
	if (printf "${RED}`ls /bin`${NC} \n"); then
		echo "OK."
	fi

	echo

	printf "${YELLOW}Listing /sbin directory${NC}: \n"
	if (printf "${RED}`ls /sbin`${NC} \n"); then
		echo "OK."
	fi

	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Viewed bin files via MANDY, entry \"bin\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: ls /bin; ls /sbin" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
