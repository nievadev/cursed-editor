import curses
from curses import textpad

def main(stdscr):
    curses.raw()

    height, width = stdscr.getmaxyx()
    beg = (4, 10)
    end = (height - 4, width - 10)

    textpad.rectangle(stdscr, beg[0], beg[1], end[0], end[1])
    box_width = end[1] - beg[1]

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

        if len(line) + 1 == box_width:
            continue

        line += chr(key)
        stdscr.addstr(chr(key))

    buf = "".join(lines)

    with open("test_file", "w") as f:
        f.write(buf)

curses.wrapper(main)
