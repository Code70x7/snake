# bonus_food.py
from turtle import Turtle
import random

# Create the BonusFood class which inherits from the Turtle class
class BonusFood(Turtle):
    # Initialize the bonus food, setting its appearance and position
    def __init__(self):
        super().__init__() # Call the parent class (Turtle) constructor
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)  # Smaller size than regular food
        self.color("green")
        self.speed("fastest")
        self.refresh()

    # Move the bonus food to a random position within the screen boundaries

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
