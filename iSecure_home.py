# coding: utf8
from termcolor import colored
import time
import map
import IO

def ls():
    print colored("Steve est connecté, 'ls' permet de lister les fichiers, voyons ce qu'il y a sur ce serveur .. ", 'yellow')
    print("Steve@iCorporate: ls ")
    print ('Entrer to continue')
    raw_input('')
    print "employees, contracts, offices, devices, REMOTE_FOLDER"
    mv()

def mv():
    print colored("\nOk, je dois déplacer tout ces fichiers vers le serveur distant.", 'yellow')
    print 'mv ./* ./REMOTE_FOLDER'
    raw_input('')
    sudo()

def sudo():
    print colored("Error: unsufficient permissions, make you you have super-user rights", 'red')
    print colored("Ohoh, en tant qu'administrateur, cela marchera mieux", 'yellow')
    print 'sudo mv ./* ./REMOTE_FOLDER'
    raw_input("")
    raw_input('Password: ************')
    print "Processing ..."
    time.sleep(1)
    print "Processing ..."
    time.sleep(1)
    for i in range(0, 50):
        print colored("INTERNAL ERROR", 'red')
        time.sleep(0.01)
    chat()


def chat():
    print '<Hello Steve'
    time.sleep(0.5)
    print "..."
    time.sleep(0.5)
    print "..."
    time.sleep(1)
    print '<Are you ready ?'
    time.sleep(0.5)
    print '>Yes'
    print '<Let\'s get started'
    time.sleep(0.5)
    print '<Download the package at 188.234.211.22/mdd.zip'
    time.sleep(0.5)
    print 'wget 188.234.211.22/mdd.zip'
    raw_input('')
    for i in range(10):
        print '='*i+'>'
    print 'Downloaded 23456Kb'
    unzip()


def unzip():
    print colored('Unzip the file', 'yellow')
    print 'unzip ./mdd.zip'
    raw_input('')
    print 'Done.'
    execute()

def execute():
    print colored('Launch the script', 'yellow')
    print './mdd/payload.sh'
    raw_input("")
    print "Processing ."
    time.sleep(0.5)
    print "Processing .."
    time.sleep(0.5)
    print "Processing ..."
    time.sleep(0.5)
    print 'Done.'
    time.sleep(0.5)
    print  'Shuting down..'
    time.sleep(1)


def init():
    print colored(" /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$\n| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$__  $$\n | $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$      | $$  \ $$\n| $$$$$$$$| $$$$$$$$| $$      | $$$$$/  | $$$$$   | $$  | $$\n | $$__  $$| $$__  $$| $$      | $$  $$  | $$__/   | $$  | $$\n | $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$\n | $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$$$$$$/\n |__/  |__/|__/  |__/ \______/ |__/  \__/|________/|_______/", 'green')
    print colored("Steve travaille chez AllSecure, une grande société spécialisée dans le sécurité informatique. Il doit mettre à jour l'un des vieux serveur de la société. \n", 'yellow')
    null=raw_input("Entrée pour continuer (pour chaque étape de cette histoire)")
    ls()
