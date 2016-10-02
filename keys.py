# coding: utf8
'''

left arrow: 37
up arrow: 38
right arrow: 39
down arrow: 40


Structure du personnage:

 *
===
| |

Position du personnage:
Le égal central (centre de la poitrine)
'''
import tty
import sys
import termios
import time
import os

repertoire=os.path.dirname(os.path.abspath(__file__))
plateau=[]
for j in range(29):
    plateau.append([' '] * 100) #3 lignes, 20 caracteres

def strcmp(a, b): #Compare deux chaines de texte
    if a in b:
        if b in a:
            return True

def personnage(x, y): #Ecriture du personnage sur le tableau de jeu
    plateau[y][x]="="
    plateau[y][x-1]="="
    plateau[y][x+1]="="
    plateau[y-1][x]="*"
    plateau[y+1][x-1]="|"
    plateau[y+1][x]=" "
    plateau[y+1][x+1]="|"

def erase_player(x, y):#Efface le personnage du tableau
    plateau[y][x]=" "
    plateau[y][x-1]=" "
    plateau[y][x+1]=" "
    plateau[y-1][x]=" "
    plateau[y+1][x-1]=" "
    plateau[y+1][x]=" "
    plateau[y+1][x+1]=" "

def get_player_pos(): #Obtenir les coordonnées du joueur sous forme de liste
    for j in range (0, len(plateau)):
        for i in range (0, len(plateau[j])):
            if strcmp(plateau[j][i], '*'):
                return [i, j+1]

def clear(): #Effacer la console entre les mouvements
    load_board()
    afficher_carte()
    for i in range(5):
        print '\n'

def afficher_carte(): #Afficher le plateau
    out=''
    for j in range (0, len(plateau)):
        for i in range (0, len(plateau[j])):
            out=out+str(plateau[j][i])
        #out=out+'\n'
    print out+'\n'

def deplacer_personnage(x, y): #Déplacer le perso
    position=get_player_pos()
    erase_player(position[0], position[1])
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    clear()
    load_board()
    personnage(position[0]+x, position[1]+y)
    afficher_carte()
    tty.setraw(sys.stdin)

def load_board():
    i=0
    j=0
    f= open(repertoire+"/level1.txt", 'r')
    for line in f.readlines():
        j+=1
        i=0

        for ch in line:
                if(strcmp(ch, '\n') or strcmp(ch, 'E')):
                    plateau[j][i]=' '

                else:
                    plateau[j][i]=ch
                    i+=1
    f.close()




print get_player_pos()
load_board()
personnage(5,26)
afficher_carte()
#print plateau

def request_move(x, y):
    position=get_player_pos()
    load_board()
    if strcmp(plateau[position[1]+y+1][position[0]+x], '_'): #position[1]+y+1 = position + deplacement + tete personnage
        personnage(position[0], position[1])
        deplacer_personnage(x, y)
    else:
        personnage(position[0], position[1])

#Regalges entree textuelle
orig_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)
entree = 0
while entree != chr(27) : # ESC
    entree=sys.stdin.read(1)[0]
    #Gestion déplacements
    if (strcmp(entree, 'D') or strcmp(entree, 'd')):
        request_move(1, 0)
    if (strcmp(entree, 'Z') or strcmp(entree, 'z')):
        request_move(0, -1)
    if (strcmp(entree, 'Q') or strcmp(entree, 'q')):
        request_move(-1, 0)
    if (strcmp(entree, 'S') or strcmp(entree, 's')):
        request_move(0, 1)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
