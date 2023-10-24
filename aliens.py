
from turtle import Turtle


class Aliens(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('red')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(x,y)