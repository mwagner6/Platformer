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

    def draw(self, win, life):
        pygame.draw.rect(win, (0, 125, 255), (self.x, self.y+5, self.w, self.h-10))
        pygame.draw.rect(win, (0, 125, 255), (self.x + 5, self.y, self.w-10, 5))
        pygame.draw.rect(win, (0, 125, 255), (self.x + 5, self.y + self.h - 5, self.w - 10, 5))
        pygame.draw.circle(win, (0, 125, 255), (int(self.x) + 5, int(self.y) + 5), 5)
        pygame.draw.circle(win, (0, 125, 255), (int(self.x) + self.w - 5, int(self.y) + 5), 5)
        pygame.draw.circle(win, (0, 125, 255), (int(self.x) + 5, int(self.y) + self.h - 5), 5)
        pygame.draw.circle(win, (0, 125, 255), (int(self.x) + self.w - 5, int(self.y) + self.h - 5), 5)
        pygame.draw.rect(win, (255, 0, 0), (self.x - 5, self.y - 15, 30, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.x - 5, self.y - 15, int(life/4), 5))

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