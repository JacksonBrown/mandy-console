#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

# CREATE UPDATE SYSTEM FUNCTION
update_sys(){
	printf "${CYAN}The updates will automatically be installed, continue (y/n)?${NC} \n"
	read option_update
	echo
	printf "${CYAN}Fedora or Debian distro (1/2)?${NC} \n"
	read option_fod
	echo
	if [ $option_update = "y" ]; then


		# BEGIN IF TEST DEBIAN
		if [ $option_fod = "2" ]; then
			printf "${YELLOW}Running update: \n"

			if (printf "${RED}`sudo apt-get --yes --force-yes update`${NC} \n");
				echo
				printf "${YELLOW}Running upgrade: \n"
				then 
					printf "${RED}"
						sudo apt-get --yes --force-yes upgrade
					printf "${NC} \n";
			fi
		# END IF TEST DEBIAN


		# BEGIN IF TEST FEDORA
		elif [ $option_fod = "1" ]; then	
			printf "${YELLOW}Running update: \n"

			if (printf "${RED}`sudo yum -y update`${NC} \n");
				echo
				printf "${YELLOW}Running update${NC}: \n"
			fi
		fi
		# END IF TEST FEDORA


	# BEGIN ERROR REPORTING
	else
		printf "${YELLOW}Option other than \"y\" specified, update cancelled${NC}. \n"
	fi
	# END ERROR REPORTING
	# END IF TEST READ_OPTION

	# OPEN UPDATE MANAGER
	printf "${YELLOW}Opening update manager${NC}. \n"
	if (update-manager); then
		echo "OK."
	fi

	##LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Updates the system via MANDY, entry \"update\"." >> logs/log.txt
	echo "Commands Executed: sudo apt-get --yes --force-yes update" >> logs/log.txt
	echo "Commands Executed: sudo apt-get --yes --force-yes upgrade" >> logs/log.txt
	echo >> logs/log.txt
}
