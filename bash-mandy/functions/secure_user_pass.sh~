#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

## PROMPT FUNCTION WITH OPTION VARIABLES (READ)
prompt_pass(){
	printf "${YELLOW}Enter users for password change (five entries total, type \"done\" if an entry is blank)${NC}: \n"
	read option_one_pass
	read option_two_pass
	read option_three_pass
	read option_four_pass
	read option_five_pass
	echo
	echo
}

## CONDITIONAL TEST FUNCTION FOR OPTION VARIABLES
conditional_test_pass(){
	if [ -z "$option_one_pass" ] || [ $option_one_pass = "done" ];
		then
		echo "0: option skipped.";
		else
		printf "${YELLOW}changing $option_one_pass password${NC}: \n"
		if(printf "${RED}`sudo passwd $option_one_pass`${NC}"); then
			echo "OK."
		fi
	fi

	if [ -z "$option_two_pass" ] || [ $option_two_pass = "done" ];
		then
		echo "1: option skipped.";
		else
		printf "${YELLOW}changing $option_two_pass password${NC}: \n"
		if(printf "${RED}`sudo passwd $option_two_pass`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_three_pass" ] || [ $option_three_pass = "done" ];
		then
		echo "2: option skipped.";
		else
		printf "${YELLOW}changing $option_three_pass password${NC}: \n"
		if(printf "${RED}`sudo passwd $option_three_pass`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_four_pass" ] || [ $option_four_pass = "done" ];
		then
		echo "3: option skipped.";
		else
		printf "${YELLOW}changing $option_four_pass password${NC}: \n"
		if(printf "${RED}`sudo passwd $option_four_pass`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_five_pass" ] || [ $option_five_pass = "done" ];
		then
		echo "4: option skipped.";
		else
		printf "${YELLOW}changing $option_five_pass password${NC}: \n"
		if(printf "${RED}`sudo passwd $option_five_pass`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	echo
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Changed user passwords via MANDY, entry \"changepass\"." >> logs/log.txt
	echo "Commands Executed: sudo passwd USER_VAR" >> logs/log.txt
	echo >> logs/log.txt
}
