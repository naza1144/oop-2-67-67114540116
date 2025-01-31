import pygame 
from pygame import Color

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Mygame")
clock = pygame.time.Clock()
runing = True
frame = 0

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        magenta = Color(255,0,255)
        black = Color(0,0,0)
        react = pygame.Rect(20,50,200,300)
        screen.fill(black)
        
        pygame.draw.rect(screen,magenta,react)
        pygame.display.flip()
        clock.tick(30)
pygame.quit()