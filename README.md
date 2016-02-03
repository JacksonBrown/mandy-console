#Mandy Console

Nothing special.
For Mason, our dearest love, and dank meme expert.

NOTE:
Bash version is being halted.


# Currently In Development
*compatibility for Red Hat, SUSE, and other Systems*

*Clean up the bash version's code and output*

*Add more usable options*

*Create user interface mode*


#Description

The Mandy Console is an all purpose console made as a control panel and productivity enhancer for the Linux command line. The Mandy Console comes with a growing variety of options (which can be viewed with “help”). All of the options so far have been programmed to further enhance the productivity of the Linux Administrator. Every option within the Mandy Console will be useful in Linux System Administration.


# Install
1.) Download

2.) `sudo apt-get install python-pip`

3.) `sudo pip install clint`

#Usage

BASH VERSION:
`sudo bash mconsole.sh` OR `sudo bash /path/to/mconsole.sh`

PYTHON VERSION:
`sudo python MandyMain.py` OR `sudo python /path/to/MandyMain.py`

#Help Display

Command            | Description
------------       | ------------
help    	   | Displays this
users		   | Displays the system users
network		   | reads the /etc/network/interfaces file
bin		   | shows contents of bin directories
repo		   | show the repositories in aptitude
directory	   | display input directory
pci		   | show all devices connected via pci
ram		   | show all fre ram in the system
block		   | show all block devices connected to the system
exit		   | exit mandy console
ports 		   | show all open ports
setufw		   | sets up the ufw firewall to configuration
removeuser	   | removes the specified 5 users
removeage	   | removes and replaces the chage of 5 users
space		   | show free disk space in the system
groupsee 	   | view all of the suers in a specified group
changepass	   | change pasword of specified 5 users
editsudoremove	   | remove specified 5 users from the sudo group
logsee		   | view the tail of input log files
deldir		   | delete a input directory
editservice	   | delete a input directory
process		   | show processes on the system
services	   | show services running on the system 
shells		   | show shells on the system
editssh		   | edit the sshd config file
editlightdm	   | edit lightdm configuration files
removereadablehome | remove world readable permissions on home directories
dumptcp		   | view tcp packets in new window
howdoi		   | opens google in firefox web browser
openpam		   | views the chosen pam file
softwarescan	   | scans for basic hacking tools


