
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

        self.shapesize(2,2)

 #   def move(self):
  #       new_x = self.xcor()+10
   #      new_y = self.ycor()+10
    #     self.goto(new_x,new_y)

    def bounce_top_right(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto( new_x, new_y)

    def bounce_top_left(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def bounce_RPAD_top_down(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)


    def move(self):
        x_dir = self.xcor() + self.x
        y_dir = self.ycor() + self.y
        self.goto(x_dir, y_dir)

    def bounce(self):
        self.y *= -1



