# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___request_move()
         |___clear()
         |___load_board()
         |___get_map_position()
'''
from strings import *
import UI
import tty, os, termios, sys

def request_move(x, y, plateau, UI_file):
    position=get_player_pos(plateau)
    UI.load_board(UI_file, plateau)

    top_right=plateau[position[1]+y-1][position[0]+x+1]
    top_left=plateau[position[1]+y-1][position[0]+x-1]
    left=plateau[position[1]+y][position[0]+x-1]
    right=plateau[position[1]+y][position[0]+x+1]
    bottom_left=plateau[position[1]+y+1][position[0]+x-1]
    bottom_right=plateau[position[1]+y+1][position[0]+x+1]

    top= strcmp(top_right, ' ') and strcmp(top_left, ' ')
    middle= strcmp(right, ' ') and strcmp(left, ' ')
    bottom= strcmp(bottom_right, ' ') and strcmp(bottom_left, ' ')

    if  top and middle and bottom and (position[1]+y-1)>0 : #position[1]+y+1 = position + deplacement + tete personnage
        UI.write_player(position[0], position[1], plateau)
        move_player(x, y, plateau, UI_file)
        #print plateau[position[1]+y-1][position[0]+x+1]
    else:
        UI.write_player(position[0], position[1], plateau)

def move_player(x, y, plateau, UI_file): #Déplacer le perso
    position=get_player_pos(plateau)
    #print position
    UI.erase_player(position[0], position[1], plateau)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
    UI.clear(UI_file, plateau)
    UI.load_board(UI_file, plateau)
    UI.write_player(position[0]+x, position[1]+y, plateau)
    UI.display_map(plateau)
    tty.setraw(sys.stdin)

def get_player_pos(plateau): #Obtenir les coordonnées du joueur sous forme de liste
    for j in range (0, len(plateau)):
        for i in range (0, len(plateau[j])):
            if strcmp(plateau[j][i], '*'):
                return [i, j+1]
