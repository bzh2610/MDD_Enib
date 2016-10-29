import random, os
import UI

repertoire=os.path.dirname(os.path.abspath(__file__))

def generatemap(plateau):

    #UI.clear('void.txt', plateau)

    for j in range (0, 28):
        print len(plateau[j]), j
        for i in range (0, 100):

            plateau[j][i]=' '

    index=0
    for j in range (0, 26):
        i=0
        while i<75:
            if(j==25):
                    index=random.randint(20,30)
                    plateau[j][i+index]='|'
                    #plateau[j][i+1+index]='|'
                    plateau[j-1][i+index]='|'
                    #plateau[j-1][i+1+index]='|'
                    i=i+index
            else:
                plateau[j][i]=' '
                i+=1


    with open(repertoire + "/void.txt", "w") as file:
        file.truncate()

        for j in range (0, 27):
            line=''
            for i in range (0, 100):
                if(j==25 and plateau[j][i]==' '):
                    plateau[j][i]='='
                line=line+plateau[j][i]
            file.write(line+"\n")
        file.close()
