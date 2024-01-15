from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake= []
        self.createSnake()
        self.head = self.snake[0]

    def createSnake(self):
        for position in POSITIONS:
            self.add_snakePart(position)

    def add_snakePart(self,position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake.append(snake_part)

    def grow(self):
        self.add_snakePart(self.snake[-1].position())

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num-1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x,new_y)
        self.head.forward(DISTANCE)

    def reset(self):
        for s in self.snake:
            s.goto(1000,1000)
        self.snake.clear()
        self.createSnake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

