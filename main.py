import time
import turtle
from ball import Ball
from paddles import Paddle
from time import sleep

height = 600
width = 800

PLAYING  = True

x = 330
y = 0

screen = turtle.Screen()
screen.setup(width, height)
screen.screensize(width, height)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()


#top and bottom of the screen
top = screen.window_height() / 2
right = screen.window_width() / 2
bottom = - top
left = - right

#making the paddles
paddle_right = Paddle((x, 0))
paddle_left = Paddle((-x, 0))

#set paddles positions
new_x = paddle_right.xcor() + 330
paddle_right.goto(new_x,y)
new_x = paddle_left.xcor() - 330
paddle_left.goto(new_x,y)

#moving the paddles
turtle.onkey(paddle_right.move_right, "Up")
turtle.onkey(paddle_right.move_left, "Down")
turtle.onkey(paddle_left.move_right, "a")
turtle.onkey(paddle_left.move_left, "z")

#create the ball
ball = Ball()


while PLAYING:
    time.sleep(0)
    screen.update()
    screen.tracer(1)
    ball.move()
    if ball.ycor() > top - 30 or ball.ycor() < bottom + 30:
        ball.bounce_y()
    elif ball.xcor() == right - 50 and ball.distance(paddle_right) == 20:
        ball.bounce_x()

    print(ball.xcor(),ball.ycor())


screen.exitonclick()

