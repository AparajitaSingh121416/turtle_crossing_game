from turtle import Turtle,Screen
class Babyturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)

    def go_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_backward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x,self.ycor())
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
