#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

edit_service(){
	printf "${YELLOW}Enter service to be configured${NC}: \n"
	read service_option_one
	printf "${YELLOW}Enter action to take on $service_option_one ${NC}: \n"
	read service_option_two

	if [ $service_option_one = "apache2" ]; then
		case $service_option_two in
			"restart")
				if(printf "${RED}`sudo service apache2 restart`${NC} \n"); then
					echo "OK."
				fi
				;;
			"start")
				if(printf "${RED}`sudo service apache2 start`${NC} \n"); then
					echo "OK."
				fi
				;;
			"stop")
				if(printf "${RED}`sudo service apache2 stop`${NC} \n"); then
					echo "OK."
				fi
				;;
		esac
	fi

	if [ $service_option_one = "mysql" ]; then
		case $service_option_two in
			"restart")
				if(printf "${RED}`sudo service mysql restart`${NC} \n"); then
					echo "OK."
				fi
				;;
			"start")
				if(printf "${RED}`sudo service mysql start`${NC} \n"); then
					echo "OK."
				fi
				;;
			"stop")
				if(printf "${RED}`sudo service mysql stop`${NC} \n"); then
					echo "OK."
				fi
				;;
		esac
	fi

	if [ $service_option_one = "vsftpd" ]; then
		case $service_option_two in
			"restart")
				if(printf "${RED}`sudo service vsftpd restart`${NC} \n"); then
					echo "OK."
				fi
				;;
			"start")
				if(printf "${RED}`sudo service vsftpd start`${NC} \n"); then
					echo "OK."
				fi
				;;
			"stop")
				if(printf "${RED}`sudo service vsftpd stop`${NC} \n"); then
					echo "OK."
				fi
				;;
		esac
	fi

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Configrue services via MANDY, entry \"editservice\"." >> logs/log.txt
	echo "Commands Executed: sudo service SERVICE_VAR SERVICE_VAR_OPTION" >> logs/log.txt
	echo >> logs/log.txt
}
