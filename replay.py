import pickle as pkl
import time
import sys
from os import system, name

filename = input("Enter filename whose replay need to be run: ")
file = open('replays/'+filename, 'rb')
printreplay = pkl.load(file)
file.close()

for element in printreplay:
    sys.stdout.write(element)
    time.sleep(1/25)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')