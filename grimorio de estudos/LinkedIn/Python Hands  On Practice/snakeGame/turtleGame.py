# Import the Turtle Graphics module
import turtle

import random

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 300  # delay between actions
FOODSIZE = 10

OFFSETS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bindDirectionKeys():
    screen.onkey(lambda: setSnakeDirection("up",), "Up")
    screen.onkey(lambda: setSnakeDirection("down",), "Down")
    screen.onkey(lambda: setSnakeDirection("left",), "Left")
    screen.onkey(lambda: setSnakeDirection("right",), "Right")

def setSnakeDirection(direction):
    global DIRECTION
    if direction == "up":
        if DIRECTION != "down":
            DIRECTION = "up"
            
    elif direction == "down":
        if DIRECTION != "up":
            DIRECTION = "down"
            
    elif direction == "right":    
        if DIRECTION != "left":
            DIRECTION = "right"
            
    elif direction == "left":    
        if DIRECTION != "right":
            DIRECTION = "left"        

def gameLoop():
    mySnake.clearstamps()  # Remove existing stamps made by mySnake.

    newHead = snake[-1].copy()
    newHead[0] += OFFSETS[DIRECTION][0]
    newHead[1] += OFFSETS[DIRECTION][1]
    
    # colision
    if newHead in snake or newHead[0] < - WIDTH / 2 or newHead[0] > WIDTH / 2 \
        or newHead[1] < - HEIGHT / 2 or newHead[1] > HEIGHT / 2:
            resetGame()
    else:
        # Add new head to snake body.
        snake.append(newHead)

        if not foodColision():    
            # Remove last segment of snake.
            snake.pop(0)

        # Draw snake for the first time.
        for segment in snake:
            mySnake.goto(segment[0], segment[1])
            mySnake.stamp()

        # refresh  screen
        screen.title(f"Sneaky Snake Game. Score: {SCORE}")
        screen.update()

        # repeat
        turtle.ontimer(gameLoop, DELAY)


def getDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    
    return distance

def foodGetPos():
    x = random.randint(-WIDTH / 2 + FOODSIZE, WIDTH / 2 - FOODSIZE)
    y = random.randint(-HEIGHT / 2 + FOODSIZE, HEIGHT / 2 - FOODSIZE)
    return (x, y)

def foodColision():
    global foodPos, SCORE, DELAY

    if  getDistance(snake[-1], foodPos) < 20:
        SCORE += 1
        foodPos = foodGetPos()
        food.goto(foodPos)
        if DELAY > 105:
            DELAY -= 15
        return True
    return False

def resetGame():
    global SCORE, foodPos, snake, DIRECTION
    SCORE = 0
    DIRECTION = "up"
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    foodPos = foodGetPos()
    food.goto(foodPos)
    gameLoop()

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Sneaky Snake")
screen.bgcolor("cyan")
screen.tracer(0)  # turn off auto animation.

# event listeners
screen.listen()
bindDirectionKeys()

# initiates snake
mySnake = turtle.Turtle()
mySnake.shape("square")
mySnake.color("pink")
mySnake.penup()

# create a list of snake coordinates
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
SCORE = 0
DIRECTION = "up"

# Food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOODSIZE / 20)
food.penup()
foodPos = foodGetPos()
food.goto(foodPos)

# set game
resetGame()

# finish
turtle.done()