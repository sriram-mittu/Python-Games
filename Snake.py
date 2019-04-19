# Import the modules
import pygame
import sys
import random
import time

# Create the snakes attributes and functions
class Snakebody():
    # Create the snakes attributes
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction
        
    # Create the changing direction function
    def changeDirTo(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
            
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"

        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"

        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    # Create the function that moves the snake
    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        
        if self.direction == "LEFT":
            self.position[0] -= 10

        if self.direction == "UP":
            self.position[1] -= 10

        if self.direction == "DOWN":
            self.position[1] += 10

        # Create a variable that finds the position of the snake
        self.body.insert(0, list(self.position))
        
        # Check if the snake has collided with the food
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

     # Check for collisions with its body
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
             
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1

        for bodyPart in self.body[1]:
            if self.position == bodyPart:
                return 1
        return 0

     # Get the positions of all body parts
    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body

# Spawn the food
class FoodSpawner():
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randint(1, 50) * 10, random.randint(1, 50) * 10]
            self.isFoodOnScreen()
        return self.position

    def setFoodOnScreen(self):
        self.isFoodOnScreen = True

# Set up the display
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake | Score : 0")
fps = pygame.time.Clock()

# Set the score that you start with
score = 0

# Run the functions
foodSpawner = FoodSpawner()

# Create the game over function
def gameOver():
    pygame.quit()
    sys.exit()

snake = Snakebody()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            if event.key == pygame.K_UP:
                snake.direction = "UP"
            if event.key == pygame.K_DOWN:
                snake.direction = "DOWN"

    foodPos = foodSpawner.spawnFood()

    if snake.move(foodPos) == 1:
        score += 1
        foodSpawner.spawnFood()

    window.fill(pygame.Color(225, 225, 225))

    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0, 225, 0),pygame.Rect(pos[0],pos[1], 10, 10))
    pygame.draw.rect(window, pygame.Color(0, 225, 0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if(snake.checkCollision()==1):
        foodSpawner.spawnFood()
        gameOver()

    pygame.display.set_caption("Snake | Score : "+ str(score) )
    pygame.display.flip()
    fps.tick(5)
