
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

        self.shapesize(2,2)

    def move(self):
         new_x = self.xcor()+10
         new_y = self.ycor()+10
         self.goto(new_x,new_y)

    def bounce_top(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto( new_x, new_y)

