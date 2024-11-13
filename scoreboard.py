# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Courier", 24, "normal")
# #setting up the font for the score board
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         #erases the line up the middle
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         #added variables for alignment and font
#         self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align=ALIGNMENT, font=FONT)
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()

# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self, points=1):  # Add points parameter with default value 1
        self.score += points
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
