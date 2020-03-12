import pygame
import os
from ball import Ball
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

def printcontrols():
    pass

def main():
    printcontrols()
    pygame.display.init()
    size = (900,600)
    screen = pygame.display.set_mode(size)
    colorscheme = 1
    balls = []
    for i in range(250):
        balls.append(Ball(screen, (0,0),(0,0)))
        balls[i].random(size)
    pygame.key.set_repeat(30)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.unicode == "b":
                    for ball in balls:
                        ball.burst(size)
                elif event.unicode == "r":
                    for ball in balls:
                        ball.random(size)
                elif event.unicode >= "1" and event.unicode <= "9":
                    colorscheme = int(event.unicode)
                elif event.unicode == '-':
                    for _ in range(10):
                        if len(balls) > 0:
                            _ = balls.pop(-1)
                elif event.unicode == '+':
                    for _ in range(10):
                        balls.append(Ball(screen,(0,0), (0,0)))
                        balls[-1].random(size)
        screen.fill((0,0,0))
        for ball in balls:
            ball.update(size)
            ball.draw(colorscheme)
        pygame.display.update()

if __name__ == "__main__":
    main()
