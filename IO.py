# coding: utf8
'''
USER INTERFACE

Fonctions:
         |___load_objective()
         |___save_progress()


'''

import sys, time, os, codecs, json, base64
from strings import *
import controls

repertoire=os.path.dirname(os.path.abspath(__file__))
plateau=[]

#Retourne la langue utilisée dans le jeu
#FR ou EN
def get_language():
    data_file=codecs.open(repertoire + '/objectives.json', 'r', encoding='utf-8')
    data = json.loads(data_file.read())
    data_file.close()

    try:
        if data['language']:
            return data['language']
        else:
            return 'FR'
    except KeyError:
        return 'FR'



#Ecrit la langue utilisée dans le jeu
def set_language(language='FR'):
    data=load_objective()
    #print data
    #print language
    data['language']=language
    with codecs.open(repertoire + '/objectives.json', "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
    f.close()
    return True


#Lire les objectifs jSON,
#Retrourne la liste complete de tout les objectifs
def load_objective(i='json'): #I is a number when specified out, define it as a string if not parameter is specified
    data_file=codecs.open(repertoire + '/objectives.json', 'r', encoding='utf-8')
    data = json.loads(data_file.read())
    if(get_current_level()==0):
        if ('progress' in data):
            niveau=base64.b64decode(data['progress'])
            increase_level(niveau)
    data_file.close()

        #Si un objectif est spécifié, le retourner sinon tout retourner.
    language=get_language()

    if(isinstance(i, int) and i <= len(data['objectives'][language]) ): #Si l'objectif spécifié existe

        return data['objectives'][language][i]
    else:
        return data


#Sauvegarde la progression
#Si le parametre init est spécifié vrai, l'objectif sera fixé
#À 0 en base64
def save_progress(init=False):
    current_progress=load_objective()
    level=str(get_current_level())
    if(init):
        current_progress['progress']=base64.b64encode('0')
    else:
        current_progress['progress']=base64.b64encode(level)

    with codecs.open(repertoire + '/objectives.json', 'w', encoding="utf-8") as f:
        json.dump(current_progress, f,indent=4, sort_keys=True, ensure_ascii=False)
    f.close()

def erase_progress():
    with codecs.open(repertoire + '/objectives.json', 'r', encoding="utf-8") as data_file:
        data = json.load(data_file)

    try:
        if data['progress']:
            del data['progress']
    except KeyError:
        print "Progress Key doesn't exist, may not be an error"

    with codecs.open(repertoire + '/objectives.json', 'w', encoding="utf-8") as f:
        json.dump(data, f,indent=4, sort_keys=True,  ensure_ascii=False)
    f.close()

    init_level()




def write_level(file_name, array):
    with open(repertoire + '/'+file_name, 'w') as f:
        for j in range(len(array)):
            print ''.join(array[j])+'\n'
            f.write(''.join(array[j])+'\n')
        f.close()
