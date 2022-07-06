from colorama import Fore, Back, Style
from src.input import *
import time
import threading as th

class Queen():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 8
        self.health = 100
        self.velocity = 1
        self.lastdirection= 1

        self.color = Back.BLUE+Fore.BLACK+'Q'+Style.RESET_ALL

        self.inputClass = Get()

    def updatequeen(self):
        if self.health == 0:
            self.color = Back.WHITE+' '+Style.RESET_ALL

    def cannonattackB(self, game2):
        for cannon in game2.cannons:
            if cannon.health != 0:
                flag = 0
                for i in range(3):
                    if((abs(cannon.x-game2.barbarians[i].x)+abs(cannon.y-game2.barbarians[i].y)) <= cannon.range and time.time()-cannon.prevtime > 1 and game2.barbarians[i].health > 0):
                        flag = 1
                        game2.barbarians[i].health = game2.barbarians[i].health - \
                            cannon.damage
                        cannon.prevtime = time.time()
                        cannon.attack = True
                        cannon.update_col()

                if flag == 0:
                    cannon.attack = False
                    cannon.update_col()

    def cannonattackA(self, game2):
        for cannon in game2.cannons:
            if cannon.health != 0:
                flag = 0
                for i in range(3):
                    if((abs(cannon.x-game2.archers[i].x)+abs(cannon.y-game2.archers[i].y)) <= cannon.range and time.time()-cannon.prevtime > 1 and game2.archers[i].health > 0):
                        flag = 1
                        game2.archers[i].health = game2.archers[i].health - \
                            cannon.damage
                        cannon.prevtime = time.time()
                        cannon.attack = True
                        cannon.update_col()

                if flag == 0:
                    cannon.attack = False
                    cannon.update_col()

    def wizardattackB(self, game2):
        for wizard in game2.wizards:
            if wizard.health != 0:
                flag = 0
                for i in range(3):
                    if((abs(wizard.x-game2.barbarians[i].x)+abs(wizard.y-game2.barbarians[i].y)) <= wizard.range and time.time()-wizard.prevtime > 1 and game2.barbarians[i].health > 0):
                        flag = 1
                        game2.barbarians[i].health = game2.barbarians[i].health - \
                            wizard.damage
                        wizard.prevtime = time.time()
                        wizard.attack = True
                        wizard.update_col()
                        if(abs(self.x-game2.barbarians[i].x) < 2 and abs(self.y-game2.barbarians[i].y) < 2):
                            self.health = self.health-wizard.damage
                            self.updateking()
                        for archers in game2.archers:
                            if(abs(archers.x-game2.barbarians[i].x) < 2 and abs(archers.y-game2.barbarians[i].y) < 2):
                                archers.health = archers.health-wizard.damage
                                archers.update_col()
                        for balloons in game2.balloons:
                            if(abs(balloons.x-game2.barbarians[i].x) < 2 and abs(balloons.y-game2.barbarians[i].y) < 2):
                                balloons.health = balloons.health-wizard.damage
                                balloons.update_col()

                if flag == 0:
                    wizard.attack = False
                    wizard.update_col()

    def wizardattackA(self, game2):
        for wizard in game2.wizards:
            if wizard.health != 0:
                flag = 0
                for i in range(3):
                    if((abs(wizard.x-game2.archers[i].x)+abs(wizard.y-game2.archers[i].y)) <= wizard.range and time.time()-wizard.prevtime > 1 and game2.archers[i].health > 0):
                        flag = 1
                        game2.archers[i].health = game2.archers[i].health - \
                            wizard.damage
                        wizard.prevtime = time.time()
                        wizard.attack = True
                        wizard.update_col()
                        for barbarians in game2.barbarians:
                            if(abs(barbarians.x-game2.archers[i].x) < 2 and abs(barbarians.y-game2.archers[i].y) < 2):
                                barbarians.health = barbarians.health-wizard.damage
                                barbarians.update_col()
                        if(abs(self.x-game2.archers[i].x) < 2 and abs(self.y-game2.archers[i].y) < 2):
                            self.health = self.health-wizard.damage
                            self.updateking()
                        for balloons in game2.balloons:
                            if(abs(balloons.x-game2.archers[i].x) < 2 and abs(balloons.y-game2.archers[i].y) < 2):
                                balloons.health = balloons.health-wizard.damage
                                balloons.update_col()
                if flag == 0:
                    wizard.attack = False
                    wizard.update_col()

    def cannonattackQ(self, game2):
        for cannon in game2.cannons:
            if cannon.health != 0:
                if((abs(cannon.x-self.x)+abs(cannon.y-self.y)) <= cannon.range and time.time()-cannon.prevtime > 1 and self.health > 0):
                    self.health = self.health-cannon.damage
                    cannon.prevtime = time.time()
                    cannon.attack = True
                    cannon.update_col()
                else:
                    cannon.attack = False
                    cannon.update_col()

    def wizardattackQ(self, game2):
        for wizard in game2.wizards:
            if wizard.health != 0:
                if((abs(wizard.x-self.x)+abs(wizard.y-self.y)) <= wizard.range and time.time()-wizard.prevtime > 1 and self.health > 0):
                    self.health = self.health-wizard.damage
                    wizard.prevtime = time.time()
                    wizard.attack = True
                    wizard.update_col()
                    for barbarians in game2.barbarians:
                        if(abs(barbarians.x-self.x) < 2 and abs(barbarians.y-self.y) < 2):
                            barbarians.health = barbarians.health-wizard.damage
                            barbarians.update_col()
                    for archers in game2.archers:
                        if(abs(archers.x-self.x) < 2 and abs(archers.y-self.y) < 2):
                            archers.health = archers.health-wizard.damage
                            archers.update_col()
                    for balloons in game2.balloons:
                        if(abs(balloons.x-self.x) < 2 and abs(balloons.y-self.y) < 2):
                            balloons.health = balloons.health-wizard.damage
                            balloons.update_col()
                else:
                    wizard.attack = False
                    wizard.update_col()

    def wizardattackBl(self, game2):
        for wizard in game2.wizards:
            if wizard.health != 0:
                flag = 0
                for i in range(3):
                    if((abs(wizard.x-game2.balloons[i].x)+abs(wizard.y-game2.balloons[i].y)) <= wizard.range and time.time()-wizard.prevtime > 1 and game2.balloons[i].health > 0):
                        flag = 1
                        game2.balloons[i].health = game2.balloons[i].health - \
                            wizard.damage
                        wizard.prevtime = time.time()
                        wizard.attack = True
                        wizard.update_col()
                        for barbarians in game2.barbarians:
                            if(abs(barbarians.x-game2.balloons[i].x) < 2 and abs(barbarians.y-game2.balloons[i].y) < 2):
                                barbarians.health = barbarians.health-wizard.damage
                                barbarians.update_col()
                        if(abs(self.x-game2.balloons[i].x) < 2 and abs(self.y-game2.balloons[i].y) < 2):
                            self.health = self.health-wizard.damage
                            self.updateking()
                        for archers in game2.archers:
                            if(abs(archers.x-game2.balloons[i].x) < 2 and abs(archers.y-game2.balloons[i].y) < 2):
                                archers.health = archers.health-wizard.damage
                                archers.update_col()
                if flag == 0:
                    wizard.attack = False
                    wizard.update_col()
    def powerattack(self,game2):
        if self.lastdirection==1:
            tx=self.x-16
            ty=self.y
        if self.lastdirection==2:
            tx=self.x
            ty=self.y-16
        if self.lastdirection==3:
            tx=self.x+16
            ty=self.y
        if self.lastdirection==4:
            tx=self.x
            ty=self.y+16
        for walls in game2.walls:
            if (abs(walls.x-tx) < 5 and abs(walls.y-ty) < 5):
                walls.health = 0
                walls.update_col()
        for huts in game2.huts:
            if(abs(huts.x-tx) < 5 and abs(huts.y-ty) < 5):
                huts.health = huts.health-self.damage
                huts.update_col()
        for townhall in game2.townhall:
            if(abs(townhall.x-tx) < 5 and abs(townhall.y-ty) < 5):
                townhall.health = townhall.health-self.damage
                townhall.update_col()
    # def cannon1attackB(self,game2):
    #     flag=0
    #     for i in range(3):
    #         if((abs(game2.cannon1.x-game2.barbarians[i].x)+abs(game2.cannon1.y-game2.barbarians[i].y))<=10 and time.time()-game2.cannon1.prevtime>1 and game2.barbarians[i].health>0):
    #             flag=1
    #             game2.barbarians[i].health=game2.barbarians[i].health-game2.cannon1.damage
    #             game2.cannon1.prevtime=time.time()
    #             game2.cannon1.attack=True
    #             game2.cannon1.update_col()

    #     if flag==0:
    #         game2.cannon1.attack=False
    #         game2.cannon1.update_col()

    # def cannon1attackK(self,game2):
    #     if((abs(game2.cannon1.x-self.x)+abs(game2.cannon1.y-self.y))<=game2.cannon1.range and time.time()-game2.cannon1.prevtime>1 and self.health>0):
    #         self.health=self.health-game2.cannon1.damage
    #         game2.cannon1.prevtime=time.time()
    #         game2.cannon1.attack=True
    #         game2.cannon1.update_col()
    #     else:
    #         game2.cannon1.attack=False
    #         game2.cannon1.update_col()

    #         #else:
    #             #game2.cannon1.attack=False
    #             #game2.cannon1.update_col()
    #         #game2.cannon1.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'C'+Style.RESET_ALL
    #     #game2.cannon1.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL
    # def cannon2attackB(self,game2):
    #     flag=0
    #     for i in range(3):
    #         if((abs(game2.cannon2.x-game2.barbarians[i].x)+abs(game2.cannon2.y-game2.barbarians[i].y))<=10 and time.time()-game2.cannon2.prevtime>1 and game2.barbarians[i].health>0):
    #             flag=1
    #             game2.barbarians[i].health=game2.barbarians[i].health-game2.cannon2.damage
    #             game2.cannon2.prevtime=time.time()
    #             game2.cannon2.attack=True
    #             game2.cannon2.update_col()
    #     if flag==0:    #else:
    #         game2.cannon2.attack=False
    #         game2.cannon2.update_col()

    # def cannon2attackK(self,game2):
    #     if((abs(game2.cannon2.x-self.x)+abs(game2.cannon2.y-self.y))<=game2.cannon2.range and time.time()-game2.cannon2.prevtime>1 and self.health>0):
    #         self.health=self.health-game2.cannon2.damage
    #         game2.cannon2.prevtime=time.time()
    #         game2.cannon2.attack=True
    #         game2.cannon2.update_col()
    #     else:
    #        game2.cannon2.attack=False
    #        game2.cannon2.update_col()

    #         #game2.cannon1.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'C'+Style.RESET_ALL
    #     #game2.cannon1.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL

    def queenMove(self, game2):
        key = input_to(self.inputClass)
        if(key == 'w' and self.x > 0 and game2.setup[self.x-1][self.y] == game2.defaultColor and game2.setup[self.x-self.velocity][self.y] == game2.defaultColor and self.health>0):
            self.x = self.x-self.velocity
            self.lastdirection=1
        if(key == 'a' and self.y > 0 and game2.setup[self.x][self.y-1] == game2.defaultColor and game2.setup[self.x][self.y-self.velocity] == game2.defaultColor and self.health>0):
            self.y = self.y-self.velocity
            self.lastdirection=2
        if(key == 's' and self.x < 24 and game2.setup[self.x+1][self.y] == game2.defaultColor and game2.setup[self.x+self.velocity][self.y] == game2.defaultColor and self.health>0):
            self.x = self.x+self.velocity
            self.lastdirection=3
        if(key == 'd' and self.y < 79 and game2.setup[self.x][self.y+1] == game2.defaultColor and game2.setup[self.x][self.y+self.velocity] == game2.defaultColor and self.health>0):
            self.y = self.y+self.velocity
            self.lastdirection=4
        if(key == ' ' and self.health>0):
            if self.lastdirection==1:
                tx=self.x-8
                ty=self.y
            if self.lastdirection==2:
                tx=self.x
                ty=self.y-8
            if self.lastdirection==3:
                tx=self.x+8
                ty=self.y
            if self.lastdirection==4:
                tx=self.x
                ty=self.y+8
            for walls in game2.walls:
                if (abs(walls.x-tx) < 3 and abs(walls.y-ty) < 3):
                    walls.health = 0
                    walls.update_col()
            for huts in game2.huts:
                if(abs(huts.x-tx) < 3 and abs(huts.y-ty) < 3):
                    huts.health = huts.health-self.damage
                    huts.update_col()
            for townhall in game2.townhall:
                if(abs(townhall.x-tx) < 3 and abs(townhall.y-ty) < 3):
                    townhall.health = townhall.health-self.damage
                    townhall.update_col()
        if(key=='p' and self.health>0):
            s=th.Timer(1.0,self.powerattack,[game2])
            s.start()
        # if(key==' ' and game2.setup[self.x+1][self.y]!=game2.defaultColor):
        #     for walls in game2.walls:
        #         if(walls.x==self.x+1 and walls.y==self.y):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game2.huts:
        #         if(huts.x==self.x+1 and huts.y==self.y):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game2.townhall:
        #         if(townhall.x==self.x+1 and townhall.y==self.y):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game2.setup[self.x-1][self.y]!=game2.defaultColor):
        #     for walls in game2.walls:
        #         if(walls.x==self.x-1 and walls.y==self.y):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game2.huts:
        #         if(huts.x==self.x-1 and huts.y==self.y):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game2.townhall:
        #         if(townhall.x==self.x-1 and townhall.y==self.y):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game2.setup[self.x][self.y+1]!=game2.defaultColor):
        #     for walls in game2.walls:
        #         if(walls.x==self.x and walls.y==self.y+1):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game2.huts:
        #         if(huts.x==self.x and huts.y==self.y+1):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game2.townhall:
        #         if(townhall.x==self.x and townhall.y==self.y+1):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        # if(key==' ' and game2.setup[self.x][self.y-1]!=game2.defaultColor):
        #     for walls in game2.walls:
        #         if(walls.x==self.x and walls.y==self.y-1):
        #             walls.health=0
        #             walls.update_col()
        #     for huts in game2.huts:
        #         if(huts.x==self.x and huts.y==self.y-1):
        #             huts.health=huts.health-self.damage
        #             huts.update_col()
        #     for townhall in game2.townhall:
        #         if(townhall.x==self.x and townhall.y==self.y-1):
        #             townhall.health=townhall.health-self.damage
        #             townhall.update_col()
        if(key == 'r'):
            self.damage = 2*self.damage
            self.velocity = 2*self.velocity
            for barbarian in game2.barbarians:
                barbarian.damage = 2*barbarian.damage
                barbarian.velocity=2*barbarian.velocity
            for archer in game2.archers:
                archer.damage = 2*archer.damage
                archer.velocity=2*archer.velocity
            for balloon in game2.balloons:
                balloon.damage = 2*balloon.damage
                balloon.velocity=2*balloon.velocity
        if(key == 'h'):
            self.health = 1.5*self.health
            if(self.health > 100):
                self.health = 100
            for barbarian in game2.barbarians:
                barbarian.health = 2*barbarian.health
                if(barbarian.health > 100):
                    barbarian.health = 100
            for balloon in game2.balloons:
                balloon.health = 2*balloon.health
                if(balloon.health > 100):
                    balloon.health = 100
            for archer in game2.archers:
                archer.health = 2*archer.health
                if(archer.health > 100):
                    archer.health = 100
        if (key == '1'):
            while game2.barbarians[0].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.barbarians[0].x)+abs(walls.y-game2.barbarians[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.barbarians[0].x)+abs(walls.y-game2.barbarians[0].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.barbarians[0].x)+abs(huts.y-game2.barbarians[0].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.barbarians[0].x)+abs(huts.y-game2.barbarians[0].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.barbarians[0].x)+abs(townhall.y-game2.barbarians[0].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.barbarians[0].x)+abs(townhall.y-game2.barbarians[0].y))
                if game2.barbarians[0].x < min_x:
                    game2.barbarians[0].x = game2.barbarians[0].x+1
                elif game2.barbarians[0].x > min_x:
                    game2.barbarians[0].x = game2.barbarians[0].x-1
                else:
                    game2.barbarians[0].x = game2.barbarians[0].x
                if game2.barbarians[0].y < min_y:
                    game2.barbarians[0].y = game2.barbarians[0].y+1
                elif game2.barbarians[0].y > min_y:
                    game2.barbarians[0].y = game2.barbarians[0].y-1
                else:
                    game2.barbarians[0].y = game2.barbarians[0].y
                # game2.barbarians[0].y=min_y
                # object.health=0
                for walls in game2.walls:
                    if(game2.barbarians[0].x == walls.x and game2.barbarians[0].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.barbarians[0].x == huts.x and game2.barbarians[0].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.barbarians[0].x == townhall.x and game2.barbarians[0].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.barbarians[0].velocity)
                self.cannonattackB(game2)
                self.wizardattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.barbarians[0].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break
        if (key == '2'):
            while game2.barbarians[1].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.barbarians[1].x)+abs(walls.y-game2.barbarians[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.barbarians[1].x)+abs(walls.y-game2.barbarians[1].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.barbarians[1].x)+abs(huts.y-game2.barbarians[1].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.barbarians[1].x)+abs(huts.y-game2.barbarians[1].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.barbarians[1].x)+abs(townhall.y-game2.barbarians[1].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.barbarians[1].x)+abs(townhall.y-game2.barbarians[1].y))
                if game2.barbarians[1].x < min_x:
                    game2.barbarians[1].x = game2.barbarians[1].x+1
                elif game2.barbarians[1].x > min_x:
                    game2.barbarians[1].x = game2.barbarians[1].x-1
                else:
                    game2.barbarians[1].x = game2.barbarians[1].x
                if game2.barbarians[1].y < min_y:
                    game2.barbarians[1].y = game2.barbarians[1].y+1
                elif game2.barbarians[1].y > min_y:
                    game2.barbarians[1].y = game2.barbarians[1].y-1
                else:
                    game2.barbarians[1].y = game2.barbarians[1].y
                # game2.barbarians[1].y=min_y
                # object.health=0
                for walls in game2.walls:
                    if(game2.barbarians[1].x == walls.x and game2.barbarians[1].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.barbarians[1].x == huts.x and game2.barbarians[1].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.barbarians[1].x == townhall.x and game2.barbarians[1].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.barbarians[1].velocity)
                self.cannonattackB(game2)
                self.wizardattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.barbarians[1].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break
        if (key == '3'):
            while game2.barbarians[2].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.barbarians[2].x)+abs(walls.y-game2.barbarians[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.barbarians[2].x)+abs(walls.y-game2.barbarians[2].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.barbarians[2].x)+abs(huts.y-game2.barbarians[2].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.barbarians[2].x)+abs(huts.y-game2.barbarians[2].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.barbarians[2].x)+abs(townhall.y-game2.barbarians[2].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.barbarians[2].x)+abs(townhall.y-game2.barbarians[2].y))
                if game2.barbarians[2].x < min_x:
                    game2.barbarians[2].x = game2.barbarians[2].x+1
                elif game2.barbarians[2].x > min_x:
                    game2.barbarians[2].x = game2.barbarians[2].x-1
                else:
                    game2.barbarians[2].x = game2.barbarians[2].x
                if game2.barbarians[2].y < min_y:
                    game2.barbarians[2].y = game2.barbarians[2].y+1
                elif game2.barbarians[2].y > min_y:
                    game2.barbarians[2].y = game2.barbarians[2].y-1
                else:
                    game2.barbarians[2].y = game2.barbarians[2].y
                # game2.barbarians[2].y=min_y
                # object.health=0
                for walls in game2.walls:
                    if(game2.barbarians[2].x == walls.x and game2.barbarians[2].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.barbarians[2].x == huts.x and game2.barbarians[2].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.barbarians[2].x == townhall.x and game2.barbarians[2].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.barbarians[2].velocity)
                self.cannonattackB(game2)
                self.wizardattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.barbarians[2].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break
        if (key == '4'):
            while game2.archers[0].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.archers[0].x)+abs(walls.y-game2.archers[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.archers[0].x)+abs(walls.y-game2.archers[0].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.archers[0].x)+abs(huts.y-game2.archers[0].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.archers[0].x)+abs(huts.y-game2.archers[0].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.archers[0].x)+abs(townhall.y-game2.archers[0].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.archers[0].x)+abs(townhall.y-game2.archers[0].y))
                if game2.archers[0].x < min_x:
                    game2.archers[0].x = game2.archers[0].x+1
                elif game2.archers[0].x > min_x:
                    game2.archers[0].x = game2.archers[0].x-1
                else:
                    game2.archers[0].x = game2.archers[0].x
                if game2.archers[0].y < min_y:
                    game2.archers[0].y = game2.archers[0].y+1
                elif game2.archers[0].y > min_y:
                    game2.archers[0].y = game2.archers[0].y-1
                else:
                    game2.archers[0].y = game2.archers[0].y
                # game2.archers[0].y=min_y
                # object.health=0
                for huts in game2.huts:
                    if(abs(huts.x-game2.archers[0].x)+abs(huts.y-game2.archers[0].y) < game2.archers[0].range and huts.health != 0):
                        huts.health = huts.health-game2.archers[0].damage
                        huts.update_col()

                for townhall in game2.townhall:
                    if(abs(townhall.x-game2.archers[0].x)+abs(townhall.y-game2.archers[0].y) < game2.archers[0].range and townhall.health != 0):
                        townhall.health = townhall.health - \
                            game2.archers[0].damage
                        townhall.update_col()

                for walls in game2.walls:
                    if(game2.archers[0].x == walls.x and game2.archers[0].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.archers[0].x == huts.x and game2.archers[0].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.archers[0].x == townhall.x and game2.archers[0].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.archers[0].velocity)
                # self.cannonattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                self.cannonattackA(game2)
                self.wizardattackA(game2)
                game2.archers[0].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        if (key == '5'):
            while game2.archers[1].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.archers[1].x)+abs(walls.y-game2.archers[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.archers[1].x)+abs(walls.y-game2.archers[1].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.archers[1].x)+abs(huts.y-game2.archers[1].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.archers[1].x)+abs(huts.y-game2.archers[1].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.archers[1].x)+abs(townhall.y-game2.archers[1].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.archers[1].x)+abs(townhall.y-game2.archers[1].y))
                if game2.archers[1].x < min_x:
                    game2.archers[1].x = game2.archers[1].x+1
                elif game2.archers[1].x > min_x:
                    game2.archers[1].x = game2.archers[1].x-1
                else:
                    game2.archers[1].x = game2.archers[1].x
                if game2.archers[1].y < min_y:
                    game2.archers[1].y = game2.archers[1].y+1
                elif game2.archers[1].y > min_y:
                    game2.archers[1].y = game2.archers[1].y-1
                else:
                    game2.archers[1].y = game2.archers[1].y
                # game2.archers[1].y=min_y
                # object.health=0
                for huts in game2.huts:
                    if(abs(huts.x-game2.archers[1].x)+abs(huts.y-game2.archers[1].y) < game2.archers[1].range and huts.health != 0):
                        huts.health = huts.health-game2.archers[1].damage
                        huts.update_col()

                for townhall in game2.townhall:
                    if(abs(townhall.x-game2.archers[1].x)+abs(townhall.y-game2.archers[1].y) < game2.archers[1].range and townhall.health != 0):
                        townhall.health = townhall.health - \
                            game2.archers[1].damage
                        townhall.update_col()

                for walls in game2.walls:
                    if(game2.archers[1].x == walls.x and game2.archers[1].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.archers[1].x == huts.x and game2.archers[1].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.archers[1].x == townhall.x and game2.archers[1].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.archers[1].velocity)
                # self.cannonattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                self.cannonattackA(game2)
                self.wizardattackA(game2)
                game2.archers[1].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        if (key == '6'):
            while game2.archers[2].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.archers[2].x)+abs(walls.y-game2.archers[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.archers[2].x)+abs(walls.y-game2.archers[2].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.archers[2].x)+abs(huts.y-game2.archers[2].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.archers[2].x)+abs(huts.y-game2.archers[2].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.archers[2].x)+abs(townhall.y-game2.archers[2].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.archers[2].x)+abs(townhall.y-game2.archers[2].y))
                if game2.archers[2].x < min_x:
                    game2.archers[2].x = game2.archers[2].x+1
                elif game2.archers[2].x > min_x:
                    game2.archers[2].x = game2.archers[2].x-1
                else:
                    game2.archers[2].x = game2.archers[2].x
                if game2.archers[2].y < min_y:
                    game2.archers[2].y = game2.archers[2].y+1
                elif game2.archers[2].y > min_y:
                    game2.archers[2].y = game2.archers[2].y-1
                else:
                    game2.archers[2].y = game2.archers[2].y
                # game2.archers[2].y=min_y
                # object.health=0
                for huts in game2.huts:
                    if(abs(huts.x-game2.archers[2].x)+abs(huts.y-game2.archers[2].y) < game2.archers[2].range and huts.health != 0):
                        huts.health = huts.health-game2.archers[2].damage
                        huts.update_col()

                for townhall in game2.townhall:
                    if(abs(townhall.x-game2.archers[2].x)+abs(townhall.y-game2.archers[2].y) < game2.archers[2].range and townhall.health != 0):
                        townhall.health = townhall.health - \
                            game2.archers[2].damage
                        townhall.update_col()

                for walls in game2.walls:
                    if(game2.archers[2].x == walls.x and game2.archers[2].y == walls.y):
                        walls.health = 0
                        walls.update_col()
                for huts in game2.huts:
                    if(game2.archers[2].x == huts.x and game2.archers[2].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.archers[2].x == townhall.x and game2.archers[2].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.archers[2].velocity)
                # self.cannonattackB(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                self.cannonattackA(game2)
                self.wizardattackA(game2)
                game2.archers[2].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        if (key == '7'):
            while game2.balloons[0].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[0].x)+abs(walls.y-game2.balloons[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[0].x)+abs(walls.y-game2.balloons[0].y))
                for cannons in game2.cannons:
                    if((abs(cannons.x-game2.balloons[0].x)+abs(cannons.y-game2.balloons[0].y)) < min and cannons.health > 0):
                        min_x = cannons.x
                        min_y = cannons.y
                        object = cannons
                        min = (
                            abs(cannons.x-game2.balloons[0].x)+abs(cannons.y-game2.balloons[0].y))
                for wizards in game2.wizards:
                    if((abs(wizards.x-game2.balloons[0].x)+abs(wizards.y-game2.balloons[0].y)) < min and wizards.health > 0):
                        min_x = wizards.x
                        min_y = wizards.y
                        object = wizards
                        min = (
                            abs(wizards.x-game2.balloons[0].x)+abs(wizards.y-game2.balloons[0].y))
                if game2.balloons[0].x < min_x:
                    game2.balloons[0].x = game2.balloons[0].x+1
                elif game2.balloons[0].x > min_x:
                    game2.balloons[0].x = game2.balloons[0].x-1
                else:
                    game2.balloons[0].x = game2.balloons[0].x
                if game2.balloons[0].y < min_y:
                    game2.balloons[0].y = game2.balloons[0].y+1
                elif game2.balloons[0].y > min_y:
                    game2.balloons[0].y = game2.balloons[0].y-1
                else:
                    game2.balloons[0].y = game2.balloons[0].y
                for cannons in game2.cannons:
                    if(game2.balloons[0].x == cannons.x and game2.balloons[0].y == cannons.y):
                        cannons.health = 0
                        cannons.update_col()
                for wizards in game2.wizards:
                    if(game2.balloons[0].x == wizards.x and game2.balloons[0].y == wizards.y):
                        wizards.health = 0
                        wizards.update_col()
                time.sleep(1/game2.balloons[0].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[0].update_col()
                game2.render()
                defensecheck = 0
                for cannons in game2.cannons:
                    if(cannons.health > 0):
                        defensecheck = 1
                for wizards in game2.wizards:
                    if(wizards.health > 0):
                        defensecheck = 1

                if defensecheck == 0:
                    break
            while game2.balloons[0].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[0].x)+abs(walls.y-game2.balloons[0].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[0].x)+abs(walls.y-game2.balloons[0].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.balloons[0].x)+abs(huts.y-game2.balloons[0].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.balloons[0].x)+abs(huts.y-game2.balloons[0].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.balloons[0].x)+abs(townhall.y-game2.balloons[0].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.balloons[0].x)+abs(townhall.y-game2.balloons[0].y))
                if game2.balloons[0].x < min_x:
                    game2.balloons[0].x = game2.balloons[0].x+1
                elif game2.balloons[0].x > min_x:
                    game2.balloons[0].x = game2.balloons[0].x-1
                else:
                    game2.balloons[0].x = game2.balloons[0].x
                if game2.balloons[0].y < min_y:
                    game2.balloons[0].y = game2.balloons[0].y+1
                elif game2.balloons[0].y > min_y:
                    game2.balloons[0].y = game2.balloons[0].y-1
                else:
                    game2.balloons[0].y = game2.balloons[0].y
                # game2.balloons[0].y=min_y
                # object.health=0
                # for walls in game2.walls:
                #     if(game2.balloons[0].x==walls.x and game2.balloons[0].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game2.huts:
                    if(game2.balloons[0].x == huts.x and game2.balloons[0].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.balloons[0].x == townhall.x and game2.balloons[0].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.balloons[0].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[0].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        if (key == '8'):
            while game2.balloons[1].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[1].x)+abs(walls.y-game2.balloons[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[1].x)+abs(walls.y-game2.balloons[1].y))
                for cannons in game2.cannons:
                    if((abs(cannons.x-game2.balloons[1].x)+abs(cannons.y-game2.balloons[1].y)) < min and cannons.health > 0):
                        min_x = cannons.x
                        min_y = cannons.y
                        object = cannons
                        min = (
                            abs(cannons.x-game2.balloons[1].x)+abs(cannons.y-game2.balloons[1].y))
                for wizards in game2.wizards:
                    if((abs(wizards.x-game2.balloons[1].x)+abs(wizards.y-game2.balloons[1].y)) < min and wizards.health > 0):
                        min_x = wizards.x
                        min_y = wizards.y
                        object = wizards
                        min = (
                            abs(wizards.x-game2.balloons[1].x)+abs(wizards.y-game2.balloons[1].y))
                if game2.balloons[1].x < min_x:
                    game2.balloons[1].x = game2.balloons[1].x+1
                elif game2.balloons[1].x > min_x:
                    game2.balloons[1].x = game2.balloons[1].x-1
                else:
                    game2.balloons[1].x = game2.balloons[1].x
                if game2.balloons[1].y < min_y:
                    game2.balloons[1].y = game2.balloons[1].y+1
                elif game2.balloons[1].y > min_y:
                    game2.balloons[1].y = game2.balloons[1].y-1
                else:
                    game2.balloons[1].y = game2.balloons[1].y
                for cannons in game2.cannons:
                    if(game2.balloons[1].x == cannons.x and game2.balloons[1].y == cannons.y):
                        cannons.health = 0
                        cannons.update_col()
                for wizards in game2.wizards:
                    if(game2.balloons[1].x == wizards.x and game2.balloons[1].y == wizards.y):
                        wizards.health = 0
                        wizards.update_col()
                time.sleep(1/game2.balloons[1].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[1].update_col()
                game2.render()
                defensecheck = 0
                for cannons in game2.cannons:
                    if(cannons.health > 0):
                        defensecheck = 1
                for wizards in game2.wizards:
                    if(wizards.health > 0):
                        defensecheck = 1

                if defensecheck == 0:
                    break
            while game2.balloons[1].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[1].x)+abs(walls.y-game2.balloons[1].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[1].x)+abs(walls.y-game2.balloons[1].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.balloons[1].x)+abs(huts.y-game2.balloons[1].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.balloons[1].x)+abs(huts.y-game2.balloons[1].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.balloons[1].x)+abs(townhall.y-game2.balloons[1].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.balloons[1].x)+abs(townhall.y-game2.balloons[1].y))
                if game2.balloons[1].x < min_x:
                    game2.balloons[1].x = game2.balloons[1].x+1
                elif game2.balloons[1].x > min_x:
                    game2.balloons[1].x = game2.balloons[1].x-1
                else:
                    game2.balloons[1].x = game2.balloons[1].x
                if game2.balloons[1].y < min_y:
                    game2.balloons[1].y = game2.balloons[1].y+1
                elif game2.balloons[1].y > min_y:
                    game2.balloons[1].y = game2.balloons[1].y-1
                else:
                    game2.balloons[1].y = game2.balloons[1].y
                # game2.balloons[1].y=min_y
                # object.health=0
                # for walls in game2.walls:
                #     if(game2.balloons[1].x==walls.x and game2.balloons[1].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game2.huts:
                    if(game2.balloons[1].x == huts.x and game2.balloons[1].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.balloons[1].x == townhall.x and game2.balloons[1].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.balloons[1].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[1].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        if (key == '9'):
            while game2.balloons[2].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[2].x)+abs(walls.y-game2.balloons[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[2].x)+abs(walls.y-game2.balloons[2].y))
                for cannons in game2.cannons:
                    if((abs(cannons.x-game2.balloons[2].x)+abs(cannons.y-game2.balloons[2].y)) < min and cannons.health > 0):
                        min_x = cannons.x
                        min_y = cannons.y
                        object = cannons
                        min = (
                            abs(cannons.x-game2.balloons[2].x)+abs(cannons.y-game2.balloons[2].y))
                for wizards in game2.wizards:
                    if((abs(wizards.x-game2.balloons[2].x)+abs(wizards.y-game2.balloons[2].y)) < min and wizards.health > 0):
                        min_x = wizards.x
                        min_y = wizards.y
                        object = wizards
                        min = (
                            abs(wizards.x-game2.balloons[2].x)+abs(wizards.y-game2.balloons[2].y))
                if game2.balloons[2].x < min_x:
                    game2.balloons[2].x = game2.balloons[2].x+1
                elif game2.balloons[2].x > min_x:
                    game2.balloons[2].x = game2.balloons[2].x-1
                else:
                    game2.balloons[2].x = game2.balloons[2].x
                if game2.balloons[2].y < min_y:
                    game2.balloons[2].y = game2.balloons[2].y+1
                elif game2.balloons[2].y > min_y:
                    game2.balloons[2].y = game2.balloons[2].y-1
                else:
                    game2.balloons[2].y = game2.balloons[2].y
                for cannons in game2.cannons:
                    if(game2.balloons[2].x == cannons.x and game2.balloons[2].y == cannons.y):
                        cannons.health = 0
                        cannons.update_col()
                for wizards in game2.wizards:
                    if(game2.balloons[2].x == wizards.x and game2.balloons[2].y == wizards.y):
                        wizards.health = 0
                        wizards.update_col()
                time.sleep(1/game2.balloons[2].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[2].update_col()
                game2.render()
                defensecheck = 0
                for cannons in game2.cannons:
                    if(cannons.health > 0):
                        defensecheck = 1
                for wizards in game2.wizards:
                    if(wizards.health > 0):
                        defensecheck = 1

                if defensecheck == 0:
                    break
            while game2.balloons[2].health > 0:
                min = 1000
                # for walls in game2.walls:
                #     if((abs(walls.x-game2.balloons[2].x)+abs(walls.y-game2.balloons[2].y))<min and walls.health>0):
                #         min_x=walls.x
                #         min_y=walls.y
                #         object=walls
                #         min=(abs(walls.x-game2.balloons[2].x)+abs(walls.y-game2.balloons[2].y))
                for huts in game2.huts:
                    if((abs(huts.x-game2.balloons[2].x)+abs(huts.y-game2.balloons[2].y)) < min and huts.health > 0):
                        min_x = huts.x
                        min_y = huts.y
                        object = huts
                        min = (
                            abs(huts.x-game2.balloons[2].x)+abs(huts.y-game2.balloons[2].y))
                for townhall in game2.townhall:
                    if((abs(townhall.x-game2.balloons[2].x)+abs(townhall.y-game2.balloons[2].y)) < min and townhall.health > 0):
                        min_x = townhall.x
                        min_y = townhall.y
                        object = townhall
                        min = (
                            abs(townhall.x-game2.balloons[2].x)+abs(townhall.y-game2.balloons[2].y))
                if game2.balloons[2].x < min_x:
                    game2.balloons[2].x = game2.balloons[2].x+1
                elif game2.balloons[2].x > min_x:
                    game2.balloons[2].x = game2.balloons[2].x-1
                else:
                    game2.balloons[2].x = game2.balloons[2].x
                if game2.balloons[2].y < min_y:
                    game2.balloons[2].y = game2.balloons[2].y+1
                elif game2.balloons[2].y > min_y:
                    game2.balloons[2].y = game2.balloons[2].y-1
                else:
                    game2.balloons[2].y = game2.balloons[2].y
                # game2.balloons[2].y=min_y
                # object.health=0
                # for walls in game2.walls:
                #     if(game2.balloons[2].x==walls.x and game2.balloons[2].y==walls.y):
                #         walls.health=0
                #         walls.update_col()
                for huts in game2.huts:
                    if(game2.balloons[2].x == huts.x and game2.balloons[2].y == huts.y):
                        huts.health = 0
                        huts.update_col()
                for townhall in game2.townhall:
                    if(game2.balloons[2].x == townhall.x and game2.balloons[2].y == townhall.y):
                        townhall.health = 0
                        townhall.update_col()
                time.sleep(1/game2.balloons[2].velocity)
                self.wizardattackBl(game2)
                # self.cannon2attackB(game2)
                # object.update_col()
                game2.balloons[2].update_col()
                game2.render()
                buildcheck = game2.checkbuildings()
                if(buildcheck == True):
                    break

        return key
