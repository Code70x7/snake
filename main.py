#instructions for game:  Green pellet is worth 2 points,  
#Blue pellet is worth 1 point. Red pellet speeds the snake up. Enjoy!

#code imports the necessary modules and classes to set up and run the snake game.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from powerup import PowerUp
from bonus_food import BonusFood
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600) # Set the screen size to 600x600 pixels
screen.bgcolor("black") # Set the background color to black
screen.title("My Snake Game") # Set the window title to "My Snake Game"
screen.tracer(0) # Disable automatic screen updates to control when the screen updates

# Create instances of the Snake, Food, Scoreboard, PowerUp, and BonusFood classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()
powerup = PowerUp()
bonus_food = BonusFood()

# Set up key listeners for snake movement control
screen.listen()
screen.onkey(snake.up, "Up") # Bind the "Up" key to the snake's up/down/left/right movement method
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True # Set a flag to keep the game running
speed = 0.1  # Initial game speed (the delay between each game loop iteration)

# Game loop to keep the game running until a "game over" condition is met
while game_is_on:
    screen.update() # Update the screen manually (because screen.tracer(0) was set)
    time.sleep(speed)  # Pause the game for a short time to control the game speed

    snake.move() # Move the snake in the current direction

  #detect collision with food - can put it to 10 if you don't want it as accurate
    if snake.head.distance(food) < 15: # Check if the snake's head is close enough to the food
        food.refresh() # Move the food to a new random location

        #snake exends itself
        snake.extend()

        #increases score everytime snake eats food
        scoreboard.increase_score()
 
    #Detect collision with power-up
    if snake.head.distance(powerup) < 15:
        powerup.refresh()
        speed *= 0.9  # Increase speed by reducing sleep time

          # Detect collision with bonus food
    if snake.head.distance(bonus_food) < 15:# Check if the snake's head is close enough to the power-up
        bonus_food.refresh()# Move the bonus food to a new random location
        snake.extend() # Add a new segment to the snake's body
        scoreboard.increase_score(2)  # Increase score by 2

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False # End the game if the snake hits the wall
        scoreboard.game_over() # Display the "Game Over" message

    #Detect collision with tail.
    for segment in snake.segments: # Check if any part of the snake's body (except the head) intersects with the head
        if segment == snake.head: # Skip the head itself
            pass
        elif snake.head.distance(segment) < 10:# Check if the head is close enough to any body segment
            game_is_on = False # End the game if the head collides with the tail
            scoreboard.game_over() # Display the "Game Over" message
# Wait for the user to click on the screen before closing the game window
screen.exitonclick()
