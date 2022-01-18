import time
import turtle
from ball import Ball
from paddles import Paddle
from time import sleep

PLAYING  = True

height = 600
width = 800
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

#crate the ball
ball = Ball()


while PLAYING:
    time.sleep(0)
    screen.update()
    screen.tracer(1)
    if ball.xcor() <= top - 35:
        ball.move()
    else:
        ball.bounce_top()



screen.exitonclick()

