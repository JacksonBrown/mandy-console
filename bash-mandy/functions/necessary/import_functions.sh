#!/bin/bash

import_functions(){
	# IMPORTS

	## NECESSARY IMPORTS
	source functions/necessary/sarcasm_and_response.sh
	source functions/necessary/run_case.sh

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

	## EDIT LIGHTDM IMPORT
	source functions/edit_lightdm.sh

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

	## IMPORT EDIT SSHD_CONFIG FUNCTION
	source functions/edit_sshd.sh

	## IMPORT REMOVE READABLE HOME
	source functions/rm_readable_home.sh

	## IMPORT SCAN FUNCTION
	source functions/scan.sh

	## IMPORT TCP CAPTURE FUNCTION
	source functions/tcp_capture.sh

	## IMPORT HOW DO I FUNCTION
	source functions/howdoi.sh

	## IMPORT OPEN PAM FUNCTION
	source functions/open_pam.sh
}

