#!/bin/bash

FILE="/tmp/out.$$"
GREP="/bin/grep"

if [ "$(id -u)" != 0 ]; then
	echo
	echo "THIS MUST BE RUN AS ROOT!" 1>&2
	echo
	exit 1
else


# SET MANDY DIRECTORY VARIABLE/CHANGE DIRECTORY TO PARENT PATH
mandy_dir=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$mandy_dir"
chmod a+x *.sh
chmod a+x functions/*.sh


# IMPORTS
source functions/necessary/import_functions.sh
import_functions


# CLEARING SCREEN AND LOGS
clear
echo > $mandy_dir/logs/log.txt
echo > $mandy_dir/logs/show_directory_output.txt
echo > $mandy_dir/logs/log_mesg.txt
echo > $mandy_dir/logs/show_process.txt
echo > $mandy_dir/logs/scan_out.txt
echo > $mandy_dir/logs/cron_files.txt
echo "MANDY LOG MESSAGES: " >> $mandy_dir/logs/log.txt


## PROMPT CALL
prompt


while [ "$option" != "exit" ]; do
	# FUNCTION CALLING
	prompt2
	run_case
done


# LEAVING WITH EXIT 0 CODE
fi
exit 0
