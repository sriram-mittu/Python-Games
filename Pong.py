import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

c = 0
d = 0

a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()
a.goto(-350, 0)

b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()
b.goto(350, 0)

ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

pen = turtle.Turtle()
pen.speed(0)
pen.color("gray")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Verdana", 24, "normal"))


def a_up():
    y = a.ycor()
    if a.ycor() < 300:
        y += 20
        a.sety(y)


def a_down():
    y = a.ycor()
    if a.ycor() > -300:
        y -= 20
        a.sety(y)


def b_up():
    y = b.ycor()
    if b.ycor() < 300:
        y += 20
        b.sety(y)


def b_down():
    y = b.ycor()
    if b.ycor() > -300:
        y -= 20
        b.sety(y)


wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 370:
        ball.goto(0, 0)
        c += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(c, d), align="center", font=("Verdana", 24, "normal"))

    if ball.xcor() < -370:
        ball.goto(0, 0)
        d += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(c, d), align="center", font=("Verdana", 24, "normal"))

    if (ball.xcor() > 340 and (ball.xcor() < 350)) and (ball.ycor() < b.ycor() + 40 and (ball.ycor() > b.ycor() -40)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and (ball.xcor() > -350)) and (ball.ycor() < a.ycor() + 40 and (ball.ycor() > a.ycor() -40)):
        ball.setx(-340)
        ball.dx *= -1
