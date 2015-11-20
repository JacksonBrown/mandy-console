#!/bin/bash

# COLOR VARIABLES
RED='\033[0;31m'
NC='\033[0m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'

disable_ubuntu_guest(){
    printf "${YELLOW}Removing guest account for ubuntu${NC}: \n"

    if [ -e /usr/share/lightdm/lightd.conf.d/50-ubuntu.conf ]; then
        sudo echo "allow-guest=false" >> /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf
    fi


    if [ -e /usr/share/lightdm/lightdm.conf ]; then
        sudo echo "allow-guest=false" >> /usr/share/lightdm/lightdm.conf
    fi


    if [ -e /etc/lightdm/lightdm.conf ]; then
        sudo echo "allow-guest=false" >> /etc/lightdm/lightdm.conf
    fi

    #sudo gedit /etc/lightdm/lightdm.conf
    echo "OK."

    ## LOG UPDATER
    echo >> logs/log.txt
    echo "`date`" >> logs/log.txt
    echo "Removed guest account via MANDY, entry \"ubuntudisable\"." >> log.txt
    echo "Commands Executed: echo \"$allow-guest=false\" >> /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf" >> logs/log.txt
    echo "Commands Executed: echo \"$allow-guest=false\" >> /usr/share/lightdm/lightdm.conf" >> log.txt
    echo >> logs/log.txt
}

