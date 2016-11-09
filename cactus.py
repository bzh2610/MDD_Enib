# coding: utf8

import tty, os, termios, sys, map, IO, UI, time
from strings import *

size_tower=0
alignement=0

def generate_cactus():
    position=0
    cactus=[]
    for i in range(200):
        cactus_position=random.randint(20, 50)
        cactus.append(position+cactus_position)
        position=position+cactus_position
    return cactus

def generate_map(cactus_array, avancement):
    map=[]
    for j in range(22):
        map.append([' '] * 90) #3 lignes, 20 caracteres
    line=''

    for k in range(len(cactus_array)): #Pour chaque nombre de la liste (x obstacle)

        i=cactus_array[k] #i=coordonnée

        if(k==0):
            j=0
        else: #Enlever le décalage entre les deux obstacles les plus proches pour connaitre l'écart
            j=cactus_array[k-1]

        line=line+' '*(i-j)

        if(cactus_array[k]>avancement):
            line=line+'|'

    line=line[:90]
    map.append(line)
    line=line.replace(' ', '=')
    map.append(line)

    return map



def init(initialisation=True, cactus_list=[], map=[], avancement=0):
    if(initialisation):
        cactus_list=generate_cactus()
        map=generate_map(cactus_list, 0)

    else:
        map=generate_map(cactus_list, avancement)

    IO.write_level('jump.txt', map)

    taille=len(cactus_list)
    i=0
    while i < taille:
        if cactus_list[i]==0:
            cactus_list.remove(cactus_list[i])
            taille-=1
        i+=1

    for i in range(len(cactus_list)):
        cactus_list[i]=cactus_list[i]-1

    return cactus_list, avancement

    #time.sleep(0.1)
    #cactus.init(False, cactus_list, map, avancement)
