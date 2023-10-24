from turtle import Turtle

class Bullets(Turtle):
    def __init__(self,x_start):
        super().__init__()
        self.color('yellow')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=0.25, stretch_wid=0.5)
        self.goto(x=x_start,y=-230)
        self.alien_bullet=False

