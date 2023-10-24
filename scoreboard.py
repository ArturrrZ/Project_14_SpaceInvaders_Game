from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center',font=('Courier',20,'normal'))

