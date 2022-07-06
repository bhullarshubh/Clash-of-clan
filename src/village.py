from colorama import Fore, Back, Style

class Buildings():
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.health=100

class TownHall(Buildings):
    def __init__(self,x,y):
        super().__init__(x,y)

        self.color=Back.GREEN+'T'+Style.RESET_ALL

    def update_col(self):
        if (self.health>=50):
            self.color=Back.GREEN+'T'+Style.RESET_ALL
        if (self.health<50 and self.health>=20):
            self.color=Back.YELLOW+'T'+Style.RESET_ALL
        if (self.health<20 and self.health>0):
            self.color=Back.RED+'T'+Style.RESET_ALL
        if (self.health<=0):
            self.color=Back.WHITE+' '+Style.RESET_ALL

class Walls():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.health=1

        self.color=Back.CYAN+' '+Style.RESET_ALL


    def update_col(self):
        if self.health==1:
            self.color=Back.CYAN+' '+Style.RESET_ALL
        else:
            self.color=Back.WHITE+' '+Style.RESET_ALL

class Cannon():
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.damage=10
        self.range=5
        self.prevtime=0
        self.attack=False
        self.health=1


        self.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL

    def update_col(self):
        if self.attack==True:
            self.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'C'+Style.RESET_ALL
        else:
            self.color=Back.RED+Fore.BLACK+'C'+Style.RESET_ALL
        
        if self.health==0:
            self.color=Back.WHITE+' '+Style.RESET_ALL


class Wizard():
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.damage=10
        self.range=5
        self.prevtime=0
        self.attack=False
        self.health=1


        self.color=Back.RED+Fore.BLACK+'W'+Style.RESET_ALL

    def update_col(self):
        if self.attack==True:
            self.color=Back.LIGHTYELLOW_EX+Fore.BLACK+'W'+Style.RESET_ALL
        else:
            self.color=Back.RED+Fore.BLACK+'W'+Style.RESET_ALL
        
        if self.health==0:
            self.color=Back.WHITE+' '+Style.RESET_ALL



class Huts(Buildings):
    def __init__(self,x,y):
        super().__init__(x,y)

        self.color=Back.GREEN+Fore.BLACK+'H'+Style.RESET_ALL

    def update_col(self):
        if (self.health>=50):
            self.color=Back.GREEN+'H'+Style.RESET_ALL
        if (self.health<50 and self.health>=20):
            self.color=Back.YELLOW+'H'+Style.RESET_ALL
        if (self.health<20 and self.health>0):
            self.color=Back.RED+'H'+Style.RESET_ALL
        if (self.health<=0):
            self.color=Back.WHITE+' '+Style.RESET_ALL
