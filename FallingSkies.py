import turtle
import random
import os

score = 0
lives = 3

wn = turtle.Screen()
wn.bgpic("background.gif")
wn.title("Falling Skies")
wn.setup(width=800, height=600)
wn.tracer(20)

wn.register_shape("lion_left.gif")
wn.register_shape("lion_right.gif")
wn.register_shape("hunter.gif")
wn.register_shape("apple.gif")

player = turtle.Turtle()
player.speed(0)
player.penup()
player.goto(0, -250)
player.shape("lion_right.gif")
player.color("white")
player.direction = "stop"

goods = []

for _ in range(20):
    good = turtle.Turtle()
    good.speed(0)
    good.penup()
    x = random.randint(-380, 380)
    y = random.randint(300, 400)
    good.goto(x, y)
    good.shape("apple.gif")
    good.color("blue")
    good.speed = random.randint(1, 3)
    goods.append(good)

bads = []

for _ in range(10):
    bad = turtle.Turtle()
    bad.speed(0)
    bad.penup()
    x = random.randint(-380, 380)
    y = random.randint(300, 400)
    bad.goto(x, y)
    bad.shape("hunter.gif")
    bad.color("red")
    bad.speed = random.randint(1, 3)
    bads.append(bad)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.shape("square")
pen.color("white")
font = ("Verdana", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)



def left():
    player.direction = "left"
    player.shape("lion_left.gif")

def right():
    player.direction = "right"
    player.shape("lion_right.gif")

wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    wn.update()

    if lives < 1:
        bads.goto(0, 0)

    if player.direction == "left":
        x = player.xcor()
        x -= 1
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 1
        player.setx(x)

    px = player.xcor()
    if px > 380:
        player.setx(380)


    if px < -380:
        player.setx(-380)


    for good in goods:

        y = good.ycor()
        y -= good.speed
        good.sety(y)

        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 600)
            good.goto(x, y)


        if good.distance(player) < 27:
            x = random.randint(-380, 380)
            y = random.randint(300, 600)
            good.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    for bad in bads:

        y = bad.ycor()
        y -= bad.speed
        bad.sety(y)

        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 600)
            bad.goto(x, y)

        if bad.distance(player) < 30:
            x = random.randint(-380, 380)
            y = random.randint(300, 600)
            bad.goto(x, y)
            score -= 5
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
