import curses
from curses import textpad

def main(stdscr):
    curses.raw() # We set raw so we can handle signals such interruption's

    file_name = "tf"

    height, width = stdscr.getmaxyx()
    beg = (4, 10) # Top left coordinates of graphical 2d box
    end = (height - 4, width - 10) # Botttom right coordinates of graphical 2d box

    textpad.rectangle(stdscr, beg[0], beg[1], end[0], end[1]) # Drawing 2d box
    box_width = end[1] - beg[1] # Just calculting the box's width

    stdscr.move(beg[0] + 1, beg[1] + 1)

    line = str()
    lines = list()

    while True:
        key = stdscr.getch()
        cursor = stdscr.getyx()

        # User sends signal of interruption
        if key == 3: 
            if len(lines) == 0:
                lines = [line + "\n"]

            buf = "".join(lines)

            with open(file_name, "w") as f:
                f.write(buf)

            break

        # User presses enter
        elif key == 10: 
            # If cursor got to the bottom, just don't do anything
            if cursor[0] + 1 == end[0]: 
                continue

            lines.append(line + "\n")
            line = str()
            stdscr.move(cursor[0] + 1, beg[1] + 1)

        # User presses backspace
        elif key == 263: 
            # If cursor got to the right wall of the box, just don't do anything
            if cursor[1] - 1 == beg[1]: 
                continue
    
            stdscr.addstr(cursor[0], cursor[1] - 1, " ")
            stdscr.move(cursor[0], cursor[1] - 1)
            line = line[:-1]

        # User basically writes a character that's not backspace, enter nor Ctrl + C
        else: 
            if len(line) + 1 == box_width:
                continue

            line += chr(key)

            stdscr.addstr(chr(key))

curses.wrapper(main)
