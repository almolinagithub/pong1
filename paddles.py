
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=1, stretch_len= 10)

    def move_right(self):
        self.forward(10)

    def move_left(self):
        self.back(10)


