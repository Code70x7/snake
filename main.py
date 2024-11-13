#instructions for game:  Green pellet is worth 2 points,  
#Blue pellet is worth 1 point. Red pellet speeds the snake up. Enjoy!

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from powerup import PowerUp
from bonus_food import BonusFood
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
powerup = PowerUp()
bonus_food = BonusFood()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
speed = 0.1  # Initial game speed

while game_is_on:
    screen.update()
    time.sleep(speed)  # Use speed here

    snake.move()

  #detect collision with food - can put it to 10 if you don't want it as accurate
    if snake.head.distance(food) < 15:
        food.refresh()

        #snake exends itself
        snake.extend()

        #increases score everytime snake eats food
        scoreboard.increase_score()
 
    #Detect collision with power-up
    if snake.head.distance(powerup) < 15:
        powerup.refresh()
        speed *= 0.9  # Increase speed by reducing sleep time

          # Detect collision with bonus food
    if snake.head.distance(bonus_food) < 15:
        bonus_food.refresh()
        snake.extend()
        scoreboard.increase_score(2)  # Increase score by 2

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
