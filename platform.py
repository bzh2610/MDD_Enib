# coding: utf8

import tty, os, termios, sys, map, IO, UI, time
from strings import *
import random

def randbool():
    boolean=random.randint(0,1)
    return boolean

alignement=0

#Créé une liste d'obstacles
def generate_obstacles():

    coordonnees=[10]
    for k in range(500): #Pour chaque nombre de la liste (x obstacle)
        previous_coordinates=coordonnees[k]
        right=randbool() #Sera a droite si vrai
        current=0
        if((right or previous_coordinates<8)and previous_coordinates<90):
            current=random.randint(previous_coordinates+4, previous_coordinates+8)
        else:
            current=random.randint(previous_coordinates-8, previous_coordinates-4)
        coordonnees.append(current)

    #On commence à 10 héhéhé
    coordonnees.reverse()
    return coordonnees


#Génère une carte à partir de la liste d'obstacles fournie
def generate_map(coordonnees, avancement):
    output=[]
    for k in range(len(coordonnees)-5-avancement, len(coordonnees)-avancement):
        output.append(coordonnees[k]*' '+'====='+(90-coordonnees[k]-5)*' ')
        output.append(' '*90)
        output.append(' '*90)
        output.append(' '*90)
        output.append(' '*90)

    return output


#Map désigne le tableau contenant la carte
#obstacles_list désigne la liste des obstacles par coordonnées
def init(initialisation=True, obstacles_list=[], map=[], avancement=0):

    if(initialisation):
        obstacles_list=generate_obstacles()

    map=generate_map(obstacles_list, avancement)

    IO.write_level('platform.txt', map)


    while (500-avancement>len(obstacles_list)):
        obstacles_list.remove(obstacles_list[500-avancement])

    if(avancement>500-30):
        avancement-=1

    return obstacles_list, avancement
    print avancement

init()
