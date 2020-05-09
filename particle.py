import pygame

class Particle(object):
    def __init__(self, x, y, xv, yv, r, g, b):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.r = r
        self.g = g
        self.b = b
        self.ra = 1
        self.life = 20

    def draw(self, win):
        pygame.draw.circle(win, (self.r, self.g, self.b), (int(self.x), int(self.y)), self.ra)
    
    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.yv += 0.1
        self.life -= 1