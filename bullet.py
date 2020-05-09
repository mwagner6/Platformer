import pygame

class Bullet(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.r = 4
        self.v = 15

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 120), (int(self.x), int(self.y)), self.r)
    
    def move(self):
        if self.d == "Right":
            self.x += self.v
        else:
            self.x -= self.v