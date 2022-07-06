from colorama import Fore, Back, Style

class Archer():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.damage=10
        self.health=25
        self.velocity=2
        self.range=10

        self.color=Back.GREEN+Fore.BLACK+'A'+Style.RESET_ALL

    def update_col(self):
        if(self.health>=20):
            self.color=Back.GREEN+'A'+Style.RESET_ALL
        if(self.health>=10 and self.health<20):
            self.color=Back.YELLOW+'A'+Style.RESET_ALL
        if(self.health<10 and self.health>0):
            self.color=Back.RED+'A'+Style.RESET_ALL
        if (self.health<=0):
            self.color=Back.WHITE+' '+Style.RESET_ALL
