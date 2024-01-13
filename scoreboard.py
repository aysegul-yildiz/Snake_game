from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Calibri", 20, "normal"))

    def increase(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Calibri", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", align="center", font=("Calibri", 20, "normal"))