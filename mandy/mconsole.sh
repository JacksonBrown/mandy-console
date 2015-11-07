#!/bin/bash

# SET MANDY DIRECTORY VARIABLE/CHANGE DIRECTORY TO PARENT PATH
mandy_dir=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$mandy_dir"

chmod a+x *.sh
chmod a+x functions/*.sh

# IMPORTS

## PROMPT IMPORT
source functions/prompt.sh

## SHOW DIRECTORY IMPORT
source functions/show_dir.sh

## SHOW BIN FILES IMPORT
source functions/show_bin.sh

## SHOW REPOSITORIES IMPORT
source functions/show_repositories.sh

## SHOW SYSTEM INFO IMPORT
source functions/show_sys_info.sh

## SHOW HELP IMPORT
source functions/help.sh

## SHOW USERS IMPORT
source functions/show_users.sh

## SHOW NETWORK INTERFACE IMPORT
source functions/net_interface.sh

## SHOW FREE RAM IMPORT
source functions/show_free.sh

## SHOW PCI BUS CONNECTIONS IMPORT
source functions/show_pci.sh

## SHOW BLOCK DEVICES IMPORT
source functions/show_blk.sh

## SHOW DISK SPACE IMPORT
source functions/show_space.sh

## SHOW OPEN PORTS IMPORT
source functions/show_open_ports.sh

## DISABLE UBUNTU GUEST IMPORT
source functions/disable_ubuntu_guest.sh

## UPDATE SYSTEM IMPORT
source functions/updateme.sh

## DELETE USERS IMPORT
source functions/userdelete.sh

## SET UFW FIREWALL IMPORT
source functions/ufwset.sh

## REMOVE/REPLACE USER CHAGE IMPORT
source functions/remove_age.sh

## EDIT SUDOERS IMPORT
source functions/edit_sudoers.sh

## SHOW GROUP USERS IMPORT
source functions/show_group_users.sh

## CHANGE USER PASS FUNCTION IMPORT
source functions/secure_user_pass.sh

## IMPORT LOG VIEW FUNCTION
source functions/log_view.sh

## IMPORT SUDO GROUP REMOVE 
source functions/remove_sudo_group_users.sh

## IMPORT DIRECTORY REMOVE
source functions/dir_delete.sh

## IMPORT CRON VIEWER
source functions/show_cron.sh

## IMPORT SERVICE EDIT
source functions/edit_service.sh

## IMPORT SHOW PROCESS FUNCTION
source functions/show_process.sh

## IMPORT SHOW SERVICES RUNNING
source functions/show_services.sh

## IMPORT CHECKLIST SHOW
source functions/show_checklist.sh

## IMPORT SHOW SHELLS FUNCTION
source functions/show_shells.sh

# SETTING NECESSARY ALIASES
#alias cdm="cd"
#shopt -s expand_aliases

clear
echo > $mandy_dir/logs/log.txt
echo > $mandy_dir/logs/show_directory_output.txt
echo > $mandy_dir/logs/log_mesg.txt
echo > $mandy_dir/logs/show_process.txt

echo "MANDY LOG MESSAGES: " >> $mandy_dir/logs/log.txt

## PROMPT CALL
prompt


# FUNCTIONS

## WHILE LOOP TO END MANDY
while [ "$option" != "exit" ]; do

## RUN CASE FUNCTION
run_case(){

	## CREATE CASE FOR $OPTION
	case $option in
		"help")
			help_info
			;;
		"show")
			show_sys_info
			;;
		"users")
			show_users
			;;
		"network")
			net_interface
			;;
		"bin")
			show_bin
			;;
		"space")
			show_space
			;;
		"repo")
			show_repositories
			;;
		"directory")
			show_dir
			line_count_condition
			;;
		"ram")
			show_free
			;;
		"pci")
			show_pci
			;;
		"block")
			show_blk
			;;
		"ports")
			show_open_ports
			;;
		"setufw")
			set_ufw_enable
			set_ufw_ruleset
			set_ufw_in
			set_allow_port
			;;
		"update")
			update_sys
			;;
		"removeuser")
			delete_user
			;;
		"removeage")
			prompt_age
			conditional_test_age
			;;
		"editsudo")
			edit_sudoers
			;;
		"groupsee")
			prompt_show_group_users
			show_group_users
			;;
		"changepass")
			prompt_pass
			conditional_test_pass
			;;
		"editsudoremove")
			prompt_group
			conditional_test_group
			;;
		"logsee")
			log_view
			;;
		"deldir")
			dir_delete
			;;
		"cron")
			show_cron
			;;
		"editservice")
			edit_service
			;;
		"process")
			show_process
			;;
		"services")
			show_services
			;;

		"checklist")
			show_checklist
			;;
		"shells")
			show_shells
			;;
		*)
			if [ "$option" == "exit" ]; then
				echo "Exiting Mandy"
				echo
				else
				echo >> logs/log.txt
				echo "Entry not found: returned to console."
				echo "Entry not found: returned to console." >> logs/log.txt
				echo >> logs/log.txt
				echo
			fi
			;;
		esac
		## END CASE
}

add_common_cmd(){
	case $option in
		"clear")
			clear
			;;
		"ls")
			ls
			echo
		;;
		"pwd")
			pwd
			echo
		;;
		"mandyhistory")
			cat logs/log.txt
			echo
		;;
	esac
}


# FUNCTION CALLING

## CALL PRINT FUNCTION
#print

## CALL SECONDARY PROMPT FUNCTION
prompt2

## CALL RUN_CASE/ADD_COMMON_CMD FUNCTIONS
run_case
#add_common_cmd

# ENDING LOOP
done

# LEAVING WITH EXIT 0 CODE
exit 0
