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


def change_map(map, x_dest, y_dest, plateau, possible_objectives=[]):

    #Checks for achivements to pass
    temp_level=get_current_level()
    if(temp_level in possible_objectives):
        increase_level()

    #Move, clear the list, write position, display
    x,y=controls.get_player_pos(plateau)

    UI.clear(map, plateau)
    UI.load_board(map, plateau)
    UI.write_player(x_dest, y_dest, plateau)
    UI.display_map(plateau)
    return map


def init():
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


    entry = 0
    while entry != chr(27) : # ESC
        entry=sys.stdin.read(1)[0]
        if (strcmp(entry, 'E') or strcmp(entry, 'e')): #E provoque une action: changement de carte/interraction
            x,y=controls.get_player_pos(plateau)
            if(UI_file=="map.txt"):
                x,y=UI.get_map_position(plateau)
                if(x==0 and y==0):
                    UI_file=change_map('iSecure.txt', 55, 20, plateau, [0])

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


        #Log
        if (strcmp(entry, 'L') or strcmp(entry, 'l')):
            print controls.get_player_pos(plateau)
            #print plateau[1][0]

        if (strcmp(entry, 'D') or strcmp(entry, 'd')):
            controls.request_move(1, 0, plateau, UI_file)

        if (strcmp(entry, 'Z') or strcmp(entry, 'z')):
            controls.request_move(0, -1, plateau, UI_file)
        if (strcmp(entry, 'Q') or strcmp(entry, 'q')):
            controls.request_move(-1, 0, plateau, UI_file)
        if (strcmp(entry, 'S') or strcmp(entry, 's')):
            controls.request_move(0, 1, plateau, UI_file)
