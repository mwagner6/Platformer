import pygame

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.vel = 0
        self.xaccel = 0.2
        self.jumping = False
        self.jumptime = 15
        self.yaccel = 0.5
        self.yvel = 0
        self.dire = "Right"

    def draw(self, win):
        pygame.draw.rect(win, (0, 125, 255), (self.x, self.y, self.w, self.h))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 10:
            self.vel -= self.xaccel
            self.dire = "Left"
        if keys[pygame.K_RIGHT] and self.x < 690 - self.w:
            self.vel += self.xaccel
            self.dire = "Right"
        if keys[pygame.K_UP] and self.jumping == False:
            self.jumping = True
            self.yvel = 15
        if self.jumping == False:
            self.vel *= 0.95
        self.x += self.vel
        if self.x <= 0:
            self.x = 0
            self.vel = 0
        if self.x >= 700 - self.w:
            self.x = 700 - self.w
            self.vel = 0
        if self.jumping == True:
                self.yvel -= self.yaccel
                self.y -= self.yvel    
    
    def direc(self):
        return self.dire