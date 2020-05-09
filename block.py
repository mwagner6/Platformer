import pygame
import random

class Block(object):
    def __init__(self, x, y, v, w):
        self.x = x
        self.y = y
        self.v = v
        self.w = w
        self.h = 20
        rand = random.random() - 0.5
        self.dir = rand / abs(rand)
        if self.dir < 0:
            self.x = 0 - self.w

    def draw(self, win):
        pygame.draw.rect(win, (120, 0, 0), (self.x, self.y, self.w, self.h))
    
    def move(self):
        self.x -= self.v * self.dir