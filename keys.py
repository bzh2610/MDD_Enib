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

plateau=[]
for j in range(20):
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

def erase_player(x, y): #Efface le personnage du tableau
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
    for i in range(40):
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
    personnage(position[0]+x, position[1]+y)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    clear()
    afficher_carte()
    tty.setraw(sys.stdin)



personnage(3,15)
afficher_carte()

#Regalges entree textuelle
orig_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)
entree = 0
while entree != chr(27) : # ESC
    entree=sys.stdin.read(1)[0]
    #Gestion déplacements
    if (strcmp(entree, 'D') or strcmp(entree, 'd')):
        deplacer_personnage(1, 0)
    if (strcmp(entree, 'Z') or strcmp(entree, 'z')):
        deplacer_personnage(0, -1)
    if (strcmp(entree, 'Q') or strcmp(entree, 'q')):
        deplacer_personnage(-1, 0)
    if (strcmp(entree, 'S') or strcmp(entree, 's')):
        deplacer_personnage(0, 1)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
