#/bin/env python3

# source
# https://docs.python.org/3/howto/curses.html

from curses import wrapper

def main(stdscr):
    stdscr.clear()

    for i in range(11):
        stdscr.addstr(i, 0, '10 + {} = {}'.format(i, 10+i))
    
    stdscr.addstr(10, 0, ','.join(map(str, dir(stdscr))))
    stdscr.addstr(0,0,str(stdscr.getmaxyx()))
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
