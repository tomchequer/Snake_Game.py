#This is where the snake class is being created

from turtle import Turtle, Screen
import random

STARTING_AXIS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.squares = []  
        self.create_snake()
    
    def create_snake(self):
        for i in STARTING_AXIS:
            new_square = Turtle('square')
            new_square.color('white')
            new_square.penup()
            new_square.goto(i)
            self.squares.append(new_square)
    
    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

