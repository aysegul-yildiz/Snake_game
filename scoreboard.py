from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score}  Highscore = {self.highscore}", align="center", font=("Calibri", 20, "normal"))

    def increase(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}  Highscore = {self.highscore}",align="center",font=("Calibri", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",mode="w") as file:
                file.write(f"self.highscore")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  Highscore = {self.highscore}", align="center", font=("Calibri", 20, "normal"))
