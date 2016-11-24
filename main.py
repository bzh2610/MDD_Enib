# coding: utf8
#Carte principale
import tty, signal, sys, termios, time, os, termcolor
from strings import *
import UI, IO, controls, map, jump, iSecure_home


#initialisation
repertoire=os.path.dirname(os.path.abspath(__file__))
screen=[]
for j in range(22):
    screen.append([' '] * 100) #3 lignes, 20 caracteres

IO.load_objective()

def show_main_menu(a):
    UI_file='menu.txt'
    a=UI.load_board(UI_file, screen)
    UI.display_map(a)

show_main_menu(screen)

#Set text entry
set_orig_settings()
orig_settings = get_orig_settings()

commande=""
while commande != 'exit' : # ESC
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())

    commande=raw_input('root@188.166.172.81 : ')
    if(commande=="play"):
        a= IO.load_objective()
        if(not 'progress' in a):
            iSecure_home.init()
            IO.save_progress(True)
            IO.init_level()

        map.init()
        show_main_menu(screen)

    elif(commande=="exit"):
        break

    elif(commande=="skip"):
        map.init()
        show_main_menu(screen)

    elif(commande=="language"):
        print IO.get_language()
        if(strcmp("EN", IO.get_language())):
            IO.set_language('FR')
            print "La langue utilisée est désormais le Français."
        else:
            IO.set_language('EN')
            print "Language set to English"

    elif(commande == "rm ./save"):
        termcolor.cprint("Are you sure ? Y/N", 'red')
        temp=raw_input('')
        if(temp=='Y' or temp=='y'):
            IO.erase_progress()
            termcolor.cprint("Done.", 'red')


    elif(commande == "help"):
        show_main_menu(screen)

    else:
        termcolor.cprint("Type help to get a list of commands", 'yellow')
