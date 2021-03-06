#!/bin/bash

# VARIABLES
RED='\033[0;31m'
NOCOL='\033[0m'
CYAN='\033[0;36m'


source ../mconsole.sh


# FUNCTIONS

## PROMPT WITH READ NETWORK VAR
scan_prompt(){
	cat logos/logo_scan
	echo "Enter network (or type \"help\" for a tutorial): "
	read network
	echo > logs/scan_out.txt
}

## RUN NMAP SCAN ON NETWORK VAR
nmap_scan(){

	
	if [ $network = "help" ]; then
		echo "enter the address of a network you would like to scan."
		echo
	else


		echo
		echo "Initializing full scan"
		echo "All scan info will be directed to \"logs/scan_out.txt\" "
		printf "${RED}EVERYTIME YOU RUN FULL SCAN \"logs/scan_out.txt\" IS OVER WRITTEN${NOCOL} \n"
		echo "This may take several minutes"
		echo
		printf "${CYAN}BEGINNING NMAP SCAN ${NOCOL} \n"
		echo "######################"
		echo "BEGINNING NMAP SCAN" >> logs/scan_out.txt
		echo >> logs/scan_out.txt
		echo "######################" >> logs/scan_out.txt
		echo

		printf "${CYAN}Operating System Scan: ${NOCOL} \n"
		printf "__OPERATING SYSTEM SCAN__ \n" >> logs/scan_out.txt
		if(nmap -A $network | tee >> logs/scan_out.txt);
			then
				echo >> logs/scan_out.txt
				echo "######################" >> logs/scan_out.txt
				#echo >> logs/scan_out.txt
				echo "OK.";
			else
				printf "${RED}Scan failed${NOCOL} \n";
		fi
		echo
		echo

		printf "${CYAN}Probe Scan: ${NOCOL} \n"
		echo "__PROBE SCAN__" >> logs/scan_out.txt
		if(nmap -sV $network | tee >> logs/scan_out.txt);
			then
				echo >> logs/scan_out.txt
				echo "######################" >> logs/scan_out.txt
				#echo >> logs/scan_out.txt
				echo "OK.";
			else
				printf "${RED}Scan failed${NOCOL} \n";
		fi
		echo
		echo

		printf "${CYAN}Verbose Scan: ${NOCOL} \n"
		echo "__VERBOSE SCAN__" >> logs/scan_out.txt
		if(nmap -v $network | tee >> logs/scan_out.txt);
			then
				echo >> logs/scan_out.txt
				echo "######################" >> logs/scan_out.txt
				#echo >> logs/scan_out.txt
				echo "OK.";
			else
				printf "${RED}Scan failed${NOCOL} \n";
		fi
		echo
		echo
	
		printf "${CYAN}IPV6 Scan: ${NOCOL} \n"
		echo "__IPV6 SCAN__" >> logs/scan_out.txt
		if(nmap -6 $network | tee >> logs/scan_out.txt);
			then
				echo >> logs/scan_out.txt
				echo "######################" >> logs/scan_out.txt
				#echo >> logs/scan_out.txt
				echo "OK.";
			else
				printf "${RED}Scan failed${NOCOL} \n";
		fi
		echo
		echo

		echo "All scans complete "
		echo "Output of scans has been sent to \"logs/scan_out.txt\" "
		echo

		## LOG UPDATER
		echo >> $mandy_dir/logs/log.txt
		echo "`date`" >> $mandy_dir/logs/log.txt
		echo "Scanned input network via MANDY, entry \"removeage\"." >> $mandy_dir/logs/log.txt
		echo "Commands Executed: sudo nmap -OPT -HOST" >> $mandy_dir/logs/log.txt
	fi
}
