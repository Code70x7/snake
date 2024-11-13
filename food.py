from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Creates the snake
snake = Snake()
#Creates Food class
food = Food()
#need to bind the onkey to the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

  #moves the snake
    snake.move()

  #detect collision with food - can put it to 10 if you don't want it as accurate
    if snake.head.distance(food) < 15:
      food.refresh()