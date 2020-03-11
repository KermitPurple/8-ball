import pygame
import os
from ball import Ball
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = (900,600)
screen = pygame.display.set_mode(size)
ball = Ball(screen, (size[0]/2, size[1]/2),(1.5,1.5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    ball.update(size)
    ball.draw()
    pygame.display.update()
