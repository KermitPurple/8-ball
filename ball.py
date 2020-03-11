import pygame

class Ball:
    def __init__(self, screen, pos = (0,0), vel = (0,0)):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.r = 10
    
    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

    def draw(self):
        p = (int(self.pos[0]),int(self.pos[1]))
        pygame.draw.circle(self.screen, (255,255,255), p, self.r)
