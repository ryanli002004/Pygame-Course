import pygame
import os

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption ("Bitting images")

dragon_left_image = pygame.image.load(os.path.join("tutorial","dragon_left.png"))
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load(os.path.join("tutorial","dragon_right.png"))
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH,0)

pygame.draw.line(display_surface, (255,255,255), (0,75), (WINDOW_WIDTH, 75), 5)

running = True
while running:
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()