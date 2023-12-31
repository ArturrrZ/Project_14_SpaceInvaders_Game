import turtle as tr
from gamer import  Gamer
import time
from bullets import Bullets
from barriers import Barrier
from aliens import Aliens
from scoreboard import Scoreboard
import random
screen=tr.Screen()
screen.title('Space Invaders Game')
screen.setup(width=720,height=576)
screen.bgcolor('black')
screen.tracer(0)

gamer=Gamer()
bullets=[]
score=Scoreboard()


# def create_bullet():
#     bullets.append(Bullets(gamer.xcor()))

gamer_can_shoot = True
def enable_shooting():
    global gamer_can_shoot
    gamer_can_shoot = True

shoot_delay=100
def create_bullet():
    global gamer_can_shoot, shoot_delay
    if gamer_can_shoot:
        gamer_can_shoot = False
        bullets.append(Bullets(gamer.xcor()))
        tr.ontimer(enable_shooting,t= shoot_delay)
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

#columns of alien ships
alien_ships=[]
y=220
x=-280
for _ in range(10):

    for alien_ship in range(5):
        ship=Aliens(x,y)
        y-=40
        alien_ships.append(ship)
    x+=40
    y = 220

def move_aliens():
    global game_is_on
    for alien in alien_ships:
        alien.move_horiz()
        alien.ymove=0
        if alien_ships[len(alien_ships)-1].xcor() > 300 or alien_ships[0].xcor() < -300:
                alien.flip_x()
                alien.ymove -=40
        if alien.ycor() <-210:
            game_is_on=False
            score.goto(0,0)
            score.write('GAME IS OVER', align='center',font=('Courier',30,'bold'))

def write_level():
    level_turtle.clear()
    level_turtle.write(f"Your level: {LEVEL}",align='center',font=('Courier',10,'normal'))

LEVEL=0
level_turtle=tr.Turtle()
level_turtle.penup()
level_turtle.hideturtle()
level_turtle.color('white')
level_turtle.goto(250,240)
write_level()


chance_to_shoot=30
game_is_on=True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    if random.randint(0,chance_to_shoot)==1:
        # print('alien shoot')
        shooter=random.choice(alien_ships)
        bullet=Bullets(shooter.xcor())
        bullet.color('orange')
        bullet.goto(shooter.xcor(),shooter.ycor())
        bullet.alien_bullet=True
        bullets.append(bullet)

    move_aliens()

    for each in bullets:

        #move them forward
        if each.alien_bullet:
            each.goto(x=each.xcor(), y=each.ycor()  -10)
        else:
            each.goto(x=each.xcor(), y=each.ycor() + 10)
        #detect collision with barriers:
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

        #collision with aliens
        for ship in alien_ships:
            if each.alien_bullet == False:
                if ship.distance(each) < 20:
                    ship.hideturtle()

                    ship.goto(1000,1000)
                    alien_ships.remove(ship)
                    each.hideturtle()
                    bullets.remove(each)
                    each.goto(1000,1000)
                    score.score +=1
                    score.update_score()

        if each.alien_bullet and each.distance(gamer) < 20:
            print('MINUS LIFE')
            bullets.remove(each)
            each.hideturtle()
            gamer.health -=1
            gamer.update_health()
            if gamer.health ==0:
                game_is_on = False
                score.goto(0, 0)
                score.write('GAME IS OVER', align='center', font=('Courier', 30, 'bold'))



        #reload aliens,speed them up, level up, slow down delay for gamer
        if len(alien_ships) ==0:
            # columns of alien ships
            alien_ships = []
            y = 220
            x = -280
            for _ in range(10):

                for alien_ship in range(5):
                    ship = Aliens(x, y)
                    y -= 40
                    alien_ships.append(ship)
                x += 40
                y = 220
            shoot_delay += 200
            if chance_to_shoot > 10:
                chance_to_shoot -=10
            LEVEL +=1
            write_level()

















screen.exitonclick()

