import turtle
import time
import random

delay = 0.075

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "up"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Verdana", 24, "normal"))


def mvup():
    if head.direction != "down":
        head.direction = "up"


def mvdn():
    if head.direction != "up":
        head.direction = "down"


def mvlft():
    if head.direction != "right":
        head.direction = "left"


def mvrt():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

wn.listen()
wn.onkeypress(mvup, "Up")
wn.onkeypress(mvrt, "Right")
wn.onkeypress(mvlft, "Left")
wn.onkeypress(mvdn, "Down")

while True:
    wn.update()

    if head.xcor() > 290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x - 600, y)

    if head.xcor() < -290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x + 600, y)

    if head.ycor() > 290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x, y - 600)

    if head.ycor() < -290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x, y + 600)

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        score += 1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Verdana", 24, "normal"))

        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.color("white")
        ns.penup()
        segments.append(ns)

    if 0 < len(segments):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            score = 0

            pen.clear()
            pen.write("Score: {} ".format(score),
                      align="center", font=("Verdana", 24, "normal"))
            
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)

wn.mainloop()
