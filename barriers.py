import turtle
from turtle import Turtle


class Barrier(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('darkgreen')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.goto(x,y)

        self.health=30
        self.health_score=turtle.Turtle()
        self.health_score.color('white')
        self.health_score.hideturtle()
        self.health_score.goto(x=x,y=y-30)
        self.write_health()

    def write_health(self):
        self.health_score.clear()
        self.health_score.write(self.health,align='center',font=('Courier',10,'normal'))

