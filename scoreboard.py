from turtle import Turtle

# Create the Scoreboard class which inherits from the Turtle class
class Scoreboard(Turtle):
    # Initialize the scoreboard, setting up the initial score and positioning
    def __init__(self):
        super().__init__() # Call the parent class (Turtle) constructor
        self.score = 0 # Set the initial score to 0
        self.hideturtle() # Hide the turtle cursor (since it's just used for text display)
        self.color("white") # Set the color of the score text to white
        self.penup() # Lift the pen so it doesn't draw lines
        self.goto(0, 270) # Position the scoreboard at the top of the screen
        self.update_scoreboard() # Update the scoreboard display

# Update the scoreboard by clearing the old score and writing the new score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

# Increase the score by a certain number of points (default is 1)
    def increase_score(self, points=1):  # Add points parameter with default value 1
        self.score += points
        self.update_scoreboard()


    # Display "GAME OVER" message at the center of the screen when the game ends
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
