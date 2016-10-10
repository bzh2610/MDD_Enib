# coding: utf8
from termcolor import colored
from random import randint
import time
import mastermind

def iSecure():
    print colored("\nSteve travaille chez AllSecure, une grande société spécialisée dans le sécurité informatique. Il doit mettre à jour l'un des vieux serveur de la société. \n", 'yellow')
    null=raw_input("Entrée pour continuer")
    ls()

def ls():
    print colored("Steve est connecté, 'ls' permet de lister les fichiers, voyons ce qu'il y a sur ce serveur ..\n ", 'yellow')
    entree=raw_input("Steve@iCorporate: ")
    if(entree == "ls"):
        print "employees, contracts, offices, devices, REMOTE_FOLDER"
        print colored("Ok, je dois déplacer tout ces fichiers vers le serveur distant, pour ce faire: 'mv ./* ./REMOTE_FOLDER'", 'yellow')
        mv()

    else:
        ls()
def mv():
    entree=raw_input("Steve@iCorporate: ")
    if entree.startswith('mv'):
        sudo()

def sudo():
    print colored("Error: unsufficient permissions, do you have super-user rights ?", 'red')
    print colored("Ohoh, rééssayons avec sudo [commande]. En tant qu'administrateur, cela marchera", 'yellow')
    entree=raw_input("Steve@iCorporate: ")
    if (entree.startswith('sudo')):
        entree=raw_input('Password: ')
        print "Processing ..."
        time.sleep(1)
        print "Processing ..."
        time.sleep(1)
        for i in range(0, 100):
            print colored("INTERNAL ERROR", 'red')
            time.sleep(0.01)
        print colored(" /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$\n| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$__  $$\n | $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$      | $$  \ $$\n| $$$$$$$$| $$$$$$$$| $$      | $$$$$/  | $$$$$   | $$  | $$\n | $$__  $$| $$__  $$| $$      | $$  $$  | $$__/   | $$  | $$\n | $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$\n | $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$$$$$$/\n |__/  |__/|__/  |__/ \______/ |__/  \__/|________/|_______/", 'green')
        print ("logout\nSaving session...\n...copying shared history...\n...saving history...truncating history files...\n...completed.\nDeleting expired sessions...33 completed.")
        print colored("FILE SYSTEM ENCRYPTED, PLEASE ENTRER PASSWORD", 'red')
        temp=raw_input("Press enter to continue..")
        print colored("Il semblerait que quelquechose se soit très mal passé..\nVoyons si il est possible de débloquer ça..\n", 'yellow')
        number=randint(0,9999)
        mastermind.play(str(number))
        print colored("Filesystem UNLOCKED\n", 'green')
