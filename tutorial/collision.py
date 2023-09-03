import pygame
import random

pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 300
surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Collision!")

FPS = 60
clock = pygame.time.Clock()
VELOCITY = 10

dragon = pygame.image.load("tutorial/dragon_right.png")
dragonrect = dragon.get_rect()
dragonrect.topleft = (25,25)

coin = pygame.image.load("tutorial/coin.png")
coinrect = coin.get_rect()
coinrect.center = (WINDOWWIDTH//2,WINDOWHEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and dragonrect.left >0:
        dragonrect.x -= VELOCITY
    if keys[pygame.K_d] and dragonrect.right < WINDOWWIDTH:
        dragonrect.x += VELOCITY
    if keys[pygame.K_w] and dragonrect.top >0:
        dragonrect.y -= VELOCITY
    if keys[pygame.K_s] and dragonrect.bottom < WINDOWHEIGHT:
        dragonrect.y += VELOCITY
    if dragonrect.colliderect(coinrect):
        print("HIT")
        coinrect.x = random.randint(0,WINDOWWIDTH -32)
        coinrect.y = random.randint(0,WINDOWHEIGHT-32)
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0,255,0), dragonrect , 1)
    pygame.draw.rect(surface, (255,255,0),coinrect, 1)
    surface.blit(dragon, dragonrect)
    surface.blit(coin, coinrect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()