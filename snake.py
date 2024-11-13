from turtle import Turtle
# Define constants for the starting positions of the snake and movement settings

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # Distance the snake moves each time
# Angle for moving up/down/left/right
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = [] # List to hold all segments of the snake
        self.create_snake() # Create the snake body using the starting positions
        self.head = self.segments[0] # Set the first segment (head) of the snake

    def create_snake(self):
        #creates snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)

   #adds segment to body
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
   #this will extend the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
                # Move the snake by updating the position of each segment

        for seg_num in range(len(self.segments) - 1, 0, -1):
            #moves snake forward- tail follows where head is going

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

#keystrokes indicate direction of the snake.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
