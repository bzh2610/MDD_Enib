# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___strcmp()
'''
import tty, os, termios, sys, random
global_orig_settings=termios.tcgetattr(sys.stdin)
global_head_symbol='☺'
current_level=0;

def strcmp(a, b): #Compare deux chaines de texte
    if a in b:
        if b in a:
            return True

def get_orig_settings():
    return global_orig_settings

def get_head_symbol():
    return global_head_symbol

def set_orig_settings():
    global_orig_settings=termios.tcgetattr(sys.stdin)

def get_current_level():
    return current_level

def increase_level(i=0):

    global current_level
    current_level+=1

    if(i>0):
        current_level=int(i)
