import curses
import random


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

maxl = curses.LINES - 1
maxc = curses.COLS - 1

background = []
player_c = player_l = 0

def init():
    global player_c, player_l
    for i in range(maxl):
        background.append([])
        for j in range(maxc):
            background[i].append(' ' if random.random() > 0.025 else '.')
    player_l = random.randint(0, maxl)
    player_c = random.randint(0, maxc)

def endscreen(a, min_val, max_val):
    if a > max_val:
        return max_val
    if a < min_val:
        return min_val
    return a

def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, background[i][j])
    stdscr.addch(player_l, player_c, 'x')
    stdscr.refresh()

def move(c):
    global player_l, player_c
    if c == 'w':
        player_l -= 1
    elif c == 's':
        player_l += 1
    elif c == 'a':
        player_c -= 1
    elif c == 'd':
        player_c += 1

    player_l = endscreen(player_l, 0, maxl - 1)    
    player_c = endscreen(player_c, 0, maxc - 1)

init()

playing = True
while playing:
    try:
        c = stdscr.getkey()
    except:
        c = ''
    if c in 'asdw':
        move(c)
    elif c == 'q':
        playing = False
    draw()

stdscr.clear()
stdscr.refresh()
