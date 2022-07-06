from src.games import *
from src.games2 import *
from os import system, name
import time
import pickle as pkl

def save_replay():
    filename=input("Filename to store replay: ")
    file=open('replays/'+filename,'wb')
    pkl.dump(replayfinal,file)
    file.close()
flag=0
enter1=0
enter2=0
replayfinal=[]

def withking1():
    locationC=[18,46,5,33,24,4,9,61]
    game=Game(locationC)
    global enter1
    global replayfinal
    while(True):
        if enter1==1:
            break
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game.king.kingMove(game)
        if (key == 'q'):
            flag=1
            break
        game.king.cannonattackK(game)
        game.king.wizardattackK(game)
        #game.king.cannon2attackK(game)
        game.king.updateking()
        game.render()
        buildcheck=game.checkbuildings()
        if(buildcheck==True):
            enter1=1
            withking2()
        troopcheck=game.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    replayfinal.extend(game.replays)
    #save_replay()

def withking2():
    #locationC=[18,46,5,33,24,4,9,61,12,43,12,36,16,40,8,40]
    locationC=[18,46,5,33,24,4,9,61,12,43,12,36]
    game=Game(locationC)
    global enter2
    global replayfinal
    while(True):
        if enter2==1:
            break
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game.king.kingMove(game)
        if (key == 'q'):
            flag=1
            break
        game.king.cannonattackK(game)
        game.king.wizardattackK(game)
        #game.king.cannon2attackK(game)
        game.king.updateking()
        game.render()
        buildcheck=game.checkbuildings()
        if(buildcheck==True):
            enter2=1
            withking3()
        troopcheck=game.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    replayfinal.extend(game.replays)

def withking3():
    #locationC=[18,46,5,33,24,4,9,61,12,43,12,36,16,40,8,40,11,62,50,50,22,39,1,55]
    locationC=[18,46,5,33,24,4,9,61,12,43,12,36,16,40,8,40]
    game=Game(locationC)
    global replayfinal
    while(True):
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game.king.kingMove(game)
        if (key == 'q'):
            flag=1
            break
        game.king.cannonattackK(game)
        game.king.wizardattackK(game)
        #game.king.cannon2attackK(game)
        game.king.updateking()
        game.render()
        buildcheck=game.checkbuildings()
        if(buildcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Victory")
            break
        troopcheck=game.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    replayfinal.extend(game.replays)

def withqueen1():
    locationC=[18,46,5,33,24,4,9,61]
    game2=Game2(locationC)
    global enter1
    global replayfinal
    while(True):
        if enter1==1:
            break
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game2.queen.queenMove(game2)
        if (key == 'q'):
            flag=1
            break
        game2.queen.cannonattackQ(game2)
        game2.queen.wizardattackQ(game2)
        game2.queen.updatequeen()
        game2.render()
        buildcheck=game2.checkbuildings()
        if(buildcheck==True):
            enter1=1
            withqueen2()
        troopcheck=game2.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    #save_replay()
    replayfinal.extend(game2.replays)

def withqueen2():
    locationC=[18,46,5,33,24,4,9,61,12,43,12,36]
    game2=Game2(locationC)
    global enter2
    global replayfinal
    while(True):
        if enter2==1:
            break
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game2.queen.queenMove(game2)
        if (key == 'q'):
            flag=1
            break
        game2.queen.cannonattackQ(game2)
        game2.queen.wizardattackQ(game2)
        game2.queen.updatequeen()
        game2.render()
        buildcheck=game2.checkbuildings()
        if(buildcheck==True):
            enter2=1
            withqueen3()
        troopcheck=game2.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    replayfinal.extend(game2.replays)

def withqueen3():
    locationC=[18,46,5,33,24,4,9,61,12,43,12,36,16,40,8,40]
    game2=Game2(locationC)
    global replayfinal
    while(True):
        global flag
        #print("\033[%d;%dH" % (0, 0))
        #game.fillobjects()
        key=game2.queen.queenMove(game2)
        if (key == 'q'):
            flag=1
            break
        game2.queen.cannonattackQ(game2)
        game2.queen.wizardattackQ(game2)
        game2.queen.updatequeen()
        game2.render()
        buildcheck=game2.checkbuildings()
        if(buildcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Victory")
            break
        troopcheck=game2.checktroop()
        if(troopcheck==True):
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            print("Defeat")
            break
    replayfinal.extend(game2.replays)

x=input("Type with what you want to play with (King or Queen): ")

if (x=="King"):
    withking1()
elif (x=="Queen"):
    withqueen1()
else:
    print("Restart game and type correct name")

if flag==0:
    save_replay()

if flag==1:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')