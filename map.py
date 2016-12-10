# coding: utf8
'''
Main map
'''
import tty, sys, termios, time, os, select
from strings import *
import UI, IO, controls, hanoi, cactus, mastermind
import curses, platform



GRAVITY=False
list_cactus, plateau =[], []
avancement, iteration_compteur, moves_in_air, score = 0, 0, 0, 0
repertoire=os.path.dirname(os.path.abspath(__file__))

def get_score():
    global score
    return score



def change_map(map, x_dest, y_dest, plateau, possible_objectives=[], test=False):
    if(not(os.path.isfile(repertoire+'/'+map))):
        if(os.path.isfile(repertoire+'/'+map)):
            change_map('map.txt', 27, 3, plateau)
            return 'main.txt'
        else:
            print 'Error: AT LEAST 2 PROGRAM FILES ARE MISSING, PLEASE RE-DOWNLOAD THE GAME'
            return 'main.txt'
    #Checks for achivements to pass
    else:
        temp_level=get_current_level()
        if(temp_level in possible_objectives):
            increase_level()
            IO.save_progress()

        #Move, clear the list, write position, display
        x,y=controls.get_player_pos(plateau)

        UI.clear(map, plateau)
        UI.load_board(map, plateau)
        UI.write_player(x_dest, y_dest, plateau)
        if(test==False):
            UI.display_map(plateau)
        return map



def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])



