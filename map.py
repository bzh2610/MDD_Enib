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
import UI
import controls


'''
INIT
'''
repertoire=os.path.dirname(os.path.abspath(__file__))
plateau=[]
for j in range(29):
    plateau.append([' '] * 100) #3 lignes, 20 caracteres

#print controls.get_player_pos(plateau)
UI_file='map.txt'
UI.load_board('map.txt', plateau)
UI.write_player(40,15, plateau)
UI.display_map(plateau)
#print plateau


#Set text entry
set_orig_settings()
orig_settings = get_orig_settings()

tty.setraw(sys.stdin)
entry = 0
while entry != chr(27) : # ESC
    entry=sys.stdin.read(1)[0]
    if (strcmp(entry, 'E') or strcmp(entry, 'e')):
        x,y=UI.get_map_position(plateau)
        #print x,y
        if(x==0 and y==0):
            UI_file='iSecure.txt'
            UI.clear(UI_file, plateau)
            UI.load_board(UI_file, plateau)
            UI.write_player(55, 25, plateau)
            UI.display_map(plateau)
            #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            #menu.iSecure()



        #print (position[0]-7)/6
        #print position
    if (strcmp(entry, 'D') or strcmp(entry, 'd')):
        controls.request_move(1, 0, plateau, UI_file)
    if (strcmp(entry, 'Z') or strcmp(entry, 'z')):
        controls.request_move(0, -1, plateau, UI_file)
    if (strcmp(entry, 'Q') or strcmp(entry, 'q')):
        controls.request_move(-1, 0, plateau, UI_file)
    if (strcmp(entry, 'S') or strcmp(entry, 's')):
        controls.request_move(0, 1, plateau, UI_file)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
#menu.iSecure
