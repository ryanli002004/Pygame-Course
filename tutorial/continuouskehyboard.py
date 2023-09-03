import pygame

pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 300
surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("continuous keyboard")
FPS = 60
clock = pygame.time.Clock()
dragon = pygame.image.load("tutorial/dragon_right.png")
dragonrect = dragon.get_rect()
dragonrect.center = (WINDOWWIDTH//2,WINDOWHEIGHT//2)
VELOCITY = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dragonrect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragonrect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragonrect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragonrect.y += VELOCITY
    surface.fill((0,0,0))
    surface.blit(dragon,dragonrect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()