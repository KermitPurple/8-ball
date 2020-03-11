import pygame

class Ball:
    def __init__(self, screen, x = 0, y = 0):
        self.screen = screen
        self.x = int(x)
        self.y = int(y)
        self.r = 10
    
    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (self.x,self.y), self.r)
