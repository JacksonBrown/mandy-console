
#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

open_pam(){
	printf "${YELLOW}Opening input pam file: \n1=common-auth, \n2=common-password, \n3=common-account, \nother=enter the specified name \n${NC}"

	read option_pam

	## ELIF OPT 1
	if [[ $option_pam = 1 ]]; then
		gedit /etc/pam.d/common-auth &

	## ELIF OPT 2
	elif [[ $option_pam = 2 ]]; then
		gedit /etc/pam.d/common-password &

	## ELIF OPT 3
	elif [[ $option_pam = 3 ]]; then
		gedit /etc/pam.d/common-account &

	## ELIF OTHER
	elif [ "$option_pam" = "other" ]; then
		printf "${YELLOW}Enter the specified pam file name${NC}: \n"
		read pam_spec_option

		if (gedit /etc/pam.d/$pam_spec_option &); then
			echo "OK."
		fi


	else 
		echo "Invalid spefication, closing open_pam"
	fi

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "View pam files via MANDY, entry \"openpam\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cat" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}

