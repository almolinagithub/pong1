
from turtle import  Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width = 10
        self.hideturtle()
        self.penup()


    def score_writer_right(self, points):
        self.setpos(40, 260)
        self.clear()
        self.write(points)

    def score_writer_left(self, points):
        self.setpos(-40, 260)
        self.clear()
        self.write(points)


