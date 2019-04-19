import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.setup(width=640, height=640)
wn.tracer(0)

gravity = 0.1

balls = []
for _ in range(25):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "blue", "purple", "white"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

while True:

    wn.update()
    time.sleep(0.01)

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # Check for wall collision
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1

        # Check for a bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1

wn.mainloop()
