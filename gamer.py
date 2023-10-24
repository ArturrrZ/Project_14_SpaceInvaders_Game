import turtle
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

        self.health_turtle=turtle.Turtle()
        self.health_turtle.hideturtle()
        self.health_turtle.color('white')
        self.health_turtle.penup()
        self.health_turtle.goto(-250,240)
        self.update_health()

    def go_right(self):
        if self.xcor() <=320:
            new_x=self.xcor() + 20
            self.goto(new_x,self.ycor())

    def go_left(self):
        if self.xcor() >= -320:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def update_health(self):
        self.health_turtle.clear()
        self.health_turtle.write(f"Your health: {self.health}",align='center',font=('Courier',10,'normal'))
