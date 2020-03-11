import pygame
import os
from ball import Ball
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = (900,600)
screen = pygame.display.set_mode(size)
balls = []
for i in range(250):
    balls.append(Ball(screen, (0,0),(0,0)))
    balls[i].random(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for ball in balls:
        ball.update(size)
        ball.draw()
    pygame.display.update()
