#!/bin/bash

## LOCKING ROOT USER PASSWORD
lock_root_user(){
	echo "Enter new root user password: "
	if(sudo passwd root); then
		echo
		echo "Locking root user password: "
		if (sudo passwd -l root); then
			echo "OK."
			echo
		fi
	fi
}

lock_root_user
