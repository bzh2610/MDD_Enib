# coding: utf8
'''
Main map
'''
import tty
import sys
import termios
import time
import os
import termcolor
from strings import *
import UI, IO
import controls
import map


'''
INIT
'''
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

#COMMENT OUT FOR PROD
#map.init()
#show_main_menu(screen)
#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
#END



commande=""
while commande != 'exit' : # ESC
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())

    commande=raw_input('root@188.166.172.81 : ')
    if(commande=="play"):
        map.init()
        show_main_menu(screen)

    elif(commande=="exit"):
        break

    elif(commande == "rm ./save"):
        termcolor.cprint("Are you sure ? Y/N", 'red')
        temp=raw_input('')
        if(temp=='Y' or temp=='y'):
            termcolor.cprint("Done.", 'red')

    elif(commande == "help"):
        show_main_menu(screen)

    else:
        termcolor.cprint("Type help to get a list of commands", 'yellow')
