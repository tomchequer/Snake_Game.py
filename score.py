from turtle import Turtle, mode
from food import Food
from snake import Snake
with open('data.txt', "r") as hsdata:
    ranking = hsdata.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = ranking
        self.color('green')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"score:{self.score} highscore:{self.highscore}", align ='center', font=('Courier', 24, 'normal')) 
        
    
    
    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
        self.score = 0
        self.update()
        
        
    def increase_score(self):
        self.score += 1
        self.update()
        
    def save_highscore(self):
        with open('data.txt', mode='w') as hs:  
           hs.write(str(self.highscore))
    
    
    
        