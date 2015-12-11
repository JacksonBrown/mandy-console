#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'


source ../mconsole.sh


# SCAN SOFTWARE FUNCTION
software_scan(){
	echo
	echo "SCANNING SOFTWARE FOR FOLLOWING PROGRAMS: "
	printf "${RED}"
	echo "hydra"
	echo "john the ripper"
	echo "nmap"
	echo "wireshark"
	echo "aircrack"
	echo "sqlmap"
	echo "metasploit"
	echo "netcat"
	echo
	printf "${NC}"
	echo "RUNNING TEST: "
	printf "${YELLOW}searching for hydra${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"hydra\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for john the ripper${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"john\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for nmap${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"nmap\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for wireshark${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"wireshark\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for aircrack${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"aircrack-ng\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${LOW}searching for sqlmap${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"sqlmap\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for metasploit${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"metasploit\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for netcat-traditional${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"netcat-traditional\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for netcat-openbsd${NC}: \n"
	if(printf "${RED}** `dpkg -l | grep \"netcat-openbsd\"`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	printf "${YELLOW}searching for nc${NC}: \n"
	if(printf "${RED}** `ls /usr/bin/nc`${NC} \n"); then
		printf "${CYAN}OK. ${NC}"
		echo
	fi

	echo
	echo "DONE."
	echo

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Scanned for prohibited software in MANDY, entry \"help\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: dpkg -l, ls, grep" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}

