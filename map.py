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

def change_map(map, x_dest, y_dest, plateau):
    x,y=controls.get_player_pos(plateau)
    UI_file=map
    UI.clear(UI_file, plateau)
    UI.load_board(UI_file, plateau)
    UI.write_player(x_dest, y_dest, plateau)
    UI.display_map(plateau)


def init():
    repertoire=os.path.dirname(os.path.abspath(__file__))
    plateau=[]
    for j in range(31):
        plateau.append([' '] * 100) #3 lignes, 20 caracteres

    #print controls.get_player_pos(plateau)
    UI_file='map.txt'
    plateau=UI.load_board('map.txt', plateau)
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
            #E provoque une action: changement de carte/interraction
            x,y=controls.get_player_pos(plateau)
            if(UI_file=="map.txt"):
                #print x,y
                x,y=UI.get_map_position(plateau)
                if(x==0 and y==0):
                    UI_file='iSecure.txt'
                    UI.clear(UI_file, plateau)
                    UI.load_board(UI_file, plateau)
                    UI.write_player(55, 20, plateau)
                    UI.display_map(plateau)
                    #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
                    #menu.iSecure()

            elif(UI_file=="iSecure.txt"):
                if(x>=60 and y>=21): #Joueur sur la case de sortie
                    UI_file='map.txt'
                    UI.clear(UI_file, plateau)
                    UI.load_board(UI_file, plateau)
                    UI.write_player(40, 15, plateau)
                    UI.display_map(plateau)

                elif (x>=4 and x<=13 and y==11): #Joueur sur BOSS OFFICE
                    UI_file='boss_office.txt'
                    UI.clear(UI_file, plateau)
                    UI.load_board(UI_file, plateau)
                    UI.write_player(45, 18, plateau)
                    UI.display_map(plateau)


            elif(UI_file=="boss_office.txt"):
                if(x>=59 and y>=18):
                    UI_file="iSecure.txt"
                    change_map(UI_file, 55, 20, plateau)

                if(x>=23 and x<=42 and y>=11 and y<=18):
                    UI_file="labyrinthe.txt"
                    change_map(UI_file, 71, 2,plateau)




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

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    #menu.iSecure
