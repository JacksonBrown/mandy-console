#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


## PROMPT FUNCTION WITH OPTION VARIABLES (READ)
prompt_group(){
	printf "${YELLOW}Enter users for sudo group remove (five entries total, type \"done\" if an entry is blank)${NC}: \n"
	read option_one_group
	read option_two_group
	read option_three_group
	read option_four_group
	read option_five_group
	echo
	echo
}

## CONDITIONAL TEST FUNCTION FOR OPTION VARIABLES
conditional_test_group(){
	if [ -z "$option_one_group" ] || [ $option_one_group = "done" ];
		then
		echo "0: option skipped.";
		else
		printf "${YELLOW}Removing $option_one_group from sudo${NC}: \n"
		if(printf "${RED}`sudo deluser $option_one_group sudo`${NC} \n"); then
			echo "OK."
			echo
		fi
	fi

	if [ -z "$option_two_group" ] || [ $option_two_group = "done" ];
		then
		echo "1: option skipped.";
		else
		printf "${YELLOW}Removing $option_two_group from sudo${NC}: \n"
		if(printf "${RED}`sudo deluser $option_two_group sudo`${NC} \n"); then
			echo "OK."
			echo
		fi
	fi

	if [ -z "$option_three_group" ] || [ $option_three_group = "done" ];
		then
		echo "2: option skipped.";
		else
		printf "${YELLOW}Removing $option_three_group from sudo${NC}: \n"
		if(printf "${RED}`sudo deluser $option_three_group sudo`${NC} \n"); then
			echo "OK."
			echo
		fi
	fi

	if [ -z "$option_four_group" ] || [ $option_four_group = "done" ];
		then
		echo "3: option skipped.";
		else
		printf "${YELLOW}Removing $option_four_group from sudo${NC}: \n"
		if(printf "${RED}`sudo deluser $option_four_group sudo`${NC} \n"); then
			echo "OK."
			echo
		fi
	fi

	if [ -z "$option_five_group" ] || [ $option_five_group = "done" ];
		then
		echo "4: option skipped.";
		else
		printf "${YELLOW}Removing $option_five_group from sudo${NC}: \n"
		if(printf "${RED}`sudo deluser $option_five_group sudo`${NC} \n"); then
			echo "OK."
			echo
		fi
	fi

	echo
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Removed sudo users via MANDY, entry \"editsudoremove\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: sudo deluser OPTION_VAR sudo" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt

}
