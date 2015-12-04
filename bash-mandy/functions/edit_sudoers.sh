#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


edit_sudoers(){
	printf "${YELLOW}Opening the sudoers file for editing${NC}: \n"
	export EDITOR=nano
	sudo nano /etc/sudoers
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Opened the sudoers file via MANDY, entry \"editsudo\"" >> $mandy_dir/logs/log.txt
	echo "Commands Executed: export EDITOR=nano" >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo nano /etc/sudoers" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
