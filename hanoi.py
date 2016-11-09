# coding: utf8

import tty, os, termios, sys, map, IO
from strings import *

size_tower=0
alignement=0

def init(size):
    tours=[[]]

    for row in range(3):
        if(row==0):
            value=1
            for i in range(size):
                tours[0].append(value)
                value+=2
        else:
            tours.append([0] * size) #3 lignes, 20 caracteres

    global size_tower
    size_tower=tours[0][len(tours[0])-1]+2
    global alignement
    alignement=(size_tower-1)/2

    return tours


def show_towers(tours):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
    plateau=[]
    for j in range(len(tours[0])+1):
        plateau.append([' '] * 24) #3 lignes, 20 caracteres
    output='\n'


    for i in range (len(tours[0])):
        for j in range (len(tours)):
                if tours[j][i]==0:
                    output=output+alignement*' '+'|'+alignement*' '
                else:
                    output=output+(size_tower-tours[j][i])/2*' '+tours[j][i]*'='+(size_tower-tours[j][i])/2*' '


        output=output+'\n'
    print output



def play(size, plateau):
    tours=init(size)

    first_input=True
    source=0
    destination=0
    invalid=False
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
    print "This puzzle is an Hanoe Towers game, here are the rules:\n"
    print "•You can move a ring to any of the towers as long as you don't put a ring on top of a smaller one\n"
    print "•The goal is to transfer all the rings from the first tower to the last\n"
    print "•To move a ring, enter the number of the tower you want to move it from to the number of the tower you want to move it to\n"
    print "Eg: type 1 and then 3 to move a ring from the first tower to the last"

    show_towers(tours)
    while tours[2][0]==0 or not sorted(tours[2], reverse=True):
        tty.setraw(sys.stdin)
        entry=sys.stdin.read(1)[0]


        if entry.isdigit():
            entry=int(entry)
            if(entry>3):
                first_input=True
                invalid=True
                print "Invalid "
            else:
                entry=entry-1
                print entry
                invalid=False
        else:
            if(entry==chr(27)):
                UI_file=map.change_map("cctv.txt", 55, 16, plateau, [6])
                break
            first_input=True
            invalid=True
            print 'Invalid'



        moved=False
        if first_input and not invalid:
            source=entry
            first_input=False

        elif not first_input and not invalid:
            destination=entry
            first_input=True
            if(destination != source): #Si on déplace un anneau
                for i in range(len(tours[source])):
                    if(tours[source][i] != 0 and not moved): #On choisi le 1er anneau que l'on trouve et on le marque comme "pris"
                        moved=True
                        finished=False  #Le tour n'est pas fini

                        for j in range(len(tours[destination])):


                            if(tours[destination][j] != 0):
                                if(tours[destination][j]<tours[source][i]):
                                    pass
                                    finished=True
                                    show_towers(tours)

                                elif (tours[destination][j]>tours[source][i]  and j>0 and not finished): #Si la tour de destination a déja des briques

                                    tours[destination][j-1]=tours[source][i]
                                    tours[source][i]=0
                                    show_towers(tours)
                                    finished=True

                            elif(tours[destination][len(tours[destination])-1] == 0 and not finished): #Si la tour est vide

                                tours[destination][len(tours[destination])-1]=tours[source][i]
                                tours[source][i]=0
                                show_towers(tours)
                                finished=True



        else:
            pass

    if(tours[2][0]!=0 and sorted(tours[2], reverse=True)):

        print "Not that bad..."
        increase_level()
        IO.save_progress()
        UI_file=map.change_map("cctv.txt", 55, 16, plateau, [6])
        return 0

#play(5)
