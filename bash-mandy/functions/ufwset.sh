#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

set_ufw_enable(){
	printf "${YELLOW}Enabling ufw firewall: ${NC} \n"

	if (printf "${RED}`sudo ufw enable`${NC} \n"); then
		echo "using version: "
		printf "${RED}`sudo ufw --version`${NC} \n"
		echo "OK."
	fi

	echo
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Enables and configures ufw firewall via MANDY, entry \"setufw\"." >> logs/log.txt
	echo "Commands Executed: sudo ufw enable" >> logs/log.txt
	echo "Commands Executed: sudo ufw default deny" >> logs/log.txt
	echo "Commands Executed: sudo ufw deny in http" >> logs/log.txt
	echo "Commands Executed: sudo ufw deny in smtp" >> logs/log.txt
	echo "Commands Executed: sudo ufw allow in 80" >> logs/log.txt
	echo "Commands Executed: sudo ufw allow in 22" >> logs/log.txt
	echo >> logs/log.txt
}

set_ufw_ruleset(){
	echo
	printf "${YELLOW}Setting default ruleset to deny: ${NC} \n"
	if (printf "${RED}`sudo ufw default deny`${NC} \n"); then
		echo "OK."
	fi
	echo
}

set_ufw_in(){
	echo

	echo "*******************************************"
	echo "Setting rules to accomidate default ruleset: "
	echo "*******************************************"

	echo

	printf "${YELLOW}Setting deny in HTTP: ${NC} \n"
	if (printf "${RED}`sudo ufw deny in http`${NC} \n"); then
		echo "OK."
	fi

	echo

	printf "${YELLOW}Setting deny in SMTP: ${NC} \n"
	if (printf "${RED}`sudo ufw deny in smtp`${NC} \n"); then
		echo "OK."
	fi
	echo
}

set_allow_port(){
	echo

	printf "${YELLOW}Allowing http acces in common port (80): ${NC} \n"
	if (printf "${RED}`sudo ufw allow in 80`${NC} \n"); then
		echo "OK."
	fi

	echo
	
	printf "${YELLOW}Allowing ssh acces in common port (20): ${NC} \n"
	if (printf "${RED}`sudo ufw allow in 22`${NC} \n"); then
		echo "OK."
	fi
}

# ONLY ADD THIS FUNCTION TO UNDO UFW SET UP NON MANUALLY
undo_setup(){
	echo

	echo "un-doing all functions"
	echo

	echo "Setting default ruleset to accept: "
	if (sudo ufw default allow); then
		echo "OK."
	fi
	echo

	echo "Un-doing ruleset accomidation: "
	echo
	echo "Setting accept in HTTP: "
	if (sudo ufw allow in http); then
		echo "OK."
	fi

	echo

	echo "Setting accept in SMTP: "
	if (sudo ufw allow in smtp); then
		echo "OK."
	fi
	echo

	echo "Disabling firewall: "
	if(sudo ufw disable); then
		echo "using version: "
		sudo ufw --version
		echo "OK."
	fi
	echo
}
