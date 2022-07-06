from colorama import Fore, Back, Style
from src.input import *
import time

class King():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.damage=10
        self.health=100
        self.velocity=1

        self.color=Back.BLUE+Fore.BLACK+'K'+Style.RESET_ALL

        self.inputClass=Get()

    def updateking(self):
        if self.health==0:
            self.color=Back.WHITE+' '+Style.RESET_ALL

    def cannonattackB(self,game):
        for cannon in game.cannons:
            if cannon.health!=0:
                flag=0
                for i in range(3):
                    if((abs(cannon.x-game.barbarians[i].x)+abs(cannon.y-game.barbarians[i].y))<=cannon.range and time.time()-cannon.prevtime>1 and game.barbarians[i].health>0):
                        flag=1
                        game.barbarians[i].health=game.barbarians[i].health-cannon.damage
                        cannon.prevtime=time.time()
                        cannon.attack=True
                        cannon.update_col()
                    
                if flag==0:
                    cannon.attack=False
                    cannon.update_col()

    def cannonattackA(self,game):
        for cannon in game.cannons:
            if cannon.health!=0:
                flag=0
                for i in range(3):
                    if((abs(cannon.x-game.archers[i].x)+abs(cannon.y-game.archers[i].y))<=cannon.range and time.time()-cannon.prevtime>1 and game.archers[i].health>0):
                        flag=1
                        game.archers[i].health=game.archers[i].health-cannon.damage
                        cannon.prevtime=time.time()
                        cannon.attack=True
                        cannon.update_col()
                
                if flag==0:
                    cannon.attack=False
                    cannon.update_col()

    def wizardattackB(self,game):
        for wizard in game.wizards:
            if wizard.health!=0:
                flag=0
                for i in range(3):
                    if((abs(wizard.x-game.barbarians[i].x)+abs(wizard.y-game.barbarians[i].y))<=wizard.range and time.time()-wizard.prevtime>1 and game.barbarians[i].health>0):
                        flag=1
                        game.barbarians[i].health=game.barbarians[i].health-wizard.damage
                        wizard.prevtime=time.time()
                        wizard.attack=True
                        wizard.update_col()
                        if(abs(self.x-game.barbarians[i].x)<2 and abs(self.y-game.barbarians[i].y)<2):
                            self.health=self.health-wizard.damage
                            self.updateking()
                        for archers in game.archers:
                            if(abs(archers.x-game.barbarians[i].x)<2 and abs(archers.y-game.barbarians[i].y)<2):
                                archers.health=archers.health-wizard.damage
                                archers.update_col()
                        for balloons in game.balloons:
                            if(abs(balloons.x-game.barbarians[i].x)<2 and abs(balloons.y-game.barbarians[i].y)<2):
                                balloons.health=balloons.health-wizard.damage
                                balloons.update_col()
                    
                if flag==0:
                    wizard.attack=False
                    wizard.update_col()

    def wizardattackA(self,game):
        for wizard in game.wizards:
            if wizard.health!=0:
                flag=0
                for i in range(3):
                    if((abs(wizard.x-game.archers[i].x)+abs(wizard.y-game.archers[i].y))<=wizard.range and time.time()-wizard.prevtime>1 and game.archers[i].health>0):
                        flag=1
                        game.archers[i].health=game.archers[i].health-wizard.damage
                        wizard.prevtime=time.time()
                        wizard.attack=True
                        wizard.update_col()
                        for barbarians in game.barbarians:
                            if(abs(barbarians.x-game.archers[i].x)<2 and abs(barbarians.y-game.archers[i].y)<2):
                                barbarians.health=barbarians.health-wizard.damage
                                barbarians.update_col()
                        if(abs(self.x-game.archers[i].x)<2 and abs(self.y-game.archers[i].y)<2):
                            self.health=self.health-wizard.damage
                            self.updateking()
                        for balloons in game.balloons:
                            if(abs(balloons.x-game.archers[i].x)<2 and abs(balloons.y-game.archers[i].y)<2):
                                balloons.health=balloons.health-wizard.damage
                                balloons.update_col()
                if flag==0:
                    wizard.attack=False
                    wizard.update_col()


    def cannonattackK(self,game):
        for cannon in game.cannons:
            if cannon.health!=0:
                if((abs(cannon.x-self.x)+abs(cannon.y-self.y))<=cannon.range and time.time()-cannon.prevtime>1 and self.health>0):
                    self.health=self.health-cannon.damage
                    cannon.prevtime=time.time()
                    cannon.attack=True
                    cannon.update_col()
                else:
                    cannon.attack=False
                    cannon.update_col() 

    def wizardattackK(self,game):
        for wizard in game.wizards:
            if wizard.health!=0:
                if((abs(wizard.x-self.x)+abs(wizard.y-self.y))<=wizard.range and time.time()-wizard.prevtime>1 and self.health>0):
                    self.health=self.health-wizard.damage
                    wizard.prevtime=time.time()
                    wizard.attack=True
                    wizard.update_col()
                    for barbarians in game.barbarians:
                        if(abs(barbarians.x-self.x)<2 and abs(barbarians.y-self.y)<2):
                            barbarians.health=barbarians.health-wizard.damage
                            barbarians.update_col()
                    for archers in game.archers:
                        if(abs(archers.x-self.x)<2 and abs(archers.y-self.y)<2):
                            archers.health=archers.health-wizard.damage
                            archers.update_col()
                    for balloons in game.balloons:
                        if(abs(balloons.x-self.x)<2 and abs(balloons.y-self.y)<2):
                            balloons.health=balloons.health-wizard.damage
                            balloons.update_col()
                else:
                    wizard.attack=False
                    wizard.update_col()

    def wizardattackBl(self,game):
        for wizard in game.wizards:
            if wizard.health!=0:
                flag=0
                for i in range(3):
                    if((abs(wizard.x-game.balloons[i].x)+abs(wizard.y-game.balloons[i].y))<=wizard.range and time.time()-wizard.prevtime>1 and game.balloons[i].health>0):
                        flag=1
                        game.balloons[i].health=game.balloons[i].health-wizard.damage
                        wizard.prevtime=time.time()
                        wizard.attack=True
                        wizard.update_col()
                        for barbarians in game.barbarians:
                            if(abs(barbarians.x-game.balloons[i].x)<2 and abs(barbarians.y-game.balloons[i].y)<2):
                                barbarians.health=barbarians.health-wizard.damage
                                barbarians.update_col()
                        if(abs(self.x-game.balloons[i].x)<2 and abs(self.y-game.balloons[i].y)<2):
                            self.health=self.health-wizard.damage
                            self.updateking()
                        for archers in game.archers:
                            if(abs(archers.x-game.balloons[i].x)<2 and abs(archers.y-game.balloons[i].y)<2):
                                archers.health=archers.health-wizard.damage
                                archers.update_col()
                if flag==0:
                    wizard.attack=False
                    wizard.update_col()


    # def cannon1attackB(self,game):
    #     flag=0
    #     for i in range(3):
    #         if((abs(game.cannon1.x-game.barbarians[i].x)+abs(game.cannon1.y-game.barbarians[i].y))<=10 and time.time()-game.cannon1.prevtime>1 and game.barbarians[i].health>0):
    #             flag=1
    #             game.barbarians[i].health=game.barbarians[i].health-game.cannon1.damage
    #             game.cannon1.prevtime=time.time()
    #             game.cannon1.attack=True
    #             game.cannon1.update_col()
        
    #     if flag==0:
    #         game.cannon1.attack=False
    #         game.cannon1.update_col()

    # def cannon1attackK(self,game):
    #     if((abs(game.cannon1.x-self.x)+abs(game.cannon1.y-self.y))<=game.cannon1.range and time.time()-game.cannon1.prevtime>1 and self.health>0):
    #         self.health=self.health-game.cannon1.damage
    #         game.cannon1.prevtime=time.time()
    #         game.cannon1.attack=True
    #         game.cannon1.update_col()
    #     else:
    #         game.cannon1.attack=False
    #         game.cannon1.update_col()

    #         #else:
    #             #game.cannon1.attack=False
    #             #game.cannon1.update_col()
    #         #game.cannon1.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'C'+Style.RESET_ALL
    #     #game.cannon1.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL
    # def cannon2attackB(self,game):
    #     flag=0
    #     for i in range(3):
    #         if((abs(game.cannon2.x-game.barbarians[i].x)+abs(game.cannon2.y-game.barbarians[i].y))<=10 and time.time()-game.cannon2.prevtime>1 and game.barbarians[i].health>0):
    #             flag=1
    #             game.barbarians[i].health=game.barbarians[i].health-game.cannon2.damage
    #             game.cannon2.prevtime=time.time()
    #             game.cannon2.attack=True
    #             game.cannon2.update_col()
    #     if flag==0:    #else:
    #         game.cannon2.attack=False
    #         game.cannon2.update_col()

    # def cannon2attackK(self,game):
    #     if((abs(game.cannon2.x-self.x)+abs(game.cannon2.y-self.y))<=game.cannon2.range and time.time()-game.cannon2.prevtime>1 and self.health>0):
    #         self.health=self.health-game.cannon2.damage
    #         game.cannon2.prevtime=time.time()
    #         game.cannon2.attack=True
    #         game.cannon2.update_col()
    #     else:
    #        game.cannon2.attack=False
    #        game.cannon2.update_col()
        
    #         #game.cannon1.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'C'+Style.RESET_ALL
    #     #game.cannon1.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL

    def kingMove(self,game):
        key=input_to(self.inputClass)
        if(key=='w' and self.x>0 and game.setup[self.x-1][self.y]==game.defaultColor and game.setup[self.x-self.velocity][self.y]==game.defaultColor and self.health>0):
            self.x=self.x-self.velocity
        if(key=='a' and self.y>0 and game.setup[self.x][self.y-1]==game.defaultColor and game.setup[self.x][self.y-self.velocity]==game.defaultColor and self.health>0):
            self.y=self.y-self.velocity
        if(key=='s' and self.x<24 and game.setup[self.x+1][self.y]==game.defaultColor and game.setup[self.x+self.velocity][self.y]==game.defaultColor and self.health>0):
            self.x=self.x+self.velocity
        if(key=='d' and self.y<79 and game.setup[self.x][self.y+1]==game.defaultColor and game.setup[self.x][self.y+self.velocity]==game.defaultColor and self.health>0):
            self.y=self.y+self.velocity
        if(key==' ' and self.health>0):
            for walls in game.walls:
                if (abs(walls.x-self.x)<3 and abs(walls.y-self.y)<3):
                    walls.health=0
                    walls.update_col()
            for huts in game.huts:
                if(abs(huts.x-self.x)<3 and abs(huts.y-self.y)<3):
                    huts.health=huts.health-self.damage
                    huts.update_col()
            for townhall in game.townhall:
                if(abs(townhall.x-self.x)<3 and abs(townhall.y-self.y)<3):
                    townhall.health=townhall.health-self.damage
                    townhall.update_col()
        # if(key==' ' and game.setup[self.x+1][self.y]!=game.defaultColor):
        #     for walls in game.walls:
        #         if(walls.x==self.x+1 and walls.y==self.y):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game.huts:
        #         if(huts.x==self.x+1 and huts.y==self.y):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game.townhall:
        #         if(townhall.x==self.x+1 and townhall.y==self.y):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game.setup[self.x-1][self.y]!=game.defaultColor):
        #     for walls in game.walls:
        #         if(walls.x==self.x-1 and walls.y==self.y):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game.huts:
        #         if(huts.x==self.x-1 and huts.y==self.y):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game.townhall:
        #         if(townhall.x==self.x-1 and townhall.y==self.y):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game.setup[self.x][self.y+1]!=game.defaultColor):
        #     for walls in game.walls:
        #         if(walls.x==self.x and walls.y==self.y+1):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game.huts:
        #         if(huts.x==self.x and huts.y==self.y+1):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game.townhall:
        #         if(townhall.x==self.x and townhall.y==self.y+1):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game.setup[self.x][self.y-1]!=game.defaultColor):
        #     for walls in game.walls:
        #         if(walls.x==self.x and walls.y==self.y-1):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game.huts:
        #         if(huts.x==self.x and huts.y==self.y-1):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game.townhall:
        #         if(townhall.x==self.x and townhall.y==self.y-1):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        if(key=='r'):
            self.damage=2*self.damage
            self.velocity=2*self.velocity
            for barbarian in game.barbarians:
                barbarian.damage = 2*barbarian.damage
                barbarian.velocity=2*barbarian.velocity
            for archer in game.archers:
                archer.damage = 2*archer.damage
                archer.velocity=2*archer.velocity
            for balloon in game.balloons:
                balloon.damage = 2*balloon.damage
                balloon.velocity=2*balloon.velocity
        if(key=='h'):
            self.health=1.5*self.health
            if(self.health>100):
                self.health=100
            for barbarian in game.barbarians:
                barbarian.health=2*barbarian.health
                if(barbarian.health>100):
                    barbarian.health=100
            for balloon in game.balloons:
                balloon.health=2*balloon.health
                if(balloon.health>100):
                    balloon.health=100
            for archer in game.archers:
                archer.health=2*archer.health
                if(archer.health>100):
                    archer.health=100
        if (key=='1'):
            while game.barbarians[0].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.barbarians[0].x)+abs(walls.y-game.barbarians[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.barbarians[0].x)+abs(walls.y-game.barbarians[0].y))
                for huts in game.huts:
                    if((abs(huts.x-game.barbarians[0].x)+abs(huts.y-game.barbarians[0].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.barbarians[0].x)+abs(huts.y-game.barbarians[0].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.barbarians[0].x)+abs(townhall.y-game.barbarians[0].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.barbarians[0].x)+abs(townhall.y-game.barbarians[0].y))
                if game.barbarians[0].x<min_x:
                    game.barbarians[0].x=game.barbarians[0].x+1
                elif game.barbarians[0].x>min_x:
                    game.barbarians[0].x=game.barbarians[0].x-1
                else:
                    game.barbarians[0].x=game.barbarians[0].x
                if game.barbarians[0].y<min_y:
                    game.barbarians[0].y=game.barbarians[0].y+1
                elif game.barbarians[0].y>min_y:
                    game.barbarians[0].y=game.barbarians[0].y-1
                else:
                    game.barbarians[0].y=game.barbarians[0].y
                # game.barbarians[0].y=min_y
                # object.health=0
                for walls in game.walls:
                    if(game.barbarians[0].x==walls.x and game.barbarians[0].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.barbarians[0].x==huts.x and game.barbarians[0].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.barbarians[0].x==townhall.x and game.barbarians[0].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.barbarians[0].velocity)
                self.cannonattackB(game)
                self.wizardattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.barbarians[0].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break
        if (key=='2'):
            while game.barbarians[1].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.barbarians[1].x)+abs(walls.y-game.barbarians[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.barbarians[1].x)+abs(walls.y-game.barbarians[1].y))
                for huts in game.huts:
                    if((abs(huts.x-game.barbarians[1].x)+abs(huts.y-game.barbarians[1].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.barbarians[1].x)+abs(huts.y-game.barbarians[1].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.barbarians[1].x)+abs(townhall.y-game.barbarians[1].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.barbarians[1].x)+abs(townhall.y-game.barbarians[1].y))
                if game.barbarians[1].x<min_x:
                    game.barbarians[1].x=game.barbarians[1].x+1
                elif game.barbarians[1].x>min_x:
                    game.barbarians[1].x=game.barbarians[1].x-1
                else:
                    game.barbarians[1].x=game.barbarians[1].x
                if game.barbarians[1].y<min_y:
                    game.barbarians[1].y=game.barbarians[1].y+1
                elif game.barbarians[1].y>min_y:
                    game.barbarians[1].y=game.barbarians[1].y-1
                else:
                    game.barbarians[1].y=game.barbarians[1].y
                # game.barbarians[1].y=min_y
                # object.health=0
                for walls in game.walls:
                    if(game.barbarians[1].x==walls.x and game.barbarians[1].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.barbarians[1].x==huts.x and game.barbarians[1].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.barbarians[1].x==townhall.x and game.barbarians[1].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.barbarians[1].velocity)
                self.cannonattackB(game)
                self.wizardattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.barbarians[1].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break
        if (key=='3'):
            while game.barbarians[2].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.barbarians[2].x)+abs(walls.y-game.barbarians[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.barbarians[2].x)+abs(walls.y-game.barbarians[2].y))
                for huts in game.huts:
                    if((abs(huts.x-game.barbarians[2].x)+abs(huts.y-game.barbarians[2].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.barbarians[2].x)+abs(huts.y-game.barbarians[2].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.barbarians[2].x)+abs(townhall.y-game.barbarians[2].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.barbarians[2].x)+abs(townhall.y-game.barbarians[2].y))
                if game.barbarians[2].x<min_x:
                    game.barbarians[2].x=game.barbarians[2].x+1
                elif game.barbarians[2].x>min_x:
                    game.barbarians[2].x=game.barbarians[2].x-1
                else:
                    game.barbarians[2].x=game.barbarians[2].x
                if game.barbarians[2].y<min_y:
                    game.barbarians[2].y=game.barbarians[2].y+1
                elif game.barbarians[2].y>min_y:
                    game.barbarians[2].y=game.barbarians[2].y-1
                else:
                    game.barbarians[2].y=game.barbarians[2].y
                # game.barbarians[2].y=min_y
                # object.health=0
                for walls in game.walls:
                    if(game.barbarians[2].x==walls.x and game.barbarians[2].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.barbarians[2].x==huts.x and game.barbarians[2].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.barbarians[2].x==townhall.x and game.barbarians[2].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.barbarians[2].velocity)
                self.cannonattackB(game)
                self.wizardattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.barbarians[2].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break
        if (key=='4'):
            while game.archers[0].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.archers[0].x)+abs(walls.y-game.archers[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.archers[0].x)+abs(walls.y-game.archers[0].y))
                for huts in game.huts:
                    if((abs(huts.x-game.archers[0].x)+abs(huts.y-game.archers[0].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.archers[0].x)+abs(huts.y-game.archers[0].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.archers[0].x)+abs(townhall.y-game.archers[0].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.archers[0].x)+abs(townhall.y-game.archers[0].y))
                if game.archers[0].x<min_x:
                    game.archers[0].x=game.archers[0].x+1
                elif game.archers[0].x>min_x:
                    game.archers[0].x=game.archers[0].x-1
                else:
                    game.archers[0].x=game.archers[0].x
                if game.archers[0].y<min_y:
                    game.archers[0].y=game.archers[0].y+1
                elif game.archers[0].y>min_y:
                    game.archers[0].y=game.archers[0].y-1
                else:
                    game.archers[0].y=game.archers[0].y
                # game.archers[0].y=min_y
                # object.health=0
                for huts in game.huts:
                    if(abs(huts.x-game.archers[0].x)+abs(huts.y-game.archers[0].y)<game.archers[0].range and huts.health!=0):
                        huts.health=huts.health-game.archers[0].damage
                        huts.update_col()

                for townhall in game.townhall:
                    if(abs(townhall.x-game.archers[0].x)+abs(townhall.y-game.archers[0].y)<game.archers[0].range and townhall.health!=0):
                        townhall.health=townhall.health-game.archers[0].damage
                        townhall.update_col()

                for walls in game.walls:
                    if(game.archers[0].x==walls.x and game.archers[0].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.archers[0].x==huts.x and game.archers[0].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.archers[0].x==townhall.x and game.archers[0].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.archers[0].velocity)
                #self.cannonattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                self.cannonattackA(game)
                self.wizardattackA(game)
                game.archers[0].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break

        if (key=='5'):
            while game.archers[1].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.archers[1].x)+abs(walls.y-game.archers[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.archers[1].x)+abs(walls.y-game.archers[1].y))
                for huts in game.huts:
                    if((abs(huts.x-game.archers[1].x)+abs(huts.y-game.archers[1].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.archers[1].x)+abs(huts.y-game.archers[1].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.archers[1].x)+abs(townhall.y-game.archers[1].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.archers[1].x)+abs(townhall.y-game.archers[1].y))
                if game.archers[1].x<min_x:
                    game.archers[1].x=game.archers[1].x+1
                elif game.archers[1].x>min_x:
                    game.archers[1].x=game.archers[1].x-1
                else:
                    game.archers[1].x=game.archers[1].x
                if game.archers[1].y<min_y:
                    game.archers[1].y=game.archers[1].y+1
                elif game.archers[1].y>min_y:
                    game.archers[1].y=game.archers[1].y-1
                else:
                    game.archers[1].y=game.archers[1].y
                # game.archers[1].y=min_y
                # object.health=0
                for huts in game.huts:
                    if(abs(huts.x-game.archers[1].x)+abs(huts.y-game.archers[1].y)<game.archers[1].range and huts.health!=0):
                        huts.health=huts.health-game.archers[1].damage
                        huts.update_col()

                for townhall in game.townhall:
                    if(abs(townhall.x-game.archers[1].x)+abs(townhall.y-game.archers[1].y)<game.archers[1].range and townhall.health!=0):
                        townhall.health=townhall.health-game.archers[1].damage
                        townhall.update_col()

                for walls in game.walls:
                    if(game.archers[1].x==walls.x and game.archers[1].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.archers[1].x==huts.x and game.archers[1].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.archers[1].x==townhall.x and game.archers[1].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.archers[1].velocity)
                #self.cannonattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                self.cannonattackA(game)
                self.wizardattackA(game)
                game.archers[1].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break

        if (key=='6'):
            while game.archers[2].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.archers[2].x)+abs(walls.y-game.archers[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.archers[2].x)+abs(walls.y-game.archers[2].y))
                for huts in game.huts:
                    if((abs(huts.x-game.archers[2].x)+abs(huts.y-game.archers[2].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.archers[2].x)+abs(huts.y-game.archers[2].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.archers[2].x)+abs(townhall.y-game.archers[2].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.archers[2].x)+abs(townhall.y-game.archers[2].y))
                if game.archers[2].x<min_x:
                    game.archers[2].x=game.archers[2].x+1
                elif game.archers[2].x>min_x:
                    game.archers[2].x=game.archers[2].x-1
                else:
                    game.archers[2].x=game.archers[2].x
                if game.archers[2].y<min_y:
                    game.archers[2].y=game.archers[2].y+1
                elif game.archers[2].y>min_y:
                    game.archers[2].y=game.archers[2].y-1
                else:
                    game.archers[2].y=game.archers[2].y
                # game.archers[2].y=min_y
                # object.health=0
                for huts in game.huts:
                    if(abs(huts.x-game.archers[2].x)+abs(huts.y-game.archers[2].y)<game.archers[2].range and huts.health!=0):
                        huts.health=huts.health-game.archers[2].damage
                        huts.update_col()

                for townhall in game.townhall:
                    if(abs(townhall.x-game.archers[2].x)+abs(townhall.y-game.archers[2].y)<game.archers[2].range and townhall.health!=0):
                        townhall.health=townhall.health-game.archers[2].damage
                        townhall.update_col()

                for walls in game.walls:
                    if(game.archers[2].x==walls.x and game.archers[2].y==walls.y):
                        walls.health=0
                        walls.update_col()
                for huts in game.huts:
                    if(game.archers[2].x==huts.x and game.archers[2].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.archers[2].x==townhall.x and game.archers[2].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.archers[2].velocity)
                #self.cannonattackB(game)
                #self.cannon2attackB(game)
                # object.update_col()
                self.cannonattackA(game)
                self.wizardattackA(game)
                game.archers[2].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break

        if (key=='7'):
            while game.balloons[0].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[0].x)+abs(walls.y-game.balloons[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[0].x)+abs(walls.y-game.balloons[0].y))
                for cannons in game.cannons:
                    if((abs(cannons.x-game.balloons[0].x)+abs(cannons.y-game.balloons[0].y))<min and cannons.health>0):
                        min_x=cannons.x
                        min_y=cannons.y
                        object=cannons
                        min=(abs(cannons.x-game.balloons[0].x)+abs(cannons.y-game.balloons[0].y))
                for wizards in game.wizards:
                    if((abs(wizards.x-game.balloons[0].x)+abs(wizards.y-game.balloons[0].y))<min and wizards.health>0):
                        min_x=wizards.x
                        min_y=wizards.y
                        object=wizards
                        min=(abs(wizards.x-game.balloons[0].x)+abs(wizards.y-game.balloons[0].y))
                if game.balloons[0].x<min_x:
                    game.balloons[0].x=game.balloons[0].x+1
                elif game.balloons[0].x>min_x:
                    game.balloons[0].x=game.balloons[0].x-1
                else:
                    game.balloons[0].x=game.balloons[0].x
                if game.balloons[0].y<min_y:
                    game.balloons[0].y=game.balloons[0].y+1
                elif game.balloons[0].y>min_y:
                    game.balloons[0].y=game.balloons[0].y-1
                else:
                    game.balloons[0].y=game.balloons[0].y
                for cannons in game.cannons:
                    if(game.balloons[0].x==cannons.x and game.balloons[0].y==cannons.y):
                        cannons.health=0
                        cannons.update_col()
                for wizards in game.wizards:
                    if(game.balloons[0].x==wizards.x and game.balloons[0].y==wizards.y):
                        wizards.health=0
                        wizards.update_col()
                time.sleep(1/game.balloons[0].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[0].update_col()
                game.render()
                defensecheck=0
                for cannons in game.cannons:
                    if(cannons.health>0):
                        defensecheck=1
                for wizards in game.wizards:
                    if(wizards.health>0):
                        defensecheck=1

                if defensecheck==0:
                    break
            while game.balloons[0].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[0].x)+abs(walls.y-game.balloons[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[0].x)+abs(walls.y-game.balloons[0].y))
                for huts in game.huts:
                    if((abs(huts.x-game.balloons[0].x)+abs(huts.y-game.balloons[0].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.balloons[0].x)+abs(huts.y-game.balloons[0].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.balloons[0].x)+abs(townhall.y-game.balloons[0].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.balloons[0].x)+abs(townhall.y-game.balloons[0].y))
                if game.balloons[0].x<min_x:
                    game.balloons[0].x=game.balloons[0].x+1
                elif game.balloons[0].x>min_x:
                    game.balloons[0].x=game.balloons[0].x-1
                else:
                    game.balloons[0].x=game.balloons[0].x
                if game.balloons[0].y<min_y:
                    game.balloons[0].y=game.balloons[0].y+1
                elif game.balloons[0].y>min_y:
                    game.balloons[0].y=game.balloons[0].y-1
                else:
                    game.balloons[0].y=game.balloons[0].y
                # game.balloons[0].y=min_y
                # object.health=0
                # for walls in game.walls:
                #     if(game.balloons[0].x==walls.x and game.balloons[0].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game.huts:
                    if(game.balloons[0].x==huts.x and game.balloons[0].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.balloons[0].x==townhall.x and game.balloons[0].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.balloons[0].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[0].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break  

        if (key=='8'):
            while game.balloons[1].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[1].x)+abs(walls.y-game.balloons[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[1].x)+abs(walls.y-game.balloons[1].y))
                for cannons in game.cannons:
                    if((abs(cannons.x-game.balloons[1].x)+abs(cannons.y-game.balloons[1].y))<min and cannons.health>0):
                        min_x=cannons.x
                        min_y=cannons.y
                        object=cannons
                        min=(abs(cannons.x-game.balloons[1].x)+abs(cannons.y-game.balloons[1].y))
                for wizards in game.wizards:
                    if((abs(wizards.x-game.balloons[1].x)+abs(wizards.y-game.balloons[1].y))<min and wizards.health>0):
                        min_x=wizards.x
                        min_y=wizards.y
                        object=wizards
                        min=(abs(wizards.x-game.balloons[1].x)+abs(wizards.y-game.balloons[1].y))
                if game.balloons[1].x<min_x:
                    game.balloons[1].x=game.balloons[1].x+1
                elif game.balloons[1].x>min_x:
                    game.balloons[1].x=game.balloons[1].x-1
                else:
                    game.balloons[1].x=game.balloons[1].x
                if game.balloons[1].y<min_y:
                    game.balloons[1].y=game.balloons[1].y+1
                elif game.balloons[1].y>min_y:
                    game.balloons[1].y=game.balloons[1].y-1
                else:
                    game.balloons[1].y=game.balloons[1].y
                for cannons in game.cannons:
                    if(game.balloons[1].x==cannons.x and game.balloons[1].y==cannons.y):
                        cannons.health=0
                        cannons.update_col()
                for wizards in game.wizards:
                    if(game.balloons[1].x==wizards.x and game.balloons[1].y==wizards.y):
                        wizards.health=0
                        wizards.update_col()
                time.sleep(1/game.balloons[1].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[1].update_col()
                game.render()
                defensecheck=0
                for cannons in game.cannons:
                    if(cannons.health>0):
                        defensecheck=1
                for wizards in game.wizards:
                    if(wizards.health>0):
                        defensecheck=1

                if defensecheck==0:
                    break
            while game.balloons[1].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[1].x)+abs(walls.y-game.balloons[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[1].x)+abs(walls.y-game.balloons[1].y))
                for huts in game.huts:
                    if((abs(huts.x-game.balloons[1].x)+abs(huts.y-game.balloons[1].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.balloons[1].x)+abs(huts.y-game.balloons[1].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.balloons[1].x)+abs(townhall.y-game.balloons[1].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.balloons[1].x)+abs(townhall.y-game.balloons[1].y))
                if game.balloons[1].x<min_x:
                    game.balloons[1].x=game.balloons[1].x+1
                elif game.balloons[1].x>min_x:
                    game.balloons[1].x=game.balloons[1].x-1
                else:
                    game.balloons[1].x=game.balloons[1].x
                if game.balloons[1].y<min_y:
                    game.balloons[1].y=game.balloons[1].y+1
                elif game.balloons[1].y>min_y:
                    game.balloons[1].y=game.balloons[1].y-1
                else:
                    game.balloons[1].y=game.balloons[1].y
                # game.balloons[1].y=min_y
                # object.health=0
                # for walls in game.walls:
                #     if(game.balloons[1].x==walls.x and game.balloons[1].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game.huts:
                    if(game.balloons[1].x==huts.x and game.balloons[1].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.balloons[1].x==townhall.x and game.balloons[1].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.balloons[1].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[1].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break

        if (key=='9'):
            while game.balloons[2].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[2].x)+abs(walls.y-game.balloons[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[2].x)+abs(walls.y-game.balloons[2].y))
                for cannons in game.cannons:
                    if((abs(cannons.x-game.balloons[2].x)+abs(cannons.y-game.balloons[2].y))<min and cannons.health>0):
                        min_x=cannons.x
                        min_y=cannons.y
                        object=cannons
                        min=(abs(cannons.x-game.balloons[2].x)+abs(cannons.y-game.balloons[2].y))
                for wizards in game.wizards:
                    if((abs(wizards.x-game.balloons[2].x)+abs(wizards.y-game.balloons[2].y))<min and wizards.health>0):
                        min_x=wizards.x
                        min_y=wizards.y
                        object=wizards
                        min=(abs(wizards.x-game.balloons[2].x)+abs(wizards.y-game.balloons[2].y))
                if game.balloons[2].x<min_x:
                    game.balloons[2].x=game.balloons[2].x+1
                elif game.balloons[2].x>min_x:
                    game.balloons[2].x=game.balloons[2].x-1
                else:
                    game.balloons[2].x=game.balloons[2].x
                if game.balloons[2].y<min_y:
                    game.balloons[2].y=game.balloons[2].y+1
                elif game.balloons[2].y>min_y:
                    game.balloons[2].y=game.balloons[2].y-1
                else:
                    game.balloons[2].y=game.balloons[2].y
                for cannons in game.cannons:
                    if(game.balloons[2].x==cannons.x and game.balloons[2].y==cannons.y):
                        cannons.health=0
                        cannons.update_col()
                for wizards in game.wizards:
                    if(game.balloons[2].x==wizards.x and game.balloons[2].y==wizards.y):
                        wizards.health=0
                        wizards.update_col()
                time.sleep(1/game.balloons[2].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[2].update_col()
                game.render()
                defensecheck=0
                for cannons in game.cannons:
                    if(cannons.health>0):
                        defensecheck=1
                for wizards in game.wizards:
                    if(wizards.health>0):
                        defensecheck=1

                if defensecheck==0:
                    break
            while game.balloons[2].health>0:
                min=1000
                # for walls in game.walls:
                #     if((abs(walls.x-game.balloons[2].x)+abs(walls.y-game.balloons[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game.balloons[2].x)+abs(walls.y-game.balloons[2].y))
                for huts in game.huts:
                    if((abs(huts.x-game.balloons[2].x)+abs(huts.y-game.balloons[2].y))<min and huts.health>0):
                        min_x=huts.x
                        min_y=huts.y
                        object=huts
                        min=(abs(huts.x-game.balloons[2].x)+abs(huts.y-game.balloons[2].y))
                for townhall in game.townhall:
                    if((abs(townhall.x-game.balloons[2].x)+abs(townhall.y-game.balloons[2].y))<min and townhall.health>0):
                        min_x=townhall.x
                        min_y=townhall.y
                        object=townhall
                        min=(abs(townhall.x-game.balloons[2].x)+abs(townhall.y-game.balloons[2].y))
                if game.balloons[2].x<min_x:
                    game.balloons[2].x=game.balloons[2].x+1
                elif game.balloons[2].x>min_x:
                    game.balloons[2].x=game.balloons[2].x-1
                else:
                    game.balloons[2].x=game.balloons[2].x
                if game.balloons[2].y<min_y:
                    game.balloons[2].y=game.balloons[2].y+1
                elif game.balloons[2].y>min_y:
                    game.balloons[2].y=game.balloons[2].y-1
                else:
                    game.balloons[2].y=game.balloons[2].y
                # game.balloons[2].y=min_y
                # object.health=0
                # for walls in game.walls:
                #     if(game.balloons[2].x==walls.x and game.balloons[2].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game.huts:
                    if(game.balloons[2].x==huts.x and game.balloons[2].y==huts.y):
                        huts.health=0
                        huts.update_col()
                for townhall in game.townhall:
                    if(game.balloons[2].x==townhall.x and game.balloons[2].y==townhall.y):
                        townhall.health=0
                        townhall.update_col()
                time.sleep(1/game.balloons[2].velocity)
                self.wizardattackBl(game)
                #self.cannon2attackB(game)
                # object.update_col()
                game.balloons[2].update_col()
                game.render()
                buildcheck=game.checkbuildings()
                if(buildcheck==True):
                    break    


        return key