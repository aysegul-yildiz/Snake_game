from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun= snake.left, key = "Left")
screen.onkey(fun = snake.right, key= "Right")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.update_place()
        snake.grow()
        score.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()