#!/bin/bash

inter_change(){
    echo
    echo "Installing gnome-fallback interface."
    echo
    if (sudo apt-get install gnome-session-fallback); then
	echo "OK."
    fi
}

inter_change
