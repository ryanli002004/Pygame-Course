import pygame
import os
pygame.init()

display_surface = pygame.display.set_mode((600,300))
pygame.display.set_caption("Discrete Movement")

dragon_image = pygame.image.load(os.path.join("tutorial", "dragon_right.png"))
VELOCITY = 10

dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = 300
dragon_rect.bottom = 300

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)
    pygame.display.update()

pygame.quit()