#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

# FUNCTIONS FOR PROMPT
prompt(){
	echo
	cat logos/logo
	echo
	echo "Welcome to the Mandy console "
	echo "type \"help\" for options."
	echo
	echo "COLOR CODING: "
	printf "${GREEN}Green${NC}: Command input \n"
	printf "${RED}Red${NC}: Output of a command being run or by Mandy console \n"
	printf "${CYAN}Cyan${NC}: Information from devs \n"
	printf "${YELLOW}Yellow${NC}: Actions being commited by/info needed by Mandy console \n"
	echo
}

prompt2(){
	#echo -ne
	printf "${GREEN}`pwd`>${NC} "
	read option
	echo
}
