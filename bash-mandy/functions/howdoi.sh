#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


howdoi(){
	printf "${YELLOW}Opening google in web browser.${NC} \n"
	if (firefox www.google.com &); then
		echo "OK."
	fi

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Opened google in MANDY, entry \"help\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: links" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
