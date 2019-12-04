import curses

def main(stdscr):
    curses.raw()

    HEIGHT, WIDTH = stdscr.getmaxyx()

    line = str()
    lines = list()

    beg = (4, 10)
    end = (HEIGHT - 4, WIDTH - WIDTH // 10 - 3)

    textpad.rectangle(stdscr, beg[0], beg[1], end[0], end[1]) 

    while True:
        key = stdscr.getch()
        
        if key == 263:
            buf = buf[:-1]

        elif key == 3:
            break

        elif key == 10:
            lines.append(line)
            stdscr.move(beg[0] + len(lines), beg[1])

        else:
            line += chr(key)

        stdscr.clear()
        textpad.rectangle(stdscr, beg[0], beg[1], end[0], end[1]) 
        stdscr.move(beg[0] + len(lines) + 1, beg[1] + 1)
        stdscr.addstr(line)

curses.wrapper(main)
