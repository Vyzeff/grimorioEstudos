# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20 # miliseconds for screen updates

def moveSnake(): # manually moves snake
    mySnake.forward(1)
    mySnake.right(1)
    screen.update()
    screen.ontimer(moveSnake, DELAY)
    
# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Program Title")
screen.bgcolor("yellow")
# screen.tracer(0) # disables auto animation

# Create a turtle to do your bidding
mySnake = turtle.Turtle()
mySnake.shape("circle")
mySnake.color("cyan")
mySnake.shapesize(50 / 20)
mySnake.stamp()
mySnake.penup()
mySnake.shapesize(10 / 20)
mySnake.goto(100, 100)
mySnake.stamp()

# set animation
#moveSnake()

mySnake.forward(100)  # Sample command

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()