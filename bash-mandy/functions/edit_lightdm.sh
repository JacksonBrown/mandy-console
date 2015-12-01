#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

edit_lightdm(){
	printf "${YELLOW}Opening lightdm configuration files${NC}: \n"

	if [ -e /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf ]; then
		if (sudo gedit /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf); then
			echo "OK."
		fi
	else
		echo "file 50-ubnutu.conf non existent, moving on to next entry."
	fi


	if [ -e /usr/share/lightdm/lightdm.conf ]; then
		if (sudo gedit /usr/share/lightdm/lightdm.conf); then
			echo "OK."
		fi
	else
		echo "file lightdm.conf non existent, moving on to next entry."
	fi


	if [ -e /etc/lightdm/lightdm.conf ]; then
		if (sudo gedit /etc/lightdm/lightdm.conf); then
			echo "OK."
		fi
	else
		echo "file lightdm.conf in /etc/lightdm not found, no other entry available."
	fi

	#sudo gedit /etc/lightdm/lightdm.conf
	echo "Goodbye."
	
	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Open lightdm configuration files via MANDY, entry \"disableubuntuguest\"." >> logs/log.txt
	echo "Commands Executed: sudo gedit DIR/FILE" >> logs/log.txt
}

