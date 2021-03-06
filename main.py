#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#It'll be a simple snake game.                                    #
#Its one of my first games ever built in any programming language!#
#I'm pretty hyped, so i wish that if you're testing this,         #
#You be a little patient and complacent                           #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from turtle import Screen, Turtle, isvisible
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

scoreboard = Score()

gameison = True


while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detecting when food is eaten!!
    if snake.head.distance(food) < 15:
        print('yummy')
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    #detecting when hitting the wall!
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -300:
        scoreboard.reset()
        print('Game is over.')
        snake.reset()

    #detect colision with tail!
    for i in snake.squares[1:]:    
        if snake.head.distance(i) < 15:
            scoreboard.reset()
            snake.reset()
    
    scoreboard.save_highscore()
    
screen.exitonclick()


    
