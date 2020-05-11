import pygame
import random

from player import Player
from block import Block
from bullet import Bullet
from particle import Particle
import pygame.gfxdraw

# this version will give you points when you are high up

# initialize lists
bullets = []
blocks = []
particles = []
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Max's Game")
done = False
counter = 120
dire = "Right"
btime = 15
timer = 15
score = 0
life = 120
pcounter = 3
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render(str(score), True, (0, 0, 0), (0, 0, 255))
textRect = text.get_rect()   
textRect.center = (350, 40)


clock = pygame.time.Clock()
player1 = Player(100, 460, 20, 40)
blocks.append(Block(699, 470, 0.5, 200))
def redraw():
    pygame.gfxdraw.box(screen, (0, 0, 700, 500), (0, 0, 0, 50))
    text = font.render("Score: " + str(score), True, (50, 50, 50), (0, 0, 0, 0))
    screen.blit(text, textRect)
    player1.draw(screen, life)
    for bullet in bullets:
        bullet.draw(screen)
    for block in blocks:
        block.draw(screen)
    for particle in particles:
        particle.draw(screen)
    pygame.display.update()
    
while not done:
    if timer > 0:
        timer -= 1
    else:
        if player1.y >= 150:   
            score += 1
        else:
            score += 4
            if life <= 117:
                life += 3
        timer = 15
    if player1.y <= 150:
        particles.append(Particle(player1.x + random.random()*20, player1.y + random.random()*40, (random.random()-0.5)*5, (random.random()-0.5)*5, 0, 200, 255))
    if btime < 15:
        btime += 1
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if counter > 0:
        counter -= 1
    else:
        counter = 90
        blocks.append(Block(699, random.random()*480, random.random()*5, random.random()*100+100))
    for block in blocks:
        block.move()
        if block.x >= 700 or block.x <= 0 - block.w:
            blocks.pop(blocks.index(block))
    if keys[pygame.K_SPACE] and btime == 15:
            btime = 0
            bullets.append(Bullet(player1.x + 10, player1.y + 15, player1.direc()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player1.jumping = True
    for block in blocks:
        if player1.x <= block.x-20 or player1.x >= block.x + block.w:
            if player1.jumping == False:
                #player1.jumping = True
                player1.yvel = 0
        if player1.y <= block.y-45 or player1.y >= block.y+21: 
            if player1.jumping == False:
                #player1.jumping = True
                player1.yvel = 0
        if player1.x >= block.x - 20 and player1.x <= block.x + block.w and player1.y >= block.y + 5 and player1.y < block.y + 20:
            player1.yvel = 0
            player1.y = block.y + 20
        if player1.x >= block.x - 20 and player1.x <= block.x + block.w and player1.y + player1.yvel >= block.y + 5 and player1.y + player1.yvel < block.y + 20:
            player1.yvel = 0
            player1.y = block.y + 20
        if player1.x >= block.x - 20 and player1.x <= block.x + block.w and player1.y < block.y - 25 and player1.y > block.y-40:
            player1.y = block.y - 41
            player1.jumping = False
            player1.yvel = 0
        if player1.x >= block.x - 20 and player1.x <= block.x + block.w and player1.y + 40 < block.y and player1.y + 40 > block.y - 5:
            player1.jumping = False
        if player1.x >= block.x - 19 and player1.x + 40 <= block.x + block.w and player1.y < block.y + block.h and player1.y + 40 >= block.y:
            player1.x = block.x - 20
            player1.vel = 0
        if player1.x <= block.x + block.w and player1.x > block.x + 20 and player1.y < block.y + block.h and player1.y + 40 >= block.y:
            player1.x = block.x + block.w
            player1.vel = 0

    for bullet in bullets:
        bullet.move()
        for block in blocks:
            if bullet.x >= block.x and bullet.x <= block.x + block.w and bullet.y >= block.y and bullet.y <= block.y + block.h:
                bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        if bullet.x >= 700 or bullet.x <= 0:
            bullets.pop(bullets.index(bullet))
    for particle in particles:
        particle.move()
        if particle.life <= 0:
            particles.pop(particles.index(particle))
    if player1.y >= 460:
        player1.y = 460
        player1.yvel = 0
        player1.jumping = False
        if score >= 3:
            particles.append(Particle(player1.x + random.random()*20, player1.y + random.random()*40, (random.random()-0.5)*5, (random.random()-0.5)*5, 255, 120, 0))
            life -= 1
    if life == 0:
        done = True

    player1.move()
    redraw()

    
pygame.quit()