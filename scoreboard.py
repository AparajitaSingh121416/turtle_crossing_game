from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score=0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score:{self.score}",align="center",font=("Courier",20,"normal"))

    def car_hit(self):
        self.score += 1
        self.update_scoreboard()