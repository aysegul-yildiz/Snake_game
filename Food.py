from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("pink")
        self.shapesize(0.5, 0.5)
        self.update_place()


    def update_place(self):
        new_x = random.randint(-265,265)
        new_y = random.randint(-265,265)
        self.goto(new_x, new_y)