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
import cactus
'''
INIT
'''
GRAVITY=False
list_cactus=[]
avancement=0
plateau=[]

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
iteration_compteur=0


'''iteration_compteur=0

moves_in_air=0
def input():
    global moves_in_air
    global iteration_compteur
    try:

            #print 'You have 1 seconds to type in your stuff...'
            iteration_compteur+=1
            if(iteration_compteur>=10):
                iteration_compteur=0
                if(moves_in_air==3 and GRAVITY):
                    foo='DOWN'
                    moves_in_air=0
                else:
                    foo = sys.stdin.read(1)[0]
                    moves_in_air+=1
            else:
                foo='OUT'
                return foo

'''

moves_in_air=0
def input():
    global moves_in_air
    global plateau
    #global iteration_compteur
    try:

            #print 'You have 1 seconds to type in your stuff...'

            if(moves_in_air==3 and GRAVITY):
                foo='DOWN' #REMETTRE OUT POUR FAIRE TOMBER
                moves_in_air=0
            else:
                foo = sys.stdin.read(1)[0]
                moves_in_air+=1
            return foo

    except Exception, exc:
            # timeout

            return 'OUT'

def set_signal():

    TIMEOUT = 0.04 # number of seconds your want for timeout
    signal.signal(signal.SIGALRM, interrupted)
    # set alarm
    #signal.alarm(TIMEOUT)
    signal.setitimer(signal.ITIMER_REAL, TIMEOUT, 1)
    s = input()
    # disable the alarm after success
    signal.alarm(0)
    return s






"*****************SIGNAL************"

def init():
    reload(sys)
    sys.setdefaultencoding('utf8')
    global GRAVITY
    global moves_in_air
    global plateau
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

    global list_cactus
    global avancement
    global iteration_compteur
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
                elif (x==1 and y==3):
                    UI_file=change_map('museum.txt', 4, 23, plateau)
                elif (x==4 and y==1):
                    UI_file=change_map('airport.txt', 77, 23, plateau)
                elif (x==3 and y==2):
                    #UI_file=change_map('jump.txt', 40, 13, plateau)
                    list_cactus, avancement =cactus.init()
                    UI_file=change_map('jump.txt', 5, 20, plateau)


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
                    UI_file=change_map("map.txt", 40, 15, plateau, [9])
                elif(x>=71 and y>=13):
                    UI_file=change_map("cctv.txt", 55, 16, plateau, [6])
            elif(UI_file=="cctv.txt"):
                if(x>=59 and y>=16):
                    UI_file=change_map("metro.txt", 50, 15, plateau)
                elif(x>=2 and x<=20 and y<=16):
                    hanoi.play(4, plateau)
                elif(x>=22 and x<=39 and y<=16):
                    hanoi.play(3, plateau)
            elif(UI_file=='museum.txt'):
                if((x>=82 and y<=3) or  (x<=3 and y>=23)):
                    UI_file=change_map("map.txt", 40, 15, plateau)

            elif(UI_file=='airport.txt'):
                if(x>=81 and y>=21):
                    UI_file=change_map('map.txt', 40, 15, plateau)


        #print '--'+entry+'--'
        if (strcmp(entry, 'T') or strcmp(entry, 't')):
            jump.generatemap(plateau)

        if (strcmp(entry, 'M') or strcmp(entry, 'm')):
            UI_file=change_map("map.txt", 40, 15, plateau)

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
                moves_in_air=0
            else:
                GRAVITY=True
                moves_in_air=0

        if (strcmp(entry, ' ') and GRAVITY):

            #print plateau
            x,y=controls.get_player_pos(plateau)

            if(strcmp(plateau[y+2][x], '=')):
                controls.request_move(0, -5, plateau, UI_file)

        if (strcmp(entry, 'OUT') and GRAVITY):
            if(UI_file=='jump.txt'):
                iteration_compteur+=1
                if(iteration_compteur>=4):
                    entry='DOWN'
                    iteration_compteur=0
                x,y=controls.get_player_pos( plateau)
                list_cactus, avancement = cactus.init(False, list_cactus, map, avancement)
                UI_file=change_map('jump.txt', x, y, plateau)

        if (strcmp(entry, 'DOWN') and GRAVITY):
            controls.request_move(0,1, plateau, UI_file)
            x,y=controls.get_player_pos( plateau)


        if(UI_file=='jump.txt'):
            entry=set_signal()
        else:
            entry=sys.stdin.read(1)[0]

        #For debug, display time between moves
        #print time.time()-t0
