# Import the modules
import turtle
import time
import random

# Set the score at the beginning
score = 0
high_score = 0

# Set the speed of the turtle
delay = 0.05

# Setup the screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Register the shapes
wn.register_shape("body.gif")
wn.register_shape("left.gif")
wn.register_shape("right.gif")
wn.register_shape("up.gif")
wn.register_shape("down.gif")
wn.register_shape("circle.gif")
wn.register_shape("apple.gif")

# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("lightblue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.color("grey")
food.penup()
food.goto(0, 100)

# Create the snake body
segments = []

# Create the pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Write the score and the high score
pen.write("   Score: 0 | High Score: 0", align="center",
 font=("Calibri", 24, "normal"))

# Create the key binding functions
def up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("up.gif")

def down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("down.gif")

def right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("right.gif")

def left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("left.gif")

# Create the function that moves the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Setup the keyboard bindings
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

# Main game loop
while True:
    # Update the screen
    wn.update()

    # Check for collision with the border
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
        
    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a new position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment
        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("body.gif")
        ns.color("white")
        ns.penup()
        segments.append(ns)

        # Shorten the delay
        delay -= 0.0001

        # Increase the score
        score += 1

        # Increase the high score
        if score > high_score:
            high_score = score

        # Rewrite the scores
        pen.clear()
        pen.write("   Score: {} | High Score: {}".format(score,
         high_score), align="center", font=("Calibri", 24, "normal"))
        
    # Move the snake body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move the sanke body (Part two)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the snake head
    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Move the segments off the screen
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments
            segments.clear()

            # Reset the speed of the snake
            delay = 0.05

            # Reset the score
            score = 0
            
            # Rewrite the score
            pen.clear()
            pen.write("   Score: {} | High Score: {}".format(score,
             high_score), align="center", font=("Calibri", 24, "normal"))

    # Set the speed of the snake
    time.sleep(delay)

# Keep the window open
wn.mainloop()
