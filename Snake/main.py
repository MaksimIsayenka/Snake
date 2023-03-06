from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


COL_X = 290
COL_NEG_X= -290
COL_Y = 290
COL_NEG_Y = -290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Maksim Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #DETECT COLLISION WITH FOOD

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with wall
    if int(snake.head.xcor()) > COL_X or int(snake.head.xcor()) < COL_NEG_X or int(snake.head.ycor()) > COL_Y or int(snake.head.ycor()) < COL_NEG_Y:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
















screen.exitonclick()