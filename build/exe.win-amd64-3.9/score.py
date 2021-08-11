from turtle import Turtle
from food import Food
from snake import Snake


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update()
    
    def update(self):
        self.write(f"score: {self.score}", align ='center', font=('Courier', 24, 'normal')) 

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
        
    def gameover(self):
        self.goto(0, 0)
        self.write(f'Game over. Your final score was {self.score}.', align ='center', font=('Arial', 18, 'normal') )