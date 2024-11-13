# powerup.py
from turtle import Turtle
import random

class PowerUp(Turtle):
        # Initializing the power-up object
    def __init__(self):
        super().__init__() # Calls the parent Turtle class constructor
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)  # Make it slightly larger than normal food
        self.color("red")  # Set a different color to distinguish it as a power-up
        self.speed("fastest")
        self.refresh()
    
    # Refreshes the power-up's position to a new random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)