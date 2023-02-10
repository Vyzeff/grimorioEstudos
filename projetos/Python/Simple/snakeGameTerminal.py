# A simple snake game, similar to the other snake game I made, but this time pretty much 
# a downgraded version to the terminal.

from pytimedinput import timedInput
import os
from random import randint
from colorama import Fore, init

def fieldPrint():
    for cell in CELLS:
        if cell in scakeBody:
            print(Fore.LIGHTCYAN_EX + 'W', end='')
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT -1):
            print(Fore.LIGHTYELLOW_EX +"#", end="")
        elif cell == scorePos:
            print(Fore.MAGENTA + "S", end='')
        else:
            print(" ", end='')
        if cell[0] == FIELD_WIDTH - 1:
            print("")

def updateScake():
    global eaten
    newHead = scakeBody[0][0] + direction[0], scakeBody[0][1] + direction[1]
    scakeBody.insert(0, newHead)
    
    if not eaten:
        scakeBody.pop()
    eaten = False
    
def scoreCollision():
    global scorePos, eaten
    if scorePos == scakeBody[0]:
        scorePos = scorePlace() 
        eaten = True

def scorePlace():
    newPos = (randint(1, FIELD_WIDTH - 2), randint(1, FIELD_HEIGHT - 2))
    while newPos in scakeBody:
        newPos = (randint(1, FIELD_WIDTH - 2), randint(1, FIELD_HEIGHT - 2))
        
    return newPos

# colorama contain colors
init(autoreset=True)

# config
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]
DIRECTIONS = {'left': (-1, 0), 'right': (1,0), 'up': (0, -1), 'down': (0, 1)}

# scake
scakeBody = [(5, FIELD_HEIGHT // 2), (4, FIELD_HEIGHT // 2), (3, FIELD_HEIGHT // 2)]
direction = DIRECTIONS['right']
eaten = False

# score
scorePos = scorePlace()


while True:
    # clear field
    os.system('clear') # clear for mac and linux, cls for windows

    
    # update field
    fieldPrint()
    
    # get input
    txt,nothing = timedInput('', timeout= 0.3)
    match txt:
        case 'w': direction = DIRECTIONS['up']
        case 's': direction = DIRECTIONS['down']
        case 'a': direction = DIRECTIONS['left']
        case 'd': direction = DIRECTIONS['right']
        case 'q': 
            os.system('clear')
            print("Quit Game!")
            break


    # update scake
    scoreCollision()
    updateScake()

    # death check
    if scakeBody[0][0] in (0, FIELD_WIDTH - 1) or \
    scakeBody[0][1] in (0, FIELD_HEIGHT - 1) or \
    scakeBody[0] in scakeBody[1:]:
        os.system('clear')
        print('You lost!')
        break