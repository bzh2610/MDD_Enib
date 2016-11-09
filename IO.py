# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___load_objective()
         |___save_progress()


'''

import sys
import time
import os
import codecs
import json #parse
import base64

from strings import *
import controls

repertoire=os.path.dirname(os.path.abspath(__file__))
plateau=[]
for j in range(29):
    plateau.append([' '] * 100) #3 lignes, 20 caracteres

def strcmp(a, b): #Compare deux chaines de texte
    if a in b:
        if b in a:
            return True

'''
read json objectives
'''
def load_objective(i='json'): #I is a number when specified out
    with open(repertoire + '/objectives.json') as data_file:
        data = json.load(data_file)
    if(get_current_level()==0):
        if ('progress' in data):
            niveau=base64.b64decode(data['progress'])
            increase_level(niveau)
    data_file.close()
        #Si un objectif est spécifié, le retourner sinon tout retourner.

    if(isinstance(i, int) and i <= len(data['objectives']) ):
        return data['objectives'][i]
    else:
        return data

def save_progress():
    current_progress=load_objective()
    current_progress['progress']=base64.b64encode(str(get_current_level()))
    with open(repertoire + '/objectives.json', 'w') as f:
        json.dump(current_progress, f, ensure_ascii=False)
    f.close()


def write_level(file_name, array):
    with open(repertoire + '/'+file_name, 'w') as f:
        for j in range(len(array)):
            print ''.join(array[j])+'\n'
            f.write(''.join(array[j])+'\n')
        f.close()
