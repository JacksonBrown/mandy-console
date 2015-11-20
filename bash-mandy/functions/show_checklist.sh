#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

show_checklist(){
	printf "${CYAN}Mark off on piece of paper as you go along (note this is not fully determined)${NC}: \n"
	echo
	echo
	printf "${RED}################ CHECKLIST ################${NC} \n"
	echo
	printf "${YELLOW}"
	echo 'User Policy - 2'
	echo
	echo 'Access Control and Settings - 1'
	echo
	echo 'Forensics Questions - 1'
	echo
	echo 'Insecure Services - 1'
	echo
	echo 'Malware - 1'
	echo
	echo 'Policty Violation: Files -1'
	echo
	echo 'Policy Violation: Software (not malware) - 1'
	echo
	printf "${NC}"
}