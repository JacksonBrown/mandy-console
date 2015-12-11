#!/bin/bash

source ../../mconsole.sh

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
		"editssh")
			edit_sshd
			;;
		"clear")
			clear
			;;
		"mandyhistory")
			cat $mandy_dir/logs/log.txt
			echo
		;;
		"editlightdm")
			edit_lightdm
			;;
		"removereadablehome")
			rm_readable_home_dir
			;;
		"scan")
			scan_prompt
			nmap_scan
			;;
		"top")
			top
			;;
		"dumptcp")
			tcp_capture
			;;
		"howdoi")
			howdoi
			;;
		"openpam")
			open_pam
			;;
		"softwarescan")
			software_scan
			;;
		ping*)
			$option
			echo
			;;
		ls*)
			$option
			echo
			;;
		pwd*)
			$option
			echo
			;;
		cd*)
			$option
			echo
			;;
		rm*)
			$option
			echo
			;;
		cat*)
			$option
			echo
			;;
		gedit*)
			$option
			echo
			;;
		sudo*)
			$option
			echo
			;;
		*)
			if [ "$option" == "exit" ]; then
				echo "Exiting Mandy"
				echo
			else
				echo >> logs/log.txt
				sarcasm_and_response
			fi
			;;
		esac
		## END CASE
}

