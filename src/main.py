import pygame
from pygame.locals import *
from tmInputs.tmInput import TMInput

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])

inputs = [
    TMInput(0, 0, 1, 0),
    TMInput(10, 0.2, 1, 0),
    TMInput(20, 0.3, 0, 1),
    TMInput(30, 0.1, 1, 1),
]

inputOffset = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEWHEEL:
            if event.y > 0:
                print("scroll up")
            else:
                print("scroll down")
            print(event)

    for i in range(inputOffset, len(inputs)):
        pygame.draw.rect(screen, (255, 255, 255), (i * 50, 0, 50, 50))

    pygame.display.flip()

pygame.quit()
