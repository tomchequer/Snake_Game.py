#This is where the snake class is being created

from turtle import Turtle, Screen
import random

#constants
STARTING_AXIS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.squares = []  
        self.create_snake()
        self.head = self.squares[0]


    def create_snake(self):
        for i in STARTING_AXIS:
            self.add_square(i)

    
    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def extend(self):
        #add a new square to the snake
        self.add_square(self.squares[-1].position())
    
    def add_square (self, i):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(i)
        self.squares.append(new_square)
        
    def reset(self):
        for i in self.squares:
            i.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]