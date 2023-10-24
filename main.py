import turtle as tr
from gamer import  Gamer
import time
screen=tr.Screen()
screen.title('Space Invaders Game')
screen.setup(width=720,height=576)
screen.bgcolor('black')
screen.tracer(0)

gamer=Gamer()

screen.listen()
screen.onkey(gamer.go_left, 'a')
screen.onkey(gamer.go_right,'d')
screen.onkey(gamer.go_right,'Right')
screen.onkey(gamer.go_left,'Left')

game_is_on=True
while game_is_on:
    time.sleep(0.05)
    screen.update()









screen.exitonclick()

