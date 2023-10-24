
from turtle import Turtle


class Aliens(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('red')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.goto(x,y)
        self.xmove=1
        self.ymove=0

    def move_horiz(self):
        new_x=self.xcor() + self.xmove
        y=self.ycor() + self.ymove
        self.goto(new_x,y)
    def flip_x(self):
        self.xmove *= -1
