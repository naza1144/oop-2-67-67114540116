import pygame 
from pygame import Color
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 400))
#name game
pygame.display.set_caption("Pygame Mygame")
#lock frame rate
clock = pygame.time.Clock()
#load image
sheet = pygame.image.load("pygame\Tiny_Swords\spritesheet.png")
runing = True
frame = 0
x, y = 20,40
speed = 10


while runing:
    for e in pygame.event.get():
        if e.type == QUIT:
            runing = False
        # if e.type == KEYDOWN:
        #     if e.key == K_a or e.key == K_LEFT:
        #         x -= speed
        #     elif e.key == K_d or e.key == K_RIGHT:
        #         x += speed
        #     elif e.key == K_w or e.key == K_UP:
        #         y -=  speed
        #     elif e.key == K_s or e.key == K_DOWN:
        #         y += speed
        key = pygame.key.get_pressed()
        if key[K_a] or key[K_LEFT]:
            x -= speed
        elif key[K_d] or key[K_RIGHT]:
            x += speed
        elif key[K_w] or key[K_UP]:
            y -=  speed
        elif key[K_s] or key[K_DOWN]:
            y += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    screen.fill((0,0,0))
    screen.blit(sheet,(x,y))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()