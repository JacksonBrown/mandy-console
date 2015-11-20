#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

delete_user(){
	printf "${YELLOW}Enter usernames for deletion (there are five entries in total, type \"done\" on the extra entries)${NC}: \n"
	read option_one_del
	read option_two_del
	read option_three_del
	read option_four_del
	read option_five_del

	echo

	if [ -z "$option_one_del" ] || [ $option_one_del = "done" ];
		then echo "0: option one not set, skipping.";
		else
			printf "${YELLOW}Removing user $option_one_del${NC}:"
			if(printf "${RED}`sudo userdel $option_one_del`${NC} \n"); then
				echo "OK."
			fi
	fi

	if [ -z "$option_two_del" ] || [ $option_two_del = "done" ];
		then echo "1: option two not set, skipping.";
		else 
			printf "${YELLOW}Removing user $option_two_del${NC}:"
			if(printf "${RED}`sudo userdel $option_two_del`${NC} \n"); then
				echo "OK."
			fi
	fi

	if [ -z "$option_three_del" ] || [ $option_three_del = "done" ];
		then echo "2: option three not set, skipping.";
		else
			printf "${YELLOW}Removing user $option_three_del${NC}:"
			if(printf "${RED}`sudo userdel $option_three_del`${NC} \n"); then
				echo "OK."
			fi
	fi

	if [ -z "$option_four_del" ] || [ $option_four_del = "done" ];
		then echo "3: option four not set, skipping.";
		else
			printf "${YELLOW}Removing user $option_four_del${NC}:"
			if(printf "${RED}`sudo userdel $option_four_del`${NC} \n"); then
				echo "OK"
			fi
	fi

	if [ -z "$option_five_del" ] || [ $option_five_del = "done" ];
		then echo "4: option five not set, skipping.";
		else
			printf "${YELLOW}Removing user $option_five_del${NC}:"
			if(printf "${RED}`sudo userdel $option_five_del`${NC} \n"); then
				echo "OK"
			fi
	fi


	echo
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Removed users via MANDY, entry \"removeuser\"." >> logs/log.txt
	echo "Commands Executed: sudo userdel USER_VAR" >> logs/log.txt
	echo >> logs/log.txt
}

