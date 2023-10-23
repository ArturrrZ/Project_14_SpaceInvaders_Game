from turtle import Turtle

class Gamer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.right(30)
        self.penup()
        self.shape('triangle')
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(x=0,y=-250)
        self.health=3

    def go_right(self):
        new_x=self.xcor() + 20
        self.goto(new_x,self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
