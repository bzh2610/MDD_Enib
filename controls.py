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

'''
Vérifie si le déplacement vers le haut où le bas est possible sur le plateau, une fois les cases spéciales enlevées
Entrée: valeurs du plateau en TR, TL,
                               R, L
                              BR, BL
(TOP, MIDDLE, BOTTOM)
'''
def check_top_middle_bottom(top_temp, r, l, br, bl, letters):

    top=False
    middle=False
    bottom=False

    middle_right_chk=bottom_right_chk=middle_left_chk=bottom_left_chk=False
    # RIGHT
    for letter in letters:
        top =   top or strcmp(top_temp, letter) #top= haut lettre 1
        middle_right_chk= middle_right_chk or  strcmp(r, letter)
        bottom_right_chk= bottom_right_chk or strcmp(br, letter)

    # LEFT
    for letter in letters:
        middle_left_chk= middle_left_chk or strcmp(l, letter)
        bottom_left_chk= bottom_left_chk or strcmp(bl,letter)


    middle= middle_left_chk and middle_right_chk
    bottom= bottom_left_chk and bottom_right_chk


    return top and middle and bottom

def request_move(x, y, plateau, UI_file):
    if(UI_file=='labyrinthe.txt'):
        position=get_player_pos(plateau)

        UI.load_board(UI_file, plateau)

        move='False'
        if(position[1]+y<len(plateau)):
            move=plateau[position[1]+y][position[0]+x]




        if  move ==' ' and (position[1]+y)>0 and (position[1]+y<len(plateau)): #position[1]+y+1 = position + deplacement + tete personnage
            UI.write_player(position[0], position[1], plateau)
            move_player(x, y, plateau, UI_file)

        else:
            UI.write_player(position[0], position[1], plateau)


    else:
        position=get_player_pos(plateau)
        UI.load_board(UI_file, plateau)

        top=plateau[position[1]+y-1][position[0]+x]
        left=plateau[position[1]+y][position[0]+x-1]
        right=plateau[position[1]+y][position[0]+x+1]

        if(position[1]+y+1<len(plateau)):
            bottom_left=plateau[position[1]+y+1][position[0]+x-1]
            bottom_right=plateau[position[1]+y+1][position[0]+x+1]
        else:
            bottom_right=bottom_left='False'


        free=check_top_middle_bottom(top, right, left, bottom_right, bottom_left, ['@', ' ', '&'])

        if  free and (position[1]+y-1)>0 and (position[1]+y+1<len(plateau)): #position[1]+y+1 = position + deplacement + tete personnage
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
            if strcmp(plateau[j][i], get_head_symbol()):
                if (plateau[1][0]=='A'):
                    return [i, j]
                else:
                    return [i, j+1]
