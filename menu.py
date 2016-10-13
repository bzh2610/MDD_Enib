# coding: utf8
'''
Main map
'''
import tty
import sys
import termios
import time
import os

from strings import *
import UI
import controls
import map


'''
INIT
'''
repertoire=os.path.dirname(os.path.abspath(__file__))
screen=[]
for j in range(22):
    screen.append([' '] * 100) #3 lignes, 20 caracteres


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

    commande=raw_input('root@188.166.172.81 : ')
    if(commande=="play"):
        map.init()
        show_main_menu(screen)

    elif(commande=="exit"):
        break
    else:
        show_main_menu(screen)
