from turtle import Turtle
import random
COLOR=["red","blue","green","yellow","pink","magenta"]
class Cars():
    def __init__(self):
        self.all_cars=[]

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice==1:
            new_car= Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=3,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            new_car.goto(300,random.randint(-260,260))
            self.all_cars.append(new_car)

    def move_car(self):
        for j in self.all_cars:
            j.backward(10)
