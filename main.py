#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#It'll be a simple snake game.                                    #
#Its one of my first games ever built in any programming language!#
#I'm pretty hyped, so i wish that if you're testing this,         #
#You be a little patient and complacent                           #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from turtle import Screen, Turtle, isvisible
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = []

starting_axis = [(0,0), (-20,0), (-40, 0)]

for i in starting_axis:
    new_square = Turtle('square')
    new_square.color('white')
    new_square.penup()
    new_square.goto(i)
    snake.append(new_square)
    

gameison = True

while gameison:
    screen.update()
    time.sleep(0.5)
    for i in range(len(snake) - 1, 0, -1):
        new_x = snake[i - 1].xcor()
        new_y = snake[i - 1].ycor()
        snake[i].goto(new_x, new_y)
    snake[0].forward(20)
        




screen.exitonclick()
