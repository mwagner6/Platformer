import pygame

class Block(object):
    def __init__(self, x, y, v, w):
        self.x = x
        self.y = y
        self.v = v
        self.w = w
        self.h = 20

    def draw(self, win):
        pygame.draw.rect(win, (120, 0, 0), (self.x, self.y, self.w, self.h))
    
    def move(self):
        self.x -= self.v