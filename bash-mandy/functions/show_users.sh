#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


show_users(){
	printf "${YELLOW}Listing users in system with BASH shell${NC}: \n"
	echo
	if (printf "${RED}`cat /etc/passwd | grep -e "bash"`${NC} \n"); then
		echo "OK."
	fi

        printf "${YELLOW}Listing users in system with KORN shell${NC}: \n"
        echo
        if (printf "${RED}`cat /etc/passwd | grep -e "ksh"`${NC} \n"); then
                echo "OK."
        fi

        printf "${YELLOW}Listing users in system with C shell${NC}: \n"
        echo
        if (printf "${RED}`cat /etc/passwd | grep -e "csh"`${NC} \n"); then
                echo "OK."
        fi

	printf "${YELLOW}Would you like to open the /etc/passwd file (y/n)? ${NC} \n"
	read open_passwd_option
	if [ "$open_passwd_option" = "y" ]; then
		if (sudo gedit /etc/passwd &); then
			echo "OK."
		fi
	else
		echo "Option other than \"y\" specified."
	fi

	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Show users in system via MANDY, entry \"users\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat /etc/passwd | grep -e \"bash\"" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}
