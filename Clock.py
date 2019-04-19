#Importing the modules
import time
import turtle

# Create the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Clock")
wn.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

# Draw the clock
def drawclock(h, m, s, pen):

    pen.penup()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):

        pen.fd(190)
        pen.down()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # Draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

# Update the clock
while True:

    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    drawclock(h, m, s, pen)

    wn.update()

    time.sleep(1)

    pen.clear()

# Keep the window open
wn.mainloop()
