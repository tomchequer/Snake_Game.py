#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#It'll be a simple snake game.                                    #
#Its one of my first games ever built in any programming language!#
#I'm pretty hyped, so i wish that if you're testing this,         #
#You be a little patient and complacent                           #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from turtle import Screen, Turtle, isvisible
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


gameison = True

while gameison:
    screen.update()
    time.sleep(0.5)
    
    snake.move()
    
        
screen.exitonclick()


