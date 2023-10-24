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

    for each in bullets:
        #move them forward
        each.goto(x=each.xcor(), y=each.ycor() + 10)
        if barrier_left.distance(each) < 50 and each.ycor() > -130:
            each.hideturtle()
            bullets.remove(each)
            if barrier_left.health ==1:
                barrier_left.goto(1000,1000)
                barrier_left.health_score.clear()
            else:
                barrier_left.health -=1
                barrier_left.write_health()

        if barrier_middle.distance(each) < 50 and each.ycor() > -130:
            each.hideturtle()
            bullets.remove(each)
            if barrier_middle.health ==1:
                barrier_middle.goto(1000,1000)
                barrier_middle.health_score.clear()
            else:
                barrier_middle.health -=1
                barrier_middle.write_health()

        if barrier_right.distance(each) < 50 and each.ycor() > -130:
            each.hideturtle()
            bullets.remove(each)
            if barrier_right.health ==1:
                barrier_right.goto(1000,1000)
                barrier_right.health_score.clear()
            else:
                barrier_right.health -=1
                barrier_right.write_health()












screen.exitonclick()

