
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid= 8 , stretch_len= 1)


