from os import system, name
from src.barbarian import Barbarian
from src.archer import Archer
from src.balloon import Balloon
from src.village import *
from colorama import Fore, Back, Style
import time
import sys
from src.queen import *
import math

#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL + 'Shubh')
#print('back to normal now')
#print(Fore.RED + 'some red text') self.setup[self.cannon.x1][self.cannon.y1]=self.cannon.color
        #self.setup[self.cannon.x2][self.cannon.y2]=self.cannon.color


class Game2():
    def __init__(self,locationC):
        self.rows=25
        self.cols=80
        self.defaultColor=Back.WHITE+' '+Style.RESET_ALL
        self.frameRate=1/60
        self.queen=Queen(0,0)
        self.townhall=[]
        self.walls=[]
        self.huts=[]
        self.replays=[]
        self.barbarians=[]
        self.archers=[]
        self.balloons=[]
        #self.cannon1=Cannon(18,46)
        #self.cannon2=Cannon(5,33)
        self.cannons=[]
        self.wizards=[]
        k=0
        while k<len(locationC)/2:
            self.cannons.append(Cannon(locationC[k],locationC[k+1]))
            k=k+2
        while k<len(locationC):
            self.wizards.append(Wizard(locationC[k],locationC[k+1]))
            k=k+2
        self.setup=[]
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        for i in range(6,18):
            wall1=Walls(i,34)
            wall2=Walls(i,46)
            self.walls.append(wall1)
            self.walls.append(wall2)
        for i in range(34,46):
            wall1=Walls(6,i)
            wall2=Walls(18,i)
            self.walls.append(wall1)
            self.walls.append(wall2)

        self.huts.append(Huts(8,36))
        self.huts.append(Huts(10,64))
        self.huts.append(Huts(14,36))
        self.huts.append(Huts(16,44))
        self.huts.append(Huts(22,4))

        self.barbarians.append(Barbarian(10,0))
        self.barbarians.append(Barbarian(23,75))
        self.barbarians.append(Barbarian(5,75))

        self.archers.append(Archer(3,65))
        self.archers.append(Archer(8,1))
        self.archers.append(Archer(16,70))

        self.balloons.append(Balloon(24,65))
        self.balloons.append(Balloon(0,67))
        self.balloons.append(Balloon(6,1))

        for i in range(10,14):
            for j in range(38,41):
                self.townhall.append(TownHall(i,j))


            ##print("\033[%d;%dH" % (0, 0))
            #self.render()
            ##time.sleep(self.frameRate)
    
    def checkbuildings(self):
        for huts in self.huts:
            if(huts.health>0):
                return False
        
        for townhall in self.townhall:
            if(townhall.health>0):
                return False
        
        return True

    def checktroop(self):
        if self.queen.health>0:
            return False
        for barbarian in self.barbarians:
            if(barbarian.health>0):
                return False
        for archers in self.archers:
            if(archers.health>0):
                return False
        for balloons in self.balloons:
            if(balloons.health>0):
                return False
        
        return True

    def render(self):
        print("\033[%d;%dH" % (0, 0))
        self.setup = []
        for i in range(self.rows):
            col=[]
            for j in range(self.cols):
                col.append(Back.WHITE+' '+Style.RESET_ALL)
            self.setup.append(col)

        k=0
        for i in range(10,14):
            for j in range(38,41):
                self.setup[i][j]=self.townhall[k].color
                k=k+1
                
        

        for i in range(6,18):
            for wall in self.walls:
                if(wall.x==i and wall.y==34):
                    self.setup[i][34]=wall.color
                if(wall.x==i and wall.y==46):
                    self.setup[i][46]=wall.color

        for i in range(34,46):
            for wall in self.walls:
                if(wall.x==6 and wall.y==i):
                    self.setup[6][i]=wall.color
                if(wall.x==18 and wall.y==i):
                    self.setup[18][i]=wall.color
        
        # self.setup[self.cannon1.x][self.cannon1.y]=self.cannon1.color
        # self.setup[self.cannon2.x][self.cannon2.y]=self.cannon2.color
        for cannons in self.cannons:
            self.setup[cannons.x][cannons.y]=cannons.color

        for wizards in self.wizards:
            self.setup[wizards.x][wizards.y]=wizards.color

        for huts in self.huts:
            self.setup[huts.x][huts.y]=huts.color

        for barbarians in self.barbarians:
            self.setup[barbarians.x][barbarians.y]=barbarians.color
        
        for archers in self.archers:
            self.setup[archers.x][archers.y]=archers.color

        for balloons in self.balloons:
            self.setup[balloons.x][balloons.y]=balloons.color

        self.setup[self.queen.x][self.queen.y]=self.queen.color

        output=''

        for i in range(self.rows):
            for j in range(self.cols):
                output=output+self.setup[i][j]
            output=output+'\n'

        output=output+'\n'
        output=output+'queenS HEALTH: '
        for i in range(math.floor(self.queen.health)):
            output=output+'|'
        
        sys.stdout.write(output)
        self.replays.append(output)

        ##time.sleep(0.25)

        #time.sleep(self.frameRate)
        
