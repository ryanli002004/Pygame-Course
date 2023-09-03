import pygame
import os
import random

pygame.init()

WINDOWW = 1000
WINDOWH = 400
display_surface = pygame.display.set_mode((WINDOWW, WINDOWH))
pygame.display.set_caption("Feed the Dragon")

FPS = 60
clock = pygame.time.Clock()

STARTING_LIVES = 1
PLAYER_VEL = 10
COIN_VEL = 10
COIN_ACC = 1
BUFFER_DIS = 100

score = 0
player_lives = STARTING_LIVES
coin_vel = COIN_VEL

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.Font(os.path.join("feedthedragon","AttackGraffiti.ttf"),32)

scoretext = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
scorerect = scoretext.get_rect()
scorerect.topleft = (10,10)

titletext = font.render("Feed The Dragon", True, GREEN, WHITE)
titlerect = titletext.get_rect()
titlerect.centerx = WINDOWW//2
titlerect.y = 10

livestext = font.render("Lives: " +str(player_lives), True, GREEN, DARKGREEN)
livesrect = livestext.get_rect()
livesrect.topright = (WINDOWW -10 , 10)

gameovertext = font.render("GAMEOVER", True, GREEN, DARKGREEN)
gameoverrect = gameovertext.get_rect()
gameoverrect.center = (WINDOWW//2, WINDOWH//2)

continuetext = font.render("Press any key to play again",True, GREEN, DARKGREEN)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2, WINDOWH//2 +32)

coinsound = pygame.mixer.Sound(os.path.join("feedthedragon","coin_sound.wav"))
misssound = pygame.mixer.Sound(os.path.join("feedthedragon","miss_sound.wav"))
misssound.set_volume(.1)
pygame.mixer.music.load(os.path.join("feedthedragon","ftd_background_music.wav"))

playerimage = pygame.image.load(os.path.join("feedthedragon","dragon_right.png"))
playerrect = playerimage.get_rect()
playerrect.left = 32
playerrect.centery = WINDOWH//2

coinimage = pygame.image.load(os.path.join("feedthedragon","coin.png"))
coinrect = coinimage.get_rect()
coinrect.x = WINDOWW + BUFFER_DIS
coinrect.y = random.randint(64, WINDOWH)

running = True
pygame.mixer.music.play(-1,0.0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and playerrect.top > 64:
        playerrect.y -= PLAYER_VEL
    if keys[pygame.K_s] and playerrect.bottom < WINDOWH:
        playerrect.y += PLAYER_VEL
    if coinrect.x < 0 :
        player_lives -= 1
        misssound.play()
        coinrect.x = WINDOWW + BUFFER_DIS
        coinrect.y = random.randint(64, WINDOWH -32)
    else:
        coinrect.x -= coin_vel
    if playerrect.colliderect(coinrect):
        score += 1
        coinsound.play()
        coin_vel += COIN_ACC
        coinrect.x = WINDOWW + BUFFER_DIS
        coinrect.y = random.randint(64, WINDOWH -32)
    
    scoretext = font.render("Score: "+ str(score), True, GREEN, DARKGREEN)
    livestext = font.render("Lives: "+ str(player_lives), True, GREEN,DARKGREEN)

    if player_lives == 0:
        display_surface.blit(gameovertext,gameoverrect)
        display_surface.blit(continuetext,continuerect)
        pygame.display.update()

        pygame.mixer.music.stop()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = STARTING_LIVES
                    playerrect.y = WINDOWH//2
                    coin_vel = COIN_VEL
                    pygame.mixer.music.play(-1,0.0)
                    paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
    livestext = font.render("Lives: "+str(player_lives), True, GREEN,DARKGREEN)
    pygame.display.update()


    display_surface.fill(BLACK)
    display_surface.blit(scoretext, scorerect)
    display_surface.blit(titletext,titlerect)
    display_surface.blit(livestext,livesrect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOWW, 64) ,2)
    display_surface.blit(playerimage,playerrect)
    display_surface.blit(coinimage,coinrect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit() 
