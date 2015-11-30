#!/usr/bin/python

# IMPORTS
import curses
import os

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	os.system("clear")
	cmd_run = os.system(cmd_string)
	print " ## "
	if cmd_run == 0:
		print "Exit code: 0"
	else:
		print "Exit code: ERROR"
	raw_input("press enter")
	print " ## "

x = 0

while x!= ord(`4`):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Please Enter an option")
	screen.addstr(4, 4, "1 - Add User")
	screen.addstr(4, 4, "2 - Restart Apache")
	screen.addstr(4, 4, "1 - Show Disk Space")
	screen.addstr(4, 4, "1 - Exit")

	x = screen.getch()

	if x == ord(`1`):
		print "okey."
	elif x == ord(`2`):
		print "K."
	elif x == ord(`3`)
		print "Ight."

curses.endwin()
