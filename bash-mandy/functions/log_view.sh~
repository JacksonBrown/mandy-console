#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

log_view(){

	printf "${YELLOW}Listing log messages, exporting to file \"log_mesg.txt\": \n"
	echo
	echo > logs/log_mesg.txt
	# GENERAL LOG MESSAGES
	printf "${YELLOW}Tail of general log messages${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/messages`${NC} \n"); then
			echo "GENERAL LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/messages`" >> logs/log_mesg.txt
			echo >> logs/log_mesg.txt
		fi

	echo

	# BOOT LOG MESSAGES
	printf "${YELLOW}Tail of boot log messages${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/boot`${NC} \n"); then
			echo "BOOT LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/boot`" >> logs/log_mesg.txt
			echo log_mesg.txt
		fi

	echo

	# DEBUG LOG MESSAGES
	printf "${YELLOW}Tail of debug log messages${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/debug`${NC} \n"); then
			echo "DEBUG LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/debug`" >> logs/log_mesg.txt
			echo >> logs/log_mesg.txt
		fi

	echo

	# USER LOGIN AUTHENTICATION MESSAGES
	printf "${YELLOW}Tail of auth log messages (user login/authentication)${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/auth.log`${NC} \n"); then
			echo "AUTH LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/auth.log`" >> logs/log_mesg.txt
			echo >> logs/log_mesg.txt
		fi

	echo

        # DAEMON LOG MESSAGES
	printf "${YELLOW}Tail of daemon log messages${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/daemon.log`${NC} \n"); then
			echo "DAEMON LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/daemon.log`" >> logs/log_mesg.txt
			echo >> logs/log_mesg.txt
		fi

	echo

	# KERNEL LOG MESSAGES
	printf "${YELLOW}Tail of kernel log messages${NC}: \n"
		if (printf "${RED}`sudo tail -n 10 /var/log/kern.log`${NC} \n"); then
			echo "KERNEL LOG MESSAGES: " >> logs/log_mesg.txt
			echo "`sudo cat /var/log/kern.log`" >> logs/log_mesg.txt
			echo >> logs/log_mesg.txt
		fi

	echo

	printf "${YELLOW}View the file \"log_mesg.txt\" file now (y/n)?${NC} \n"
	read option_log_mesg
	if [ $option_log_mesg = "y" ]; then
		gedit logs/log_mesg.txt
	else
		echo "OK."
	fi

	## LOG UPDATE
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "Viewed log files via MANDY, entry \"logsee\"." >> logs/log.txt
	echo "Commands Executed: cat/var/LOG_VAR" >> logs/log.txt
	echo >> logs/log.txt

}

