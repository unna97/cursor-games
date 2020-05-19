from curses import halfdelay, beep, wrapper, error as c_err
import curses
# from time import sleep

def set_colors(frame):
    if frame % 2 == 0:
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    else:
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_WHITE)

def main(stdscr):
    halfdelay(1) # 10 fps
    frame = 0
    key = ""
    message = "~(n  n):3<"
    while key != "q":
        try:
            stdscr.clear()
            stdscr.addstr((frame % 80) * " ")
            stdscr.addstr(message, curses.color_pair(1))
            key = stdscr.getkey()
        except c_err:
            key = ""
        finally:
            frame += 1
            if len(message) > 80:
                message = "~(n  n):3<"
            set_colors(frame)
    # with open('debug.txt', 'a') as f:
    #     f.write(f"can change color: {curses.can_change_color()}\n")


wrapper(main)
