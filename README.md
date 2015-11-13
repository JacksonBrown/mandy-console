#Mandy Console

Made by Jackson Brown, Blake Holloway 

Last Update: September, 27, 2015

for Mason, our dearest love


#DESCRIPTION

The Mandy Console is an all purpose console made as a control panel and productivity enhancer for the Linux command line. The Mandy Console comes with a growing variety of options (which can be viewed with “help”). All of the options so far have been programmed to further enhance the productivity of the Linux Administrator. Every option within the Mandy Console will be useful in Linux System Administration.


#USAGE

sudo bash mconsole.sh 
OR 
sudo bash /path/to/mconsole.sh


#Help Display

show: displays the system info 

users: displays the system users 

network: reads the /etc/network/interfaces file

bin: show the bin directory 

repo: show the repositories in aptitude 

directory: display a input directory 

pci: show all devices connected via PCI bus 

ram: show all free ram in the system 

block: show all block devices connected to the system 

exit: exits Mandy Console 

ports: show all open ports 

setufw: sets up the ufw firewall to configuration 

update: updates the system 

removeuser: removes the specified 5 users 

removeage: removes and replaces the chage of 5 users 

space: show free disk space in the system 

editsudo: edits the /etc/sudoers file 

groupsee: view all of the users in a specified group 

changepass: change password of specified 5 users 

editsudoremove: remove specified 5 users from the sudo group 

logsee: view the tail of log files and creat log_mesg.txt 

deldir: delete a input directory 

cron: view all the cron files in /etc/ 

# Full Scan

a scan bash script that runs on an input network. powered my Nmap and other scan services. 
