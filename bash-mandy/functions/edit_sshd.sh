#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


edit_sshd(){
	printf "${YELLOW}Opening sshd_config file in vi${NC}: \n"

	if [ -e /etc/ssh/sshd_config ]; then
		if(vi /etc/ssh/sshd_config); then
			echo "OK."
		fi
	else
		printf "${RED}sshd_config file does not exist.${NC} \n"
	fi

	##LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Removed directory via MANDY, entry \"editssh\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo rm -r -f DIRECTORY VAR" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
