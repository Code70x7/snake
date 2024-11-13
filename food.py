from turtle import Turtle
import random


class Food(Turtle):
    # Initializing the food object
    # making the size and color of the food pellet
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    # Refreshes the food's position to a new random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)