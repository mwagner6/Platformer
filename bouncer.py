import pygame
import math
import numpy as np

class Bouncer(object):
    def __init__(self, y, rad):
        if rad >= 0.5:
            self.dir = 1
            self.x = -10
        else:
            self.dir = -1
            self.x = 710
        self.y = y
        self.r = 160
        self.g = 0
        self.b = 0
        self.ra = 17
        self.xv = 2
        self.yv = 0
        self.bouncercount = 5

    def draw(self, win):
        pygame.draw.circle(win, (self.r, self.g, self.b), (int(self.x), int(self.y)), self.ra)
    
    def move(self):
        self.x += self.xv * self.dir
        self.y += self.yv
        self.yv += 0.1
        if self.y >= 483 and self.bouncercount <= 0:
            self.yv = self.yv * -0.9
            self.bouncercount = 5
        self.bouncercount -= 1