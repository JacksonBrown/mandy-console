#!/usr/bin/python

from os import system
import curses

def getParam(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def executeCmd(cmd_string):
	system("clear")
	run_var = system(cmd_string)
	print
	if run_var == 0:
		print "OK."
	else:
		print colored.red("Error: command executed in-properly")
	raw_input("press enter to continue...")

x = 0

while x != "4":
	screen = curses.initscr()

	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Please enter an option: ")
	screen.addstr(4, 4, "1 - Add a user")
	screen.addstr(5, 4, "2 - Restart Apache2")
	screen.addstr(6, 4, "3 - Show disk space")
	screen.addstr(7, 4, "4 - Exit")
	screen.refresh()

	x = screen.getch()

	if x == "1":
		username = getParam("Enter the username: ")
		homedir = getParam("Enter the home directory: ")
		groups = getParam("Enter comma-sparated groups: ")
		shell = getParam("Enter the shell: ")
		curses.endwin()
		executeCmd("echo " + usernamae + "echo " + homedir + "echo " + groups + "echo " + shell)
	if x == "2":
		curses.endwin()
		executeCmd("sudo service apache2 restart")
	if x == "3":
		curses.endwin()
		executeCmd("df -h")

curses.endwin()	
