#!/usr/bin/python

import curses

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(0, 0, "Mandy Console")
myscreen.refresh()
myscreen.getch()

curses.endwin()
