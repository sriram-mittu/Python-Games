import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("white.gif")
wn.tracer(3)

mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)

score = 0

maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("white")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def speedboost():
    global speed
    speed += 1

def turnback():
    player.right(180)

def collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speedboost, "Up")
turtle.onkey(turnback, "Down")

while True:
    player.forward(speed)

    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    for count in range(maxGoals):
        goals[count].forward(1)

        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        if collision(player, goals[count]):
            goals[count].setposition(random.randint(-280, 280), random.randint(-280, 280))
            goals[count].right(random.randint(0, 360))
            score += 1
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("arial",14,"normal"))
