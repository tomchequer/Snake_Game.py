import turtle


class Score(turtle.Turtle()):
    def __init__(self):
        super().__init__()
        self.write(f"score: {self.score}", allign ='center', font=('Arial', 24, 'normal')) 
        self.color('white')