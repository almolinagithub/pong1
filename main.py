import turtle
import time
import paddles

PLAYING  = True

width = 800
height = 600
x = 330
y = 0

screen = turtle.Screen()
screen.setup(width, height)
screen.screensize(width, height)
screen.bgcolor("black")
screen.title("pong")

screen.listen()


while PLAYING:

    screen.update()
    time.sleep(0.2)
    paddle_right = paddles.Paddle()
    paddle_left = paddles.Paddle()

    paddle_right.goto(x,y)
    paddle_left.goto(-x,0)

    turtle.onkey(paddle_right.move_right, "Up")
    turtle.onkey(paddle_right.move_left, "Down")

    turtle.onkey(paddle_left.move_right, "a")
    turtle.onkey(paddle_left.move_left, "z")


    screen.exitonclick()