def init(tutorial=False):

    reload(sys)
    sys.setdefaultencoding('utf8')
    tty.setraw(sys.stdin)


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
    if(not tutorial):
        UI_file=change_map("map.txt", 40, 15, plateau, [9])
    else:
        UI_file=change_map('tutorial.txt', 7, 22, plateau)



    #Set text entry
    set_orig_settings()
    orig_settings = get_orig_settings()

    palier=19
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
                elif (x==1 and y==3):
                    UI_file=change_map('museum.txt', 4, 23, plateau)
                elif (x==1 and y==2):
                    UI_file=change_map('castle_1.txt', 6, 26, plateau)

                elif(x==2 and y==1):
                    UI_file=change_map('iStore.txt', 57, 21, plateau)
                elif (x==2 and y==2):
                    UI_file=change_map('bar.txt', 53, 20, plateau)

                elif (x==3 and y==3):
                    UI_file=change_map('metro.txt', 75, 7, plateau, [5])

                elif (x==4 and y==1):
                    UI_file=change_map('airport.txt', 77, 23, plateau)
                elif (x==4 and y==2):
                    UI_file=change_map('steve_home.txt', 53, 22, plateau, [4])

                elif(x==5 and y==1):
                    UI_file=change_map('post_office.txt', 54, 20, plateau)
                elif(x==5 and y==3):
                    UI_file=change_map('arcade.txt', 70, 19, plateau)


            elif(UI_file=="post_office.txt"):
                if(x>=59 and y>=17): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 58, 6, plateau)

            elif(UI_file=="arcade.txt"):
                if(x>=92 and y>=17): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 58, 14, plateau)

                if(x>=73 and y<=12): #gravity platform

                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
                    print 'GRAVITY PLATFORM'
                    print '• Press SPACE to jump'
                    print '• Score at least 20 to pass'
                    list_obstacles, avancement =platform.init()
                    UI_file=change_map('platform.txt', 13, 19, plateau)

                elif(x>=48 and y<=12): #mastermind
                    x,y=controls.get_player_pos(plateau)
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
                    mastermind.load()
                    tty.setraw(sys.stdin)
                    UI_file=change_map('arcade.txt', x, y, plateau)

                elif(x>=25 and y<=12):
                    #UI_file=change_map('jump.txt', 40, 13, plateau)
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, get_orig_settings())
                    print 'JUMP !'
                    print '• Press SPACE to jump'
                    print '• Score at least 200 to pass'
                    list_cactus, avancement =cactus.init()
                    UI_file=change_map('jump.txt', 5, 20, plateau)
                elif(x>=4 and y<=12):
                    hanoi.play(4, plateau)


            elif(UI_file=="bar.txt"):
                if(x>=59 and y>=18):
                    UI_file=change_map('map.txt', 27, 10, plateau)

            elif(UI_file=="iStore.txt"):
                if(x>=63 and y>=21): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 27, 3, plateau)

            elif(UI_file=="iSecure.txt"):
                if(x>=60 and y>=21): #Joueur sur la case de sortie
                    UI_file=change_map('map.txt', 15, 3, plateau)

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
                    UI_file=change_map("map.txt", 42, 10, plateau)

            elif(UI_file=="metro.txt"):
                if(x>=81 and y<=9):
                    UI_file=change_map("map.txt", 39, 17, plateau, [9])
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
                    UI_file=change_map("map.txt", 15, 17, plateau)
                elif(x>=94 and y>=22):
                    list_cactus, avancement =cactus.init()
                    UI_file=change_map('jump.txt', 5, 20, plateau)

            elif(UI_file=='airport.txt'):
                if(x>=81 and y>=21):
                    UI_file=change_map('map.txt', 42, 3, plateau)
                elif(x>=81 and y<=12):
                    UI_file=change_map('credits.txt', 8, 23, plateau)
            elif(UI_file=='credits.txt'):
                if(x>=81 and y>=21):
                    UI_file=change_map('map.txt', 40, 15, plateau)

            elif(UI_file=='tutorial.txt'):
                if(x>=81 and y>=20):
                    break


        if (strcmp(entry, 'M') or strcmp(entry, 'm')):
            score=0
            avancement=0
            UI_file=change_map("map.txt", 40, 15, plateau)

        #Log
        if (strcmp(entry, 'L') or strcmp(entry, 'l')):
            print controls.get_player_pos(plateau)

        if (strcmp(entry, 'D') or strcmp(entry, 'd')):
            if(UI_file=="platform.txt"):
                controls.request_move(2, 0, plateau, UI_file)
            else:
                controls.request_move(1, 0, plateau, UI_file)
            UI.display_map(plateau)

        if (strcmp(entry, 'Z') or strcmp(entry, 'z') or strcmp(entry, '\x1b[A')):
            controls.request_move(0, -1, plateau, UI_file)
            UI.display_map(plateau)

        if (strcmp(entry, 'Q') or strcmp(entry, 'q')):
            if(UI_file=="platform.txt"):
                controls.request_move(-2, 0, plateau, UI_file)
            else:
                controls.request_move(-1, 0, plateau, UI_file)
            UI.display_map(plateau)

        if (strcmp(entry, 'S') or strcmp(entry, 's')):
            controls.request_move(0, 1, plateau, UI_file)
            UI.display_map(plateau)

        if (strcmp(entry, 'G') or strcmp(entry, 'g') and score==0):
            if GRAVITY:
                GRAVITY=False
                moves_in_air=0
            else:
                GRAVITY=True
                moves_in_air=0

        if(strcmp(entry, 'I') or strcmp(entry, 'i')):
            obj=IO.load_objective()
            nombre_obj=len(obj['objectives'][IO.get_language()])
            if(get_current_level()<nombre_obj-1):
                increase_level()
                IO.save_progress()
                x,y=controls.get_player_pos(plateau)
                UI_file=change_map(UI_file, x, y, plateau)


        #print entry

        if (strcmp(entry, ' ')):

            x,y=controls.get_player_pos(plateau)

            if(UI_file=='jump.txt'):
                if(strcmp(plateau[y+2][x], '=')):
                    controls.request_move(0, -6, plateau, UI_file)


        if (strcmp(entry, 'DOWN') and GRAVITY):
            controls.request_move(0,1, plateau, UI_file)
            if(UI_file=='platform.txt'):
                if(strcmp(plateau[y+2][x], '=') or strcmp(plateau[y+2][x+1], '=') or strcmp(plateau[y+2][x-1], '=')):
                    controls.request_move(0, -6, plateau, UI_file)





        #Die
        if(UI_file=="jump.txt" and GRAVITY):
            x,y=controls.get_player_pos(plateau)
            if(strcmp(plateau[y+2][x], '|') or strcmp(plateau[y+1][x], '|') or strcmp(plateau[y][x+2], '|') or strcmp(plateau[y+1][x+2], '|') ):
                GRAVITY=False
                iteration_compteur=0
                score=0

                if(score >=200):
                    print 'Congrats, you reached the target score !'
                print 'Press Q to exit, any other key to retry :'
                entry=sys.stdin.read(1)[0]
                if(entry=='Q' or entry=="q"):
                    if(score >=200):
                        UI_file=change_map("map.txt", 40, 15, plateau, [10])
                    else:
                        UI_file=change_map("map.txt", 40, 15, plateau)

                else:
                    UI_file=change_map(UI_file, 5, 20, plateau)
                    GRAVITY=True


        elif(UI_file=="platform.txt" and GRAVITY):
            x,y=controls.get_player_pos(plateau)
            if(y>palier):
                GRAVITY=False
                score=0
                avancement=0

                if(score >=20):
                    print 'Congrats, you reached the target score !'
                print 'Press Q to exit, any other key to retry :'
                entry=sys.stdin.read(1)[0]
                if(entry=='Q' or entry=="q"):
                    if(score >=200):
                        list_obstacles, avancement = platform.init(False, list_obstacles, map, avancement)
                        UI_file=change_map("platform.txt", 13, 19, plateau, [10])
                    else:
                        UI_file=change_map("map.txt", 40, 15, plateau)
                else:
                    UI_file=change_map(UI_file, 13, 20, plateau)
                    GRAVITY=True







        entry='OUT'
        if strcmp(UI_file, 'jump.txt'):
            if isData():
                entry=sys.stdin.read(1)[0]
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
                iteration_compteur+=1
                if GRAVITY:
                    score+=1
                if(iteration_compteur>=4):
                    entry='DOWN'
                    iteration_compteur=0


            exec_time=float(time.time()-t0)
            if(0.1-exec_time>0):
                time.sleep(0.1-exec_time)


        elif strcmp(UI_file, 'platform.txt'):
            if isData():
                entry=sys.stdin.read(1)[0]
                iteration_compteur+=1
                if GRAVITY:
                    score+=1
                if(iteration_compteur>=4):
                    entry='DOWN'
                    iteration_compteur=0
            else:
                x,y=controls.get_player_pos( plateau)
                print x,y
                if(y<palier-8 and (plateau[y+2][x]=='=' or plateau[y+2][x+1]=='=' or plateau[y+2][x-1]=='=')):
                    avancement+=1

                list_obstacles, avancement = platform.init(False, list_obstacles, map, avancement)
                print avancement
                UI_file=change_map(UI_file, x, y, plateau)
                iteration_compteur+=1
                if GRAVITY:
                    score+=1
                if(iteration_compteur>=4):
                    entry='DOWN'
                    iteration_compteur=0


            exec_time=float(time.time()-t0)
            if(0.07-exec_time>0):
                time.sleep(0.07-exec_time)


        else:
            entry=sys.stdin.read(1)







        #For debug, display time between moves
        #print time.time()-t0
