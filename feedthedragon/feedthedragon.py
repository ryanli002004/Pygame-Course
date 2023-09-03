import pygame
pygame.init()

WINDOWW = 1000
WINDOWH = 400
display_surface = pygame.display.set_mode((WINDOWW, WINDOWH))
pygame.display.set_caption("Feed the Dragon")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit() 
