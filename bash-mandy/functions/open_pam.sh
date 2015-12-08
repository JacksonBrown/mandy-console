
#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

open_pam(){
	printf "${YELLOW}Opening input pam file: \n1=common-auth, \n2=common-password, \n3=common-account${NC}"

	read option_pam

	if [[ $option_pam = 1 ]]; then
		gedit /etc/pam.d/common-auth
	elif [[ $option_pam = 2 ]]; then
		gedit /etc/pam.d/common-password
	elif [[ $option_pam = 3 ]]; then
		gedit /etc/pam.d/common-account
	else 
		echo "Invalid spefication, closing open_pam"
	fi
}









