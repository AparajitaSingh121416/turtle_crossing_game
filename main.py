import time
from turtle import Turtle,Screen
from babyturtle import Babyturtle
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
tim = Babyturtle()
tim.left(90)
screen.listen()
screen.onkey(tim.go_forward,"Up")
screen.onkey(tim.go_backward,"Down")
screen.onkey(tim.go_right,"Right")
screen.onkey(tim.go_left,"Left")
car = Cars()
scoreboard = Scoreboard()
game_on=True
while game_on:
    time.sleep(0.08)
    screen.update()
    car.create_car()
    car.move_car()
    for i in car.all_cars:
        if tim.distance(i) < 10 and i.color() == ('blue','blue') :
            scoreboard.car_hit()













screen.exitonclick()
