
#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

open_pam(){
	printf "${YELLOW}Opening input pam file: \n1=common-auth, \n2=common-password, \n3=common-account \nother=enter the specified name \n${NC}"

	read option_pam

	if [[ $option_pam = 1 ]]; then
		gedit /etc/pam.d/common-auth &
	elif [[ $option_pam = 2 ]]; then
		gedit /etc/pam.d/common-password &
	elif [[ $option_pam = 3 ]]; then
		gedit /etc/pam.d/common-account &
	elif [ "$option_pam" = "other" ]; then
		gedit /etc/pam.d/$option_pam &
	else 
		echo "Invalid spefication, closing open_pam"
	fi

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "View pam modules in MANDY, entry \"help\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}









