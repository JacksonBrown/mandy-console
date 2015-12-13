
#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

source ../mconsole.sh

replace_pam_files(){
	echo "Would you like to replace the common-password file?y/n"
	read option_yes
	if [ "$option_yes" = "y" ]; then
		if (sudo cp $mandy_dir/misc/common-password /etc/pam.d/); then
			echo "OK."
		fi
			
		echo "Would you like to replace the login.def file?y/n"
		read option_yes_2
		if [ "$option_yes_2" = "y" ]; then
			if (sudo cp $mandy_dir/misc/login.defs /etc/); then
				echo "OK."
			fi
		fi
			
	fi

	## LOG UPDATER
	echo >> $mandy_dir/logs/log.txt
	echo "`date`" >> $mandy_dir/logs/log.txt
	echo "Replace pam files via MANDY, entry \"replacepam\"." >> $mandy_dir/logs/log.txt
	echo "Commands Executed: cp" >> $mandy_dir/logs/log.txt
	echo >> $mandy_dir/logs/log.txt
}






















