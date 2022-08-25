#This is a simple project, similar to snakeGame, but this time it is fully within a terminal.
#Very janky, may or may not work, but it is one of the first projects I will be doing on my own.
#Base stuff came from https://www.youtube.com/watch?v=lAIawk2IVIM

#base settings
FIELD_WIDTH = 32
FIELD_HEIGHT = 16
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]
DIRECTIONS = {"LEFT": (-1, 0), "RIGHT": (1, 0), "UP": (0, -1), "DOWN": (0, 1)}

#goal
heartPos = (5, 5)

#snake
snakeBody = [(5,FIELD_HEIGHT // 2), (4,FIELD_HEIGHT // 2), (3, FIELD_HEIGHT // 2)]
direction = DIRECTIONS['RIGHT']

#prints the hashes that surround the "game" area
def printField():
    for cell in CELLS:
        if cell in snakeBody:
            print('X', end='')
        elif cell[0] in (0, FIELD_WIDTH - 1) or cell[1] in (0, FIELD_HEIGHT - 1):
            print('#', end='')
        elif cell == heartPos:
            print("O", end='')
        else:
            print(' ', end='')
        
        if cell[0] == FIELD_WIDTH - 1:
            print('')
    print("done")

def moveSnake():
    newHead = snakeBody[0][0] + direction[0], snakeBody[0][1] + direction[1]
    snakeBody.insert(newHead)
    snakeBody.pop(-1)
    print(newHead)


#true loop
while True:
   
    printField()
    
    #update game
    moveSnake()