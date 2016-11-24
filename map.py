# coding: utf8
'''
Main map
'''
import tty, sys, termios, time, os, select, signal
from strings import *
import UI, IO, controls, jump, hanoi, cactus
import curses



GRAVITY=False
list_cactus, plateau =[], []
avancement, iteration_compteur, moves_in_air, score = 0, 0, 0, 0


def get_score():
    global score
    return score



def change_map(map, x_dest, y_dest, plateau, possible_objectives=[]):

    #Checks for achivements to pass
    temp_level=get_current_level()
    if(temp_level in possible_objectives):
        increase_level()
        IO.save_progress()

    #Move, clear the list, write position, display
    x,y=controls.get_player_pos(plateau)

    UI.clear(map, plateau)
    UI.load_board(map, plateau)
    UI.write_player(x_dest, y_dest, plateau)
    UI.display_map(plateau)
    return map


def interact():
	#gestion des evenement clavier
	#si une touche est appuyee
	if isData():
		c = sys.stdin.read(1)
		if c == '\x1b':         # x1b is ESC
			quitGame()
		return c

def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])



def init():

    reload(sys)
    sys.setdefaultencoding('utf8')
    tty.setraw(sys.stdin)

    repertoire=os.path.dirname(os.path.abspath(__file__))



    global GRAVITY
    global moves_in_air
    global plateau
    global list_cactus
    global avancement
    global iteration_compteur
    global score

    plateau=[]
    for j in range(31):
        plateau.append([' '] * 100) #3 lignes, 20 caracteres


    UI.write_player(0,0, plateau)
    UI_file=change_map("map.txt", 40, 15, plateau, [9])



    #Set text entry
    set_orig_settings()
    orig_settings = get_orig_settings()


    entry = ''
    while entry != '\x1b' : # ESC

        t0=time.time()

        if (strcmp(entry, 'E') or strcmp(entry, 'e')): #E provoque une action: changement de carte/interraction

            x,y=controls.get_player_pos(plateau)
            if(UI_file=="map.txt"):
                x,y=UI.get_map_position(plateau)
                #print x,y
                if (x==0 or y==0):
                    variable_inutile=0
                elif (x==1 and y==1):
                    UI_file=change_map('iSecure.txt', 55, 20, plateau, [0])
                elif (x==4 and y==2):
                    UI_file=change_map('steve_home.txt', 53, 22, plateau, [4])
                elif (x==3 and y==3):
                    UI_file=change_map('metro.txt', 75, 7, plateau, [5])
                elif (x==4 and y==3):
                    UI_file=change_map('void.txt', 20, 20, plateau)
                elif (x==1 and y==3):
                    UI_file=change_map('museum.txt', 4, 23, plateau)
                elif (x==4 and y==1):
                    UI_file=change_map('airport.txt', 77, 23, plateau)
                elif (x==3 and y==2):
                    #UI_file=change_map('jump.txt', 40, 13, plateau)
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
                    print '• Press SPACE to jump'
                    print '• Score at least 200 to pass'
                    list_cactus, avancement =cactus.init()
                    UI_file=change_map('jump.txt', 5, 20, plateau)
                elif(x==5 and y==1):
                    UI_file=change_map('post_office.txt', 54, 20, plateau)
                elif(x==2 and y==1):
                    UI_file=change_map('iStore.txt', 57,20, plateau)

            elif(UI_file=="post_office.txt"):
                if(x>=59 and y>=18): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 40, 18, plateau)

            elif(UI_file=="iStore.txt"):
                if(x>=63 and y>=21): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 40, 18, plateau)

            elif(UI_file=="iSecure.txt"):
                if(x>=60 and y>=21): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 40, 15, plateau)

                elif (x>=4 and x<=13 and y==11): #Joueur sur BOSS OFFICE
                    UI_file=change_map('boss_office.txt', 45, 18, plateau, [1])

            elif(UI_file=="boss_office.txt"):
                if(x>=59 and y>=18):
                    UI_file=change_map("iSecure.txt", 55, 20, plateau)

                if(x>=23 and x<=42 and y>=11 and y<=18):
                    UI_file=change_map("labyrinthe.txt", 70, 2,plateau, [2])

            elif(UI_file=="labyrinthe.txt"):
                if(x>=4 and y>=24):
                    UI_file=change_map("boss_office.txt", 45, 18,plateau, [3])
            elif(UI_file=="steve_home.txt"):
                if(x>=61 and y>=21):
                    UI_file=change_map("map.txt", 40, 15, plateau)

            elif(UI_file=="metro.txt"):
                if(x>=81 and y<=9):
                    UI_file=change_map("map.txt", 40, 15, plateau, [9])
                elif(x>=71 and y>=13):
                    UI_file=change_map("cctv.txt", 55, 16, plateau, [6])
            elif(UI_file=="cctv.txt"):
                if(x>=59 and y>=16):
                    UI_file=change_map("metro.txt", 50, 15, plateau)
                elif(x>=2 and x<=20 and y<=16):
                    hanoi.play(4, plateau)
                elif(x>=22 and x<=39 and y<=16):
                    hanoi.play(3, plateau)
            elif(UI_file=='museum.txt'):
                if((x>=82 and y<=3) or  (x<=3 and y>=23)):
                    UI_file=change_map("map.txt", 40, 15, plateau)
                elif(x>=94 and y>=22):
                    list_cactus, avancement =cactus.init()
                    UI_file=change_map('jump.txt', 5, 20, plateau)

            elif(UI_file=='airport.txt'):
                if(x>=81 and y>=21):
                    UI_file=change_map('map.txt', 40, 15, plateau)
                elif(x>=81 and y<=12):
                    UI_file=change_map('credits.txt', 8, 23, plateau)
            elif(UI_file=='credits.txt'):
                if(x>=81 and y>=21):
                    UI_file=change_map('map.txt', 40, 15, plateau)


        #print '--'+entry+'--'
        if (strcmp(entry, 'T') or strcmp(entry, 't')):
            jump.generatemap(plateau)

        if (strcmp(entry, 'M') or strcmp(entry, 'm')):
            UI_file=change_map("map.txt", 40, 15, plateau)

        #Log
        if (strcmp(entry, 'L') or strcmp(entry, 'l')):
            print controls.get_player_pos(plateau)

        if (strcmp(entry, 'D') or strcmp(entry, 'd')):
            controls.request_move(1, 0, plateau, UI_file)

        if (strcmp(entry, 'Z') or strcmp(entry, 'z') or strcmp(entry, '\x1b[A')):
            controls.request_move(0, -1, plateau, UI_file)

        if (strcmp(entry, 'Q') or strcmp(entry, 'q')):
            controls.request_move(-1, 0, plateau, UI_file)

        if (strcmp(entry, 'S') or strcmp(entry, 's')):
            controls.request_move(0, 1, plateau, UI_file)

        if (strcmp(entry, 'G') or strcmp(entry, 'g') and score==0):
            if GRAVITY:
                GRAVITY=False
                moves_in_air=0
            else:
                GRAVITY=True
                moves_in_air=0

        #print entry

        if (strcmp(entry, ' ')):
            #print 'AAA'
            print plateau[y+2][x]
            #print plateau
            x,y=controls.get_player_pos(plateau)

            if(strcmp(plateau[y+2][x], '=')):
                controls.request_move(0, -5, plateau, UI_file)


        if (strcmp(entry, 'DOWN') and GRAVITY):
            controls.request_move(0,1, plateau, UI_file)



        if(UI_file=="jump.txt" and GRAVITY):
            x,y=controls.get_player_pos(plateau)
            if(strcmp(plateau[y+2][x], '|') or strcmp(plateau[y+1][x], '|') or strcmp(plateau[y][x+2], '|') or strcmp(plateau[y+1][x+2], '|') ):
                GRAVITY=False


                if(score >=200):
                    print 'Congrats, you reached the target score !'
                print 'Press Q to exit, any other key to retry :'
                entry=sys.stdin.read(1)[0]
                if(entry=='Q' or entry=="q"):
                    if(score >=200):
                        UI_file=change_map("map.txt", 40, 15, plateau, [10])
                    else:
                        UI_file=change_map("map.txt", 40, 15, plateau)
                    score=0
                else:
                    score=0
                    UI_file=change_map(UI_file, 5, 20, plateau)
                    GRAVITY=True
                    iteration_compteur=0






        entry='OUT'
        if strcmp(UI_file, 'jump.txt'):
            if True:
                if isData():
                    entry=sys.stdin.read(1)[0]
                    if(UI_file=='jump.txt'):
                        iteration_compteur+=1
                        if GRAVITY:
                            score+=1
                        if(iteration_compteur>=4):
                            entry='DOWN'
                            iteration_compteur=0
                else:
                    x,y=controls.get_player_pos( plateau)
                    list_cactus, avancement = cactus.init(False, list_cactus, map, avancement)
                    UI_file=change_map(UI_file, x, y, plateau)
                    if(UI_file=='jump.txt'):
                        iteration_compteur+=1
                        if GRAVITY:
                            score+=1

                        if(iteration_compteur>=4):
                            entry='DOWN'
                            iteration_compteur=0


                exec_time=float(time.time()-t0)
                if(0.1-exec_time>0):
                    time.sleep(0.1-exec_time)
        else:
            entry=sys.stdin.read(1)







        #For debug, display time between moves
        #print time.time()-t0
