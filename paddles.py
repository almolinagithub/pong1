
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(2,10,8)
        self.width(20)


    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.back(20)
