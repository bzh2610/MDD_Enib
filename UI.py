# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___display_map()
         |___clear()
         |___load_board()
         |___get_map_position()
         |___write_player()
         |___erase_player()


Structure du personnage:

 *
===
| |

Position du personnage:
Le égal central (centre de la poitrine)
'''

import sys, time, os, time, codecs, base64
from strings import *
import IO, controls, map


repertoire=os.path.dirname(os.path.abspath(__file__))


def clear(UI_file, plateau): #Effacer la console entre les mouvements
    load_board(UI_file, plateau)
    display_map(plateau)
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")



'''

Fonction: load_board
Parameters: (string) UI_file: file in which the UI is stored as text
Return: plateau

'''

def erase_board(plateau):
    for j in range (len(plateau)):
        for i in range (len(plateau[j])):
            plateau[j][i]=' '
    return plateau

def get_plate_size(UI_file, plateau):
    i,j,jmax,imax=0,0,0,0

    f=codecs.open(UI_file, 'r', "utf-8")
    for line in f.readlines():
        j+=1
        i=0
        if j > jmax: #Récuperer jMax pour placer le texte d'objectif
            jmax=j
        for ch in line:
                if strcmp(ch, '\n'):
                    plateau[j][i]=' '
                else:
                    plateau[j][i]=ch.encode('utf-8')
                    i+=1
                    if i > imax: #Récuperer iMax pour centrer le texte d'objectif
                        imax=i
    f.close()
    return imax, jmax

def load_board(UI_file, plateau):
    #Erase board
    plateau=erase_board(plateau)

    #Load
    UI_file=repertoire+'/'+UI_file
    imax, jmax= get_plate_size(UI_file, plateau)

    #Si le fichier affiche un score
    #print os.path.basename(UI_file)
    if(strcmp(os.path.basename(UI_file), 'jump.txt')):
        plateau[jmax+1][imax+1]
        score=str(map.get_score())
        #print score #OK !
        decalage=(imax-len(score))/2
        for i in range(0, len(score)):
            if(i<len(score)):
                plateau[jmax+1][i+decalage]=score[i]


    #Si une carte est chargée, afficher l'objectif
    elif(os.path.basename(UI_file) != 'menu.txt'):
        plateau[jmax+1][imax+1]
        current_level=get_current_level()
        current_objective=IO.load_objective(current_level)
        
        if(len(current_objective)<100):
            decalage=(imax-len(current_objective))/2

            for i in range(0, len(current_objective)):
                if(i<len(current_objective)):
                    plateau[jmax+1][i+decalage]=current_objective[i]

    return plateau

'''

Fonction: afficher_carte
Parameters: -
Return: - : displays map

'''

def display_map(plateau): #Afficher le plateau
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
    out=''
    for j in range (0, len(plateau)):

        for i in range (0, len(plateau[j])):
                if(plateau[j][i]=='@'):
                    out=out+'_'
                elif(plateau[j][i]=='&'):
                    out=out+'|'
                elif(plateau[j][i]=='*'):
                    out=out+' '
                elif(plateau[j][i]=='A' and j==1):
                    out=out+'█'
                elif(i==99):
                    out=out+plateau[j][i]+'\n'
                else:
                    out=out+str(plateau[j][i])
        #out=out+'\n'
    print out+'\n'
    tty.setraw(sys.stdin)


'''
Fonction: get_map_position
Parameters: -
Return: - : displays map
'''


def get_map_position(plateau):

    position=controls.get_player_pos(plateau)
    x=position[0]
    y=position[1]
    map_x =0
    map_y=0
    if (5<x and x<16):
        map_x=1
    elif (17<x and x<28):
        map_x=2
    elif (29<x and x<40):
        map_x=3
    elif (41<x and x<52):
        map_x=4
    elif (53<x and x<64):
        map_x=5

    if (y>=3 and y<=6):
        map_y=1
    elif (y>=7 and y<=13):
        map_y=2
    elif (y>=14 and y<=20):
        map_y=3

    return [map_x, map_y]


'''
Fonction: write_player
Parameters: (x, y) as integers corresponding to the coordinates
Return: -
'''


def write_player(x, y, plateau): #Ecriture du personnage sur le tableau de jeu
    if(plateau[1][0]=='A'):
        plateau[y][x]=get_head_symbol()

    else:
        plateau[y-1][x]=get_head_symbol()
        plateau[y][x-1], plateau[y][x], plateau[y][x+1] = '=','=','='
        plateau[y+1][x-1], plateau[y+1][x+1] = '|','|'


'''
Fonction: erase_player
Parameters: (x, y) as integers corresponding to the coordinates
Return: -
'''

def erase_player(x, y, plateau):#Efface le personnage du tableau
    if(plateau[1][0]=='A'):
        plateau[y][x]=" "
    else:
        plateau[y-1][x]=''
        plateau[y][x-1], plateau[y][x], plateau[y][x+1] = '','',''
        plateau[y+1][x-1], plateau[y+1][x+1] = '',''
