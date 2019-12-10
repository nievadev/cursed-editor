import curses
from curses import textpad

def main(stdscr):
    curses.raw()
    stdscr.keypad(True)

    file_name = "tf"

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

        if key == 3: # User sends signal of interruption
            if len(lines) == 0:
                lines = [line + "\n"]

            buf = "".join(lines)

            with open(file_name, "w") as f:
                f.write(buf)

            break

        elif key == 10: # User presses enter
            if cursor[0] + 1 == end[0]:
                continue

            lines.append(line + "\n")
            line = str()
            stdscr.move(cursor[0] + 1, beg[1] + 1)

        elif key == 263: # User presses backspace
            if cursor[1] - 1 == beg[1]:
                continue
    
            stdscr.addstr(cursor[0], cursor[1] - 1, " ")
            stdscr.move(cursor[0], cursor[1] - 1)
            line = line[:-1]

        else: # User basically writes a character that's not backspace, enter nor Ctrl + C
            if len(line) + 1 == box_width:
                continue

            line += chr(key)

            stdscr.addstr(chr(key))

curses.wrapper(main)
