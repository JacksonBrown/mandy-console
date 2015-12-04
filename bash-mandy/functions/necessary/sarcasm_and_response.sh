#!/bin/bash

## SARCASM AND RESPONSE FUNCTION
sarcasm_and_response(){

	## BEGIN IF TESTS
	if [ "$option" = "mandy sucks" ]; then
		echo "you suck."
		echo
		sleep 3
		sl
		sleep 3
		exit

	elif [ "$option" = "fuck you" ] || [ "$option" = "fuck" ]; then
		echo "fuck you too fam."
		echo
		sleep 3
		sl
		sleep 3
		exit

	elif [ "$option" = "loser" ] || [ "$option" = "you're a loser" ] || [ "$option" = "ur a loser" ]; then
		echo "you're a loser too fam"
		echo

	elif [ "$option" = "skrillex" ]; then
		echo "BWOW WOW YOI YOI YOI YOI YOI YOI WAAAAA BWA BWA BWOW WOW Y-Y-Y-Y-Y-Y-Y-Y-Y-Y-Y-Y-Y-YAAAA"
		echo

	elif [ "$option" = "mlg" ] || [ "$option" = "mlgpro" ]; then
		echo
		printf "What have you done? \nWhy have you done? \nWhat unearthly hell have you summoned? \nJesus christ man \nJust get out of my swamp... \n"
		echo
		echo
		sudo apt-get install mplayer
		echo
		mplayer sounds/ayylmao.mp3
		echo

	elif [[ $option = you* ]]; then
		echo "you too pal"
		echo

	else

		echo "You're a $option"
		echo "Entry not found: returned to console." >> logs/log.txt
		echo >> logs/log.txt
		echo
	fi
}
