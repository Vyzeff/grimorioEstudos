# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # miliseconds for screen updates

def moveSnake(): # manually moves snake
    mySnake.clearstamps()
    
    newHead = snake[-1].copy()
    newHead[0] += 20
    
    #adds new head to the list
    snake.append(newHead)
    
    # removes old head
    snake.pop(0)
    
    for segment in snake:
        mySnake.goto(segment[0], segment[1])
        mySnake.stamp()
    
    # refresh screen
    screen.update()
    
    # repeats
    screen.ontimer(moveSnake, DELAY)
    
# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Sneaky Snake")
screen.bgcolor("yellow")
screen.tracer(0) # disables auto animation

# Create a turtle to do your bidding
mySnake = turtle.Turtle()
mySnake.shape("square")
mySnake.color("pink")
mySnake.penup()

# snake coordinates in (x, y)
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# draw snake
for segment in snake:
    mySnake.goto(segment[0], segment[1])
    mySnake.stamp()

# set animation
moveSnake()


# finish
turtle.done()