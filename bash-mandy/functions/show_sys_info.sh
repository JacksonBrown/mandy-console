#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_sys_info(){
	printf "${YELLOW}Listing system info${NC}: \n"
	echo
	echo "User: $USER"
	echo "Architecture: `uname -m`"
	echo "System: `uname`"
	echo "Uptime: `uptime`"
	echo "Kernel Name: `uname -s`"
	echo "Network Host: `uname -n`"
	echo "Host Name: `uname -m`"
	echo "Operating System: `uname -o`"
	echo

	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Displays system info via MANDY, entry \"show\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: echo" >> $mandy_dir/logs/log.txt
	echo "Commands Executed: uname OPTION_VAR" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
