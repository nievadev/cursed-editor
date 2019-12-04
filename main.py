import curses
from curses import textpad

def main(stdscr):
    curses.raw()

    height, width = stdscr.getmaxyx()
    beg = (4, 10)
    end = (height - 4, width - 10)

    textpad.rectangle(stdscr, beg[0], beg[1], end[0], end[1])

    stdscr.move(beg[0] + 1, beg[1] + 1)

    line = str()
    lines = list()

    while True:
        key = stdscr.getch()
        cursor = stdscr.getyx()

        if key == 3:
            break

        elif key == 10:
            if cursor[0] + 1 == end[0]:
                continue

            lines.append(line + "\n")
            line = str()
            stdscr.move(cursor[0] + 1, beg[1] + 1)
            continue

        line += chr(key)
        stdscr.addstr(chr(key))
        stdscr.addstr(0, 0, str(len(line)))
        stdscr.addstr(1, 0, str(end[1])) 
        stdscr.move(cursor[0], cursor[1] + 1)


curses.wrapper(main)

with open("test_file", "r+") as f:
    f.write(buf)
