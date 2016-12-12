# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___strcmp()
'''
import tty, os, termios, sys, random
global_orig_settings=termios.tcgetattr(sys.stdin)
global_head_symbol='☺'
current_level=0

#Compares two strings a and b
def strcmp(a, b): #Compare deux chaines de texte
    if a in b:
        if b in a:
            return True
        else:
            return False
    else:
        return False

#Used to reset terminal to original settings after exiting the game
def get_orig_settings():
    return global_orig_settings

#Returns the symbol used for the head of the player (mark to identify his position)
def get_head_symbol():
    return global_head_symbol

#Set original settings, these settings will be reset when the program will quit
def set_orig_settings():
    global_orig_settings=termios.tcgetattr(sys.stdin)

#Returns the current level
def get_current_level():
    return current_level

#Reset level to 0
def init_level():
    global current_level
    current_level=0
    if(get_current_level()==0):
        return True
    else:
        return False

def set_level(param):
    global current_level
    current_level=param
    return True

#Increment level
def increase_level(i=0):

    global current_level
    current_level+=1


    if(i>0):
        current_level=int(i)
