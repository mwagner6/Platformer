import pygame
import math
import numpy as np

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 120
        self.g = 0
        self.b = 0
        self.ra = 12
        self.life = 45

    def draw(self, win):
        pygame.draw.circle(win, (self.r, self.g, self.b), (int(self.x), int(self.y)), self.ra)
    
    def move(self, playerx, playery):
        distance = math.sqrt(abs(playerx-self.x)**2 + abs(playery-self.y)**2)
        self.x += ((playerx-self.x)/distance)*2
        self.y += ((playery-self.y)/distance)*2