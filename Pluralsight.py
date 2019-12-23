import pygame, sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

gsans = pygame.font.SysFont("Product Sans", 48)

helloWorld = gsans.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

hws = helloWorld.get_size()

x, y = 0, 0

dirX, dirY = 1, 1

clock = pygame.time.Clock()

while 1:

        clock.tick(75)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()

        screen.fill((0, 0, 100))

        screen.blit(helloWorld, (x, y))

        if x > 800:
                x +100

        x += 5 * dirX
        y += 5 * dirY

        if x + hws[0] > 800 or x <= 0:
                dirX *= -1

        if y + hws[1] > 600 or y <= 0:
                dirY *= -1

        pygame.display.update()
