#!/bin/bash

# VARIABLES
RED='\033[0;31m'
NOCOL='\033[0m'
CYAN='\033[0;36m'


# FUNCTIONS

## PROMPT WITH READ NETWORK VAR
prompt(){
	clear
	cat logo.txt
	echo "Powered by Nmap"
	echo "A script that runs miltiple scan services on a host"
	echo "Enter network: "
	read network
	echo > scan_out.txt
}

## RUN NMAP SCAN ON NETWORK VAR
nmap_scan(){
	echo
	echo "Initializing full scan"
	echo "All scan info will be directed to \"scan_out.txt\" "
	printf "${RED}EVERYTIME YOU RUN FULL SCAN \"scan_out.txt\" IS OVER WRITTEN${NOCOL} \n"
	echo "This may take several minutes"
	echo
	printf "${CYAN}BEGINNING NMAP SCAN ${NOCOL} \n"
	echo "######################"
	echo "BEGINNING NMAP SCAN" >> scan_out.txt
	echo >> scan_out.txt
	echo "######################" >> scan_out.txt
	echo

	printf "${CYAN}Operating System Scan: ${NOCOL} \n"
	printf "__OPERATING SYSTEM SCAN__ \n" >> scan_out.txt
	if(nmap -A $network | tee >> scan_out.txt);
		then
			echo >> scan_out.txt
			echo "######################" >> scan_out.txt
			#echo >> scan_out.txt
			echo "OK.";
		else
			printf "${RED}Scan failed${NOCOL} \n";
	fi
	echo
	echo

	printf "${CYAN}Probe Scan: ${NOCOL} \n"
	echo "__PROBE SCAN__" >> scan_out.txt
	if(nmap -sV $network | tee >> scan_out.txt);
		then
			echo >> scan_out.txt
			echo "######################" >> scan_out.txt
			#echo >> scan_out.txt
			echo "OK.";
		else
			printf "${RED}Scan failed${NOCOL} \n";
	fi
	echo
	echo

	printf "${CYAN}Verbose Scan: ${NOCOL} \n"
	echo "__VERBOSE SCAN__" >> scan_out.txt
	if(nmap -v $network | tee >> scan_out.txt);
		then
			echo >> scan_out.txt
			echo "######################" >> scan_out.txt
			#echo >> scan_out.txt
			echo "OK.";
		else
			printf "${RED}Scan failed${NOCOL} \n";
	fi
	echo
	echo
	
	printf "${CYAN}IPV6 Scan: ${NOCOL} \n"
	echo "__IPV6 SCAN__" >> scan_out.txt
	if(nmap -6 $network | tee >> scan_out.txt);
		then
			echo >> scan_out.txt
			echo "######################" >> scan_out.txt
			#echo >> scan_out.txt
			echo "OK.";
		else
			printf "${RED}Scan failed${NOCOL} \n";
	fi
	echo
	echo

	echo "All scans complete "
	echo "Output of scans has been sent to \"scan_out.txt\" "
	echo
}


prompt
nmap_scan
