# Clash-of-clan
- A terminal game based on the popular Clash of Clan game written in python

## Features and Controls:

1. King or Queen - It is the main character of the game. Choice would be given in the starting of game to choose either king or queen. 

    Controls:
        1. <KBD>W</KBD> - UP 
        2. <KBD>A</KBD> - LEFT 
        3. <KBD>S</KBD> - RIGHT
        4. <KBD>D</KBD> - DOWN
        5. <KBD>SPACE</KBD> - ATTACK

2. Barbarians: These are automated troops which unleash from their specific spawning points. There are 3 spawning points and each of the spawning point is activated from a specific key. The 3 keys that I have used are '1','2','3'.
3. Archers: Spawning points of archers get activated by '4','5','6' keys. Archers can shoot from range and over walls to destroy huts and townhall.
4. Balloons: Spawning points of balloons get activated by '7','8','9' keys. Ballons first attack cannons and wizard tower and then destroy huts and townhall. They are aerial troop and can move over walls and buildings.
5. Cannons: These shoot and damage the troops except ballons in its 5 tile radius. It brightens up with a yellow color which shows that caannon is shooting.
6. Wizard Tower: The differnce between wizard tower and cannon is that wizard tower shoots in a range. 
7. Spells: The 'R' and 'H' key are used for rage and heal spell.
8. Replay: Replay feature is added. After game ends, replay is stored in a file which is played by running replay.py file. All replay files are added in replays directory.
9. Levels: There are 3 levels, each one of which is loaded when you win the its lower level. User wins the game when he finishes all the 3 levels successfully.

## Run:
- Run 'python game.py' in home directory and play game.
- Run 'pyhton replay.py' in home directory and play replay.