#/bin/env python3

# source
# https://docs.python.org/3/howto/curses.html

import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    begin_y = 7
    begin_x = 20
    height = 5
    width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    win.addstr(0,0,"Höchste Zeit!")
    win.addstr(1,0,"Bitte eine Taste drücken")
    win.refresh()
    pressed = win.getkey()
    if pressed.isspace():
        stdscr.addstr(0,0,"Sie haben eine <SPACE>-Taste gedrückt")
    else:
        stdscr.addstr(0,0,"{} haben Sie gedrückt.".format(pressed))
    stdscr.addstr(2,4,"Beliebige Taste drücken")

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
