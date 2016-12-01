# coding: utf8
#Carte principale
import tty, signal, sys, termios, time, os, termcolor, base64, hanoi
from strings import *
import UI, IO, controls, map, iSecure_home

reload(sys)
sys.setdefaultencoding('utf8')

########################
####DÉBUT DES TESTS#####
########################

if __name__ == '__main__':
    print '****TESTING*****'
    plate=[]
    for j in range(30):
        plate.append([' '] * 100) #3 lignes, 20 caracteres

    if(not(strcmp('a','a'))):
        print 'strcmp test error'

    UI.write_player(15, 15, plate)
    #15,15 centre (ventre)
    #14,14 tete
    if(plate[14][15]!='☺'):
        print("write_player() test error")

    coordonnees=controls.get_player_pos(plate)
    if(not([coordonnees[0]==15 and coordonnees[1]==15])):
        print 'controls.get_player_pos() test error'

    if(not(strcmp(get_head_symbol(), '☺'))):
        print 'get_head_symbol() test error'

    UI.erase_player(15, 15, plate)
    if(plate[15][15]=='☺'):
        print("erase_player() test error")

    plate=UI.load_board('iSecure.txt', plate)
    if(plate[11][32]!='@'):
        print("load_board() test error")


    plate=UI.load_board('map.txt', plate)
    UI.write_player(15, 15, plate)

    if(not(UI.get_map_position(plate)==[1, 3])):
        print 'UI.get_map_position() test error'


    if(not (strcmp('test', 'test'))):
        print ("strcmp() test error")

    json=IO.load_objective()
    result=True
    try:
        if json['language'] and type(json['objectives'])==dict:
            result=True
        else:
            result=False
    except KeyError:
        result=False

    if(not(result)):
        print 'IO.load_objective() test error'


    IO.set_language('FR')
    if(json['language']!='FR'):
            print 'IO.set_language test errror'

    if(not(strcmp(IO.get_language(),'FR'))):
        print 'IO.get_language() test error'

    #On prend le niveau précedement enregistré
    json=IO.load_objective()
    niveau=''
    try:
        if json['progress']:
            niveau=json['progress']
        else:
            niveau=''
    except KeyError:
        niveau=''


    set_level(6)
    if(get_current_level()!=6):
        print 'get_current_level test error'

    IO.save_progress()
    json=IO.load_objective()
    if(not(strcmp(json['progress'], base64.b64encode('6')))):
        print 'IO.save_progress test error'

    increase_level()
    if(get_current_level()!=7):
        print 'increase_level test error'

    init_level()
    if(get_current_level()!=0):
        print 'init_level test error'

    IO.erase_progress()
    json=IO.load_objective()
    erase_progress_result=True
    try:
        if json['progress']:
            erase_progress_result=False
        else:
            erase_progress_result=True
    except KeyError:
        erase_progress_result=True

    if(not(erase_progress_result)):
        print 'IO.erase_progress test error'


    #On initialise le niveau
    if(niveau!=''):
        set_level(int(base64.b64decode(niveau)))
        IO.save_progress()
        json=IO.load_objective()
        if(strcmp(json['progress'], base64.b64encode(niveau))):
            print 'IO.save_progress test error'

    hanoe=hanoi.init(5)
    if(not(hanoe[0][3]==7 and hanoe[1][1]==0)):
            print 'hanoi.init() test error'


    #Test request_move
    UI.write_player(15,15, plate)
    controls.request_move(1,0,plate, 'map.txt')
    position=controls.get_player_pos(plate)
    if not(position[0]==16 and position[1]==15):
        print 'controls.request_move() test error'

    #Test move_player
    controls.move_player(1, 0, plate, 'map.txt')
    if(plate[14][16]==get_head_symbol()):
        print 'controls.move_player() test error'


    #Test check_top_middle_bottom
    #Déplacement invalide
    position=controls.get_player_pos(plate)
    y=0
    x=-1
    top=plate[position[1]+y-1][position[0]+x]
    left=plate[position[1]+y][position[0]+x-1]
    right=plate[position[1]+y][position[0]+x+1]

    if(position[1]+y+1<len(plate)):
        bottom_left=plate[position[1]+y+1][position[0]+x-1]
        bottom_right=plate[position[1]+y+1][position[0]+x+1]
    else:
        bottom_right=bottom_left='False'


    free=controls.check_top_middle_bottom(x, y, top, right, left, bottom_right, bottom_left, ['@', ' ', '&'])
    if(free):
        print 'controls.check_top_middle_bottom test error()'

    params=termios.tcgetattr(sys.stdin)
    set_orig_settings()

    if(type(get_orig_settings()) != list):
        print 'get_orig_settings() test error'


    #Change map
    carte_test=map.change_map('airport.txt', 77, 23, plate,[] , True)
    position=controls.get_player_pos(plate)
    if not((carte_test=='airport.txt' and position[0]==77 and position[1]==23)):
        print 'map.change_map() test error'





########################
#####FIN DES TESTS######
########################

#initialisation
repertoire=os.path.dirname(os.path.abspath(__file__))
screen=[]
for j in range(23):
    screen.append([' '] * 100) #3 lignes, 20 caracteres

IO.load_objective()

def show_main_menu(a):
    UI_file='menu.txt'
    a=UI.load_board(UI_file, screen)
    UI.display_map(a)



def loop(screen):
    show_main_menu(screen)
    set_orig_settings()
    orig_settings = get_orig_settings()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())

    commande=""
    while commande != 'exit' : # ESC
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())

        commande=raw_input('root@188.166.172.81 : ')
        if(commande=="play"):
            a= IO.load_objective()
            if(not 'progress' in a):
                iSecure_home.init()
                IO.save_progress(True)

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

loop(screen)
