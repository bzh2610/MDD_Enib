
# coding: utf8
from random import randint
import IO
from strings import *
'''
Prototype:
string_to_list():
    Présentation:
        Converti une chaine en liste
    Utilité:
        Permet de convertir la chaine d'entrée en une liste,
        afin de pouvoir la modifier (et ne pas compter 2 fois un caractere).

check_combinations():
    Présentation:
        Compare l'entrée et le nomber_mystere
    Utilité:
        savoir combien de C. sont bien placés, incorrects ou mal placés.
'''

def string_to_list(string):
    liste=[];
    for i in range(0, len(string)):
        liste.append(string[i])
    return liste

def check_combinations(nomber_mystere, entry, essai):
    print nomber_mystere
    nomber_mystere_copy=string_to_list(nomber_mystere)

    #si l'entrée est au moins aussi longue que le nombre mystere
    if (len(entry)>=len(nomber_mystere)):
        #On recherche chaque caractere des deux chaines
        pions_bien_place=0
        mal_place=0
        bien_place=[]
        entry_copy=[]
        nomber_mystere_copy=[]
        #Vérifie les bien placés
        for i in range (0, len(nomber_mystere)):
            if  nomber_mystere[i]==entry[i]:
                pions_bien_place+=1
                bien_place.append(entry[i])
                entry_copy.append('*')
                nomber_mystere_copy.append('*')

            else:
                bien_place.append("*")
                nomber_mystere_copy.append(nomber_mystere[i])
                entry_copy.append(entry[i])

        #Vérifie les mal placés
        for i in range (0, len(entry)):
            for j in range (0, len(nomber_mystere_copy)):
                if entry_copy[i]==nomber_mystere_copy[j] and entry_copy[i]!='*':
                    #   print 'mal placé '+entry[i]+'-'+nomber_mystere_copy[j]
                    mal_place+=1
                    entry_copy[i]='*'
                    nomber_mystere_copy[j]='*'

        print (bien_place)
        output=str(mal_place)+" mal placés\n"+str(len(nomber_mystere)-(pions_bien_place+mal_place))+" inccorect"

        print output

    else:
        print "ERROR: Input does not match the password strcture."
        play(nomber_mystere, essai)



def play(nomber_mystere, essai=0):
    nomber_mystere=str(nomber_mystere).zfill(4)
    #print nomber_mystere
    if(essai==0):
        print "~~~~~~~~~~~~~~~~~~\n|    Mastermind    |\n~~~~~~~~~~~~~~~~~~\n\n"
        print "• Type 'exit' to quit\n"
        print "Password length: "+str(len(nomber_mystere))

    entry=str(raw_input(">")) #On utilise raw_input:
    # input interprête du python: une entrée commençant par 0
    #sera interprêtée comme octale et fera planter le code
    if(entry!='exit'):
        check_combinations(nomber_mystere, entry, essai)

        if nomber_mystere==entry:
            print "Le nombre était:"+nomber_mystere
            print "OK, réussi en "+str(essai)+" essais."
            temp_level=IO.get_current_level()
            if(temp_level==11):
                increase_level()
                IO.save_progress()
            return True
        else:
            play(nomber_mystere, essai+1)

def load():
    play(randint(0, 1))
#play(randint(0, 9999))
#play(8825)
