
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

HEIGHT = 900
WIDTH = 900
screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


up_down = [snake.up, snake.down]
left_right = [snake.left, snake.right]

while True:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update()
        snake.add_to_tail()

    # detect collision with wall
    if snake.head.xcor() > WIDTH // 2 or snake.head.xcor() < -(WIDTH // 2) \
            or snake.head.ycor() > WIDTH // 2 or snake.head.ycor() < -(WIDTH // 2):
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # Rules for autoplay comment out if you want to play
    if snake.head.xcor() > (WIDTH // 2) - 30 and snake.head.heading() == 0:
        snake.up()
    elif snake.head.xcor() < -((WIDTH // 2) - 30) and snake.head.heading() == 180:
        snake.down()
    if snake.head.ycor() > (WIDTH // 2) - 30 and snake.head.heading() == 90:
        snake.left()
    elif snake.head.ycor() < -((WIDTH // 2) - 30) and snake.head.heading() == 270:
        snake.right()
    if abs(snake.head.xcor() - food.xcor()) < 10 and snake.head.ycor() > food.ycor():
        snake.down()
    elif abs(snake.head.xcor() - food.xcor()) < 10 and snake.head.ycor() < food.ycor():
        snake.up()
    elif abs(snake.head.ycor() - food.ycor()) < 10 and snake.head.xcor() > food.xcor():
        snake.left()
    elif abs(snake.head.ycor() - food.ycor()) < 10 and snake.head.xcor() < food.xcor():
        snake.right()

screen.exitonclick()
