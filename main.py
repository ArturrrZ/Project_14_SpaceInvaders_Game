import turtle as tr
from gamer import  Gamer
import time
from bullets import Bullets
from barriers import Barrier

screen=tr.Screen()
screen.title('Space Invaders Game')
screen.setup(width=720,height=576)
screen.bgcolor('black')
screen.tracer(0)

gamer=Gamer()
bullets=[]

# def create_bullet():
#     bullets.append(Bullets(gamer.xcor()))

gamer_can_shoot = True
def enable_shooting():
    global gamer_can_shoot
    gamer_can_shoot = True

def create_bullet():
    global gamer_can_shoot
    if gamer_can_shoot:
        gamer_can_shoot = False
        bullets.append(Bullets(gamer.xcor()))
        tr.ontimer(enable_shooting,t= 700)
def move_bullets():
    for each in bullets:
        each.goto(x=each.xcor(),y=each.ycor() + 10)

screen.listen()
screen.onkey(gamer.go_left, 'a')
screen.onkey(gamer.go_right,'d')
screen.onkey(gamer.go_right,'Right')
screen.onkey(gamer.go_left,'Left')
screen.onkey(create_bullet,'space')

barrier_left=Barrier(-240,-120)
barrier_middle=Barrier(0,-120)
barrier_right=Barrier(240,-120)

game_is_on=True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    move_bullets()











screen.exitonclick()

