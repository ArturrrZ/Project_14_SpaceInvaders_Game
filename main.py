import turtle as tr
from gamer import  Gamer
import time
from bullets import Bullets
screen=tr.Screen()
screen.title('Space Invaders Game')
screen.setup(width=720,height=576)
screen.bgcolor('black')
screen.tracer(0)

gamer=Gamer()
bullets=[]
def create_bullet():
    bullets.append(Bullets(gamer.xcor()))
screen.listen()
screen.onkey(gamer.go_left, 'a')
screen.onkey(gamer.go_right,'d')
screen.onkey(gamer.go_right,'Right')
screen.onkey(gamer.go_left,'Left')
screen.onkey(create_bullet,'space')
game_is_on=True

while game_is_on:
    time.sleep(0.05)
    screen.update()

    print(bullets)

    for each in bullets:
        each.goto(x=each.xcor(),y=each.ycor() + 10)










screen.exitonclick()

