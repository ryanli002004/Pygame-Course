import pygame
import os

pygame.init()

WINDOW_WIDTH =  600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Mouse movement")

dragon_image = pygame.image.load(os.path.join("tutorial","dragon_right.png"))
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)
    pygame.display.update()

pygame.quit()