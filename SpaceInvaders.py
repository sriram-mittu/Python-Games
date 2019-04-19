# Import the API's
import turtle
import os

# Create the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Create the border
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for side in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

# Create the player
player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("white")
player.shape("triangle")
player.setposition(0, -250)
player.setheading(90)

# Create the invaders
enemy = turtle.Turtle()
enemy.penup()
enemy.speed(0)
enemy.color("red")
enemy.shape("circle")
enemy.setposition(-200, 250)
enemy.setheading(180)

# Give the player a speed
speed = 15

# Give the invader a speed
enemy_speed = 15

# Move the player left and right
def left():
    x = player.xcor()
    x -= speed
    if x < -280:
        x = -280
    player.setx(x)

def right():
    x = player.xcor()
    x += speed
    if x > 280:
        x = 280
    player.setx(x)

# Create the keyboard bindings
wn.listen()
wn.onkey(left, "Left")
wn.onkey(right, "Right")

# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemy_speed

    if x > 280:
        x = enemy.xcor()
        y = enemy.ycor()
        enemy.ycor -= 40
        x *= -1
        enemy.setx(x)
        enemy.sety(y)

    if x < -280:
        x = enemy.xcor()
        y = enemy.ycor()
        x *= -1
        enemy.ycor -= 40
        enemy.setx(x)
        enemy.sety(y)

# Keep the window open
wn.mainloop()
