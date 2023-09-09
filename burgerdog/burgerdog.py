import pygame
import os
import random

pygame.init()

WINDOWW = 800
WINDOWH = 600
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("Burger dog")

FPS = 60
clock = pygame.time.Clock()
STARTINGLIVES = 3
PLAYERNORMALVEL = 5
PLAYERBOOSTVEL = 10
STARTINGBOOST = 100
BURGERSTARTINGVEL = 3
BURGERACC = .25
BUFFER = 100
score = 0
lives = STARTINGLIVES
burgerpoints = 0
burgerseaten = 0
playervel = PLAYERNORMALVEL
boostlevel = STARTINGBOOST
burgervel = BURGERSTARTINGVEL

ORANGE = (246,170,54)
BLACK = (0,0,0)
WHITE = (255,255,255)

barksound = pygame.mixer.Sound(os.path.join("burgerdog","bark_sound.wav"))
misssound = pygame.mixer.Sound(os.path.join("burgerdog","miss_sound.wav"))
pygame.mixer.music.load(os.path.join("burgerdog","bd_background_music.wav"))

font = pygame.font.Font(os.path.join("burgerdog","WashYourHand.ttf"),32)

burgerimage = pygame.image.load(os.path.join("burgerdog","burger.png"))
burgerrect = burgerimage.get_rect()
burgerrect.topleft = (random.randint(0,WINDOWW-32),-BUFFER)

dogleftimage = pygame.image.load(os.path.join("burgerdog","dog_left.png"))
dogrightimage = pygame.image.load(os.path.join("burgerdog","dog_right.png"))
dogimage = dogleftimage
dogrect = dogimage.get_rect()
dogrect.centerx = WINDOWW//2
dogrect.bottom = WINDOWH

pointstext = font.render("burger points: " +str(burgerpoints),True,ORANGE)
pointsrect = pointstext.get_rect()
pointsrect.topleft = (10,10)

titletext = font.render("Burger dog",True, ORANGE)
titlerect = titletext.get_rect()
titlerect.centerx = WINDOWW//2
titlerect.y = 10

scoretext = font.render("Score: "+str(score),True,ORANGE)
scorerect = scoretext.get_rect()
scorerect.topleft = (10,50)

livestext = font.render("lives: "+str(lives), True, ORANGE)
livesrect = livestext.get_rect()
livesrect.topright = (WINDOWW -10,10)

boosttext = font.render("Boost: " +str(boostlevel),True, ORANGE)
boostrect = boosttext.get_rect()
boostrect.topright = (WINDOWW-10, 50)

eatentext = font.render("Burgers eaten: "+ str(burgerseaten), True, ORANGE)
eatenrect = eatentext.get_rect()
eatenrect.centerx = WINDOWW//2
eatenrect.y =50

gameovertext = font.render("FINAL SCORE: "+str(score),True,ORANGE)
gameoverrect = gameovertext.get_rect()
gameoverrect.center=(WINDOWW//2,WINDOWH//2)

continuetext = font.render("press any key to play again",True,ORANGE)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2, WINDOWH//2+64)


running = True
pygame.mixer.music.play(-1,0.0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and dogrect.left >0:
        dogrect.x -= playervel
        dogimage = dogleftimage
    if keys[pygame.K_d] and dogrect.right < WINDOWW:
        dogrect.x += playervel
        dogimage = dogrightimage
    if keys[pygame.K_w] and dogrect.top > 100:
        dogrect.y -= playervel
    if keys[pygame.K_s] and dogrect.bottom < WINDOWH:
        dogrect.y += playervel

    if keys[pygame.K_SPACE] and boostlevel > 0:
        playervel = PLAYERBOOSTVEL
        boostlevel -= 1
    else:
        playervel = PLAYERNORMALVEL

    burgerrect.y += burgervel
    burgerpoints = int(burgervel*(WINDOWH - burgerrect.y +100))
    if burgerrect.y > WINDOWH:
        lives -=1
        misssound.play()
        burgerrect.topleft = (random.randint(0,WINDOWW-32),-BUFFER)
        burgervel = BURGERSTARTINGVEL
        dogrect.centerx = WINDOWW//2
        dogrect.bottom = WINDOWH
        boostlevel = STARTINGBOOST

    if dogrect.colliderect(burgerrect):
        score += burgerpoints
        burgerseaten +=1
        barksound.play()

        burgerrect.topleft = (random.randint(0,WINDOWW-32),-BUFFER)
        burgervel += BURGERACC

        boostlevel +=25
    if boostlevel > STARTINGBOOST:
        boostlevel = STARTINGBOOST 

    scoretext = font.render("Score: "+str(score),True,ORANGE)
    boosttext = font.render("Boost: " +str(boostlevel),True, ORANGE)
    eatentext = font.render("Burgers eaten: "+ str(burgerseaten), True, ORANGE)
    pointstext = font.render("burger points: " +str(burgerpoints),True,ORANGE)
    livestext = font.render("lives: "+str(lives), True, ORANGE)

    if lives ==0:
        gameovertext = font.render("FINAL SCORE: "+str(score),True,ORANGE)
        window.blit(gameovertext,gameoverrect)
        window.blit(continuetext,continuerect)
        pygame.display.update()
        pygame.mixer.music.stop()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused == False
                    running == False
                if event.type == pygame.KEYDOWN:
                    score = 0
                    boostlevel = STARTINGBOOST
                    burgerseaten = 0
                    lives = STARTINGLIVES
                    burgervel = BURGERSTARTINGVEL
                    pygame.mixer.music.play(-1,0.0)
                    paused = False


    window.fill(BLACK)
    window.blit(pointstext,pointsrect)
    window.blit(titletext,titlerect)
    window.blit(scoretext,scorerect)
    window.blit(eatentext,eatenrect)
    window.blit(boosttext,boostrect)
    window.blit(livestext,livesrect)
    pygame.draw.line(window,WHITE,(0,100),(WINDOWW,100),3)
    window.blit(dogimage,dogrect)
    window.blit(burgerimage,burgerrect)
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()