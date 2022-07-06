from colorama import Fore, Back, Style

class Balloon():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.damage=40
        self.health=50
        self.velocity=2

        self.color=Back.GREEN+Fore.BLACK+'L'+Style.RESET_ALL

    def update_col(self):
        if(self.health>=30):
            self.color=Back.GREEN+'L'+Style.RESET_ALL
        if(self.health>=20 and self.health<30):
            self.color=Back.YELLOW+'L'+Style.RESET_ALL
        if(self.health<20 and self.health>0):
            self.color=Back.RED+'L'+Style.RESET_ALL
        if (self.health==0):
            self.color=Back.WHITE+' '+Style.RESET_ALL