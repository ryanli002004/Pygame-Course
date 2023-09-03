import pygame
import os
pygame.init()

WINDOWW = 1000
WINDOWH = 400
display_surface = pygame.display.set_mode((WINDOWW, WINDOWH))
pygame.display.set_caption("Feed the Dragon")

FPS = 60
clock = pygame.time.Clock()

STARTING_LIVES = 5
PLAYER_VEL = 5
COIN_VEL = 5
COIN_ACC = .5
BUFFER_DIS = 100

score = 0
player_lives = STARTING_LIVES
coin_vel = COIN_VEL

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.Font(os.path.join("tutoria","AttackGraffiti.ttf"))

scoretext = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
scorerect = scoretext.getrect()
scorerect.topleft = (10,10)

titletext = font.render("Feed The Dragon", True, GREEN, WHITE)
titlerect = titletext.get_rect()
titlerect.centerx = WINDOWW//2
titlerect.y = 10

livestext = font.render("Lives: " +str(player_lives), True, GREEN, DARKGREEN)
livesrect = livestext.get_rect()
livesrect.topright = (WINDOWW -10 , 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit() 
