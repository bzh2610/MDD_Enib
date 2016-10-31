# coding: utf8
'''
Main map
'''
import tty
import sys
import termios
import time
import os

from strings import *
import UI, IO
import controls
import select
import signal
import jump
import hanoi
'''
INIT
'''
GRAVITY=False

def change_map(map, x_dest, y_dest, plateau, possible_objectives=[]):

    #Checks for achivements to pass
    temp_level=get_current_level()
    if(temp_level in possible_objectives):
        increase_level()
        IO.save_progress()

    #Move, clear the list, write position, display
    x,y=controls.get_player_pos(plateau)

    UI.clear(map, plateau)
    UI.load_board(map, plateau)
    UI.write_player(x_dest, y_dest, plateau)
    UI.display_map(plateau)
    return map

"*****************SIGNAL************"
def interrupted(signum, frame):
    "called when read times out"
    raise Exception('EOT') #End of time

def input():
    try:
            #print 'You have 1 seconds to type in your stuff...'
            foo = sys.stdin.read(1)[0]
            return foo
    except Exception, exc:
            # timeout

            return 'OUT'

def set_signal():

    TIMEOUT = 0.25 # number of seconds your want for timeout
    signal.signal(signal.SIGALRM, interrupted)
    # set alarm
    #signal.alarm(TIMEOUT)
    signal.setitimer(signal.ITIMER_REAL, 0.25, 1)
    s = input()
    # disable the alarm after success
    signal.alarm(0)
    return s



"*****************SIGNAL************"

def init():
    global GRAVITY
    tty.setraw(sys.stdin)
    repertoire=os.path.dirname(os.path.abspath(__file__))
    plateau=[]
    for j in range(31):
        plateau.append([' '] * 100) #3 lignes, 20 caracteres

    '''labyrinthe
        UI_file='labyrinthe.txt'
        plateau=UI.load_board(UI_file, plateau)
        UI.write_player(70,1, plateau)
        UI.display_map(plateau)
    '''
    #print controls.get_player_pos(plateau)
    UI_file='map.txt'
    plateau=UI.load_board(UI_file, plateau)
    UI.write_player(41,14, plateau)
    UI.display_map(plateau)
    #print plateau


    #Set text entry
    set_orig_settings()
    orig_settings = get_orig_settings()


    entry = ''
    while entry != chr(27) : # ESC

        t0=time.time()

        if (strcmp(entry, 'E') or strcmp(entry, 'e')): #E provoque une action: changement de carte/interraction

            x,y=controls.get_player_pos(plateau)
            if(UI_file=="map.txt"):
                x,y=UI.get_map_position(plateau)
                #print x,y
                if (x==0 or y==0):
                    variable_inutile=0
                elif (x==1 and y==1):
                    UI_file=change_map('iSecure.txt', 55, 20, plateau, [0])
                elif (x==4 and y==2):
                    UI_file=change_map('steve_home.txt', 53, 22, plateau, [4])
                elif (x==3 and y==3):
                    UI_file=change_map('metro.txt', 75, 7, plateau, [5])
                elif (x==4 and y==3):
                    UI_file=change_map('void.txt', 20, 20, plateau)


            elif(UI_file=="iSecure.txt"):
                if(x>=60 and y>=21): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 40, 15, plateau)

                elif (x>=4 and x<=13 and y==11): #Joueur sur BOSS OFFICE
                    UI_file=change_map('boss_office.txt', 45, 18, plateau, [1])

            elif(UI_file=="boss_office.txt"):
                if(x>=59 and y>=18):
                    UI_file=change_map("iSecure.txt", 55, 20, plateau)

                if(x>=23 and x<=42 and y>=11 and y<=18):
                    UI_file=change_map("labyrinthe.txt", 70, 2,plateau, [2])

            elif(UI_file=="labyrinthe.txt"):
                if(x>=4 and y>=24):
                    UI_file=change_map("boss_office.txt", 45, 18,plateau, [3])
            elif(UI_file=="steve_home.txt"):
                if(x>=61 and y>=21):
                    UI_file=change_map("map.txt", 40, 15, plateau)

            elif(UI_file=="metro.txt"):
                if(x>=81 and y<=9):
                    UI_file=change_map("map.txt", 40, 15, plateau)
                elif(x>=71 and y>=13):
                    UI_file=change_map("cctv.txt", 55, 16, plateau, [6])
            elif(UI_file=="cctv.txt"):
                if(x>=59 and y>=16):
                    UI_file=change_map("metro.txt", 50, 15, plateau)
                elif(x>=2 and x<=20 and y<=16):
                    hanoi.play(4)
                elif(x>=22 and x<=39 and y<=16):
                    hanoi.play(5)


        if (strcmp(entry, 'T') or strcmp(entry, 't')):
            jump.generatemap(plateau)

        #Log
        if (strcmp(entry, 'L') or strcmp(entry, 'l')):
            print controls.get_player_pos(plateau)

        if (strcmp(entry, 'D') or strcmp(entry, 'd')):
            controls.request_move(1, 0, plateau, UI_file)

        if (strcmp(entry, 'Z') or strcmp(entry, 'z')):
            controls.request_move(0, -1, plateau, UI_file)

        if (strcmp(entry, 'Q') or strcmp(entry, 'q')):
            controls.request_move(-1, 0, plateau, UI_file)

        if (strcmp(entry, 'S') or strcmp(entry, 's')):
            controls.request_move(0, 1, plateau, UI_file)

        if (strcmp(entry, 'G') or strcmp(entry, 'g')):
            if GRAVITY:
                GRAVITY=False
            else:
                GRAVITY=True

        if (strcmp(entry, ' ') and GRAVITY):
            controls.request_move(0, -3, plateau, UI_file)

        if (strcmp(entry, 'OUT') and GRAVITY):
            if(UI_file=='jump.txt'):
                controls.request_move(0,1, plateau, UI_file)

        entry=set_signal()
