#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

## OUTPUT THE COMMAND
show_dir(){
	printf "${YELLOW}Enter a directory${NC}: \n"
	read x

	printf "${YELLOW}Listing all list of directory${NC}: \n"
	printf "`ls -a $x` \n"
	# COMMENTED OUT, ABOVE IS MORE EFFICIENT
	#for i in `ls -a $x`; do
	#	printf "${RED}$i${NC} \n"
	#done
	echo

	printf "${YELLOW}Listing long list of directory${NC}: \n"
	printf "`ls -l $x` \n"
	echo

	## LOG UPDATER
	echo >> logs/log.txt
	echo "`date`" >> logs/log.txt
	echo "List all \"long\" and \"all\" list of a directory via MANDY, entry \"directory\"." >> logs/log.txt
	echo "Commands Executed: ls -a entry_var; ls -l entry_var;" >> logs/log.txt
	echo >> logs/log.txt
}

## IF THE WC IS GREATER THAN 100 OUTPUT TO FILE.TXT
line_count_condition(){
	counter_a="`ls -a $x | wc -l`"
	counter_l="`ls -l $x | wc -l`"
	counter_c=$((counter_a+counter_l))

	if [ $counter_c -ge 50 ]; then
		printf "${YELLOW}Output greater than or equal to 50 lines, output will also be in show_directory_output.txt in the logs folder${NC}: \n"
		echo > logs/show_directory_output.txt
		echo "ALL LIST OF DIRECTORY: " >> logs/show_directory_output.txt
		echo "`ls -a $x`" >> logs/show_directory_output.txt
		echo >> logs/show_directory_output.txt

		echo "LONG LIST OF DIRECTORY: " >> logs/show_directory_output.txt
		echo "`ls -l $x`" >> logs/show_directory_output.txt
		echo >> logs/show_directory_output.txt

		printf "${YELLOW}View the file now (y/n)?${NC} \n"
		read read_file
		if [ $read_file = "y" ]; then 
			gedit logs/show_directory_output.txt
		else
			echo "OK."
		fi

	fi
}
