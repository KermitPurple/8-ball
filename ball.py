import pygame
import random

class Ball:
    def __init__(self, screen, pos = (0,0), vel = (0,0)):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.r = 10
        self.friction = 0

    def collide(self, size):
        if self.pos[0] - self.r < 0 or self.pos[0] + self.r > size[0]:
            self.vel = (-self.vel[0], self.vel[1])
        elif self.pos[1] - self.r < 0 or self.pos[1] + self.r > size[1]:
            self.vel = (self.vel[0], -self.vel[1])
    
    def update(self, size):
        self.collide(size)
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        if self.vel[0] > 0:
            self.vel = (self.vel[0] - self.friction, self.vel[1])
        else:
            self.vel = (self.vel[0] + self.friction, self.vel[1])
        if self.vel[1] > 0:
            self.vel = (self.vel[0], self.vel[1] - self.friction)
        else:
            self.vel = (self.vel[0], self.vel[1] + self.friction)

    def random(self, size):
        self.randompos(size)
        self.randomvel()

    def burst(self, size):
        self.pos = (size[0]/2, size[1]/2)
        self.randomvel()

    def randompos(self, size):
        self.pos = (random.randrange(self.r,size[0]-self.r), random.randrange(self.r,size[1]-self.r))

    def randomvel(self):
        self.vel = (random.random() * random.randint(1,2) * random.choice([-1,1]), random.random() * random.randint(1,2) * random.choice([-1,1]))

    def draw(self, colorscheme):
        p = (int(self.pos[0]),int(self.pos[1]))
        color = pygame.Color(255,255,255)
        if colorscheme == 1:
            color.hsva = ((self.pos[0]+self.pos[1])%360, 100, 100)
        else: # default
            color.hsva = ((self.pos[0]+self.pos[1])%360, 100, 100)
        pygame.draw.circle(self.screen, color, p, self.r)
