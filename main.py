import turtle as tr
from gamer import Gamer

screen=tr.Screen()
screen.title('Space Invaders Game')
screen.setup(width=720,height=576)
screen.bgcolor('black')

gamer=Gamer()

screen.listen()

screen.onkey(gamer.go_left, 'a')
screen.onkey(gamer.go_right,'d')


screen.onkey(gamer.go_right,'Right')
screen.onkey(gamer.go_left,'Left')







screen.exitonclick()

