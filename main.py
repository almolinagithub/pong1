import turtle
import paddles

width = 800
height = 600
x = 330
y = 0

screen = turtle.Screen()
screen.setup(width, height)
screen.screensize(width, height)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.listen()




paddle_right = paddles.Paddle()
paddle_right.goto(x,y)

paddle_left = paddles.Paddle()
paddle_left.goto(-x,0)

screen.onkey(lambda :paddle_right.forward(40), "Up")


screen.update()
screen.exitonclick()

