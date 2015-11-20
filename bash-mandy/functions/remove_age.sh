#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

## PROMPT FUNCTION WITH OPTION VARIABLES (READ)
prompt_age(){
	printf "${YELLOW}Enter users for chage (five entries total, type \"done\" if an entry is blank)${NC}: \n"
	read option_one_age
	read option_two_age
	read option_three_age
	read option_four_age
	read option_five_age

	echo
	echo
}

## CONDITIONAL TEST FUNCTION FOR OPTION VARIABLES
conditional_test_age(){
	if [ -z "$option_one_age" ] || [ $option_one_age = "done" ];
		then
		echo "option skipped.";
		else
		printf "${YELLOW}changing $option_one expiration${NC}: \n"
		if(printf "${RED}`sudo chage -M 30 $option_one_age`${NC}"); then
			echo "OK."
		fi
	fi

	if [ -z "$option_two_age" ] || [ $option_two_age = "done" ];
		then
		echo "option skipped.";
		else
		printf "${YELLOW}changing $option_two expiration${NC}: \n"
		if(printf "${RED}`sudo chage -M 30 $option_two_age`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_three_age" ] || [ $option_three_age = "done" ];
		then
		echo "option skipped.";
		else
		printf "${YELLOW}changing $option_three expiration${NC}: \n"
		if(printf "${RED}`sudo chage -M 30 $option_three_age`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_four_age" ] || [ $option_four_age = "done" ];
		then
		echo "option skipped.";
		else
		printf "${YELLOW}changing $option_four expiration${NC}: \n"
		if(printf "${RED}`sudo chage -M 30 $option_four_age`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	if [ -z "$option_five_age" ] || [ $option_five_age = "done" ];
		then
		echo "option skipped.";
		else
		printf "${YELLOW}changing $option_five expiration${NC}: \n"
		if(printf "${RED}`sudo chage -M 30 $option_five_age`${NC}"); then
			echo "OK."
		fi
		echo "OK.";
	fi

	echo
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Removed sudo users via MANDY, entry \"removeage\"." >> logs/log.txt
	echo "Commands Executed: sudo chage -M 40 USER_VAR" >> logs/log.txt
	echo >> logs/log.txt
}
