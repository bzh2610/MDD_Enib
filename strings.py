# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___strcmp()
'''
import tty, os, termios, sys
global_orig_settings=termios.tcgetattr(sys.stdin)

def strcmp(a, b): #Compare deux chaines de texte
    if a in b:
        if b in a:
            return True

def get_orig_settings():
    return global_orig_settings

def set_orig_settings():
    global_orig_settings=termios.tcgetattr(sys.stdin)
