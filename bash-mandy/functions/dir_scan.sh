#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


# SCAN DICTIONARY FUNCTION
array_scan(){
	echo "Enter a directory to be scanned: "
	read scanned_dir
	# ARRAY DICTIONARY/SCANNED FILE NAMES
	list_arr=("passwords" "bank" "pass" "credit" "cards" 
	"accounts" "Passwords" "creditcards" "creditcardinfo" "bankpasswords" "keylog" 
	"keylogger" "rootkit" "usernames" "users" "secret" "userinfo")
	
	echo "Searching input directory for dictionary file titles: "
	echo
	for i in "${list_arr[@]}"; do
		if [ ! -d $scanned_dir ]; then
			echo "The directory you entered is invalid."
			break
		fi
		# SEARCH FOR REGULAR FILES
		if [ -e $scanned_dir/$i\.* ]; then
			printf "${YELLOW}$i${NC}: ${RED}FOUND${NC} \n"
		fi

		if [ ! -e $scanned_dir/$i\.* ]; then
			printf "${YELLOW}$i${NC}: ${GREEN}CLEAR${NC} \n"
		fi
	done
	echo
}


# SCAN FOR EXECUTABLE FILES
executable_scan(){
	# FIND EXECUTABLE FILES
	echo "Finding executable files in directory: "
	if (printf "${RED}`find $scanned_dir \( -type d ! -name . -prune \) -o \( -executable -type f \)`${NC} \n"); then
		echo "OK."
	fi
	echo
}


# SCAN FOR PRIVATE/HIDDEN FILES
private_scan(){
	# FIND PRIVATE/HIDDEN FILES
	echo "Finding hidden files in directory: "
	if (printf "${RED}`find $scanned_dir -name ".*" -ls`${NC} \n"); then
		echo "OK."
	fi
	echo
}

## RUN ARR SCAN
array_scan

## RUN EXEC SCAN
executable_scan

## RUN HIDDEN SCAN
private_scan

