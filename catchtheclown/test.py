import pygame
import random
import os
import math
import time

pygame.init()

WINDOWW = 945
WINDOWH = 600
window = pygame.display.set_mode((WINDOWW, WINDOWH))
pygame.display.set_caption("catch the clown")

FPS = 60
clock = pygame.time.Clock()

STARTINGLIVES = 5
STARTINGVEL = 5
CLOWNACC = 1

score = 0
lives = STARTINGLIVES
clownvel = STARTINGVEL
clowndx = random.choice([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
clowndy = random.choice([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

balanceby = math.sqrt(math.sqrt(2)/(abs(clowndx)**2+abs(clowndy)**2))


BLUE = (1,175,209)
YELLOW = (248,231,28)

font = pygame.font.Font(os.path.join("catchtheclown","Franxurter.ttf"),32)

titletext = font.render("Catch the Clown", True, BLUE)
titlerect = titletext.get_rect()
titlerect.topleft =(50,10)

scoretext = font.render("score :" +str(score), True, YELLOW)
scorerect = scoretext.get_rect()
scorerect.topright = (WINDOWW -50, 10)

livestext = font.render("lives: " + str(lives), True, YELLOW)
livesrect = livestext.get_rect()
livesrect.topright = (WINDOWW-50 , 50)
 
gameovertext = font.render("GAMEOVER",True, BLUE, YELLOW)
gameoverrect = gameovertext.get_rect()
gameoverrect.center = (WINDOWW//2,WINDOWH//2)

continuetext = font.render("click anywhere to play away", True, YELLOW, BLUE)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2,WINDOWH//2 +64)

clicksound = pygame.mixer.Sound(os.path.join("catchtheclown","click_sound.wav"))
misssound = pygame.mixer.Sound(os.path.join("catchtheclown","miss_sound.wav"))
pygame.mixer.music.load(os.path.join("catchtheclown","ctc_background_music.wav"))

backgroundimage = pygame.image.load(os.path.join("catchtheclown","background.png"))
backgroundrect = backgroundimage.get_rect()
backgroundrect.topleft = (0,0)

clownimage = pygame.image.load(os.path.join("catchtheclown","clown.png"))
clownrect = clownimage.get_rect()
clownrect.center = (WINDOWW//2,WINDOWH//2)



running = True
pygame.mixer.music.play(-1,0.0)
prevtime = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0]
            mousey = event.pos[1]
            if clownrect.collidepoint(mousex,mousey):
                currenttime = pygame.time.get_ticks()
                prevtime = currenttime
                timer = (currenttime - prevtime) / 1000.0
                print(math.sqrt((clownrect.x)**2 + (clownrect.y)**2)/timer)
                score += 1
                clicksound.play()
                clownvel += CLOWNACC
                prevx = clowndx
                prevy = clowndy
                while(prevx == clowndx and prevy == clowndy):
                    clowndx = random.choice ([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
                    clowndy = random.choice ([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
                    balanceby = math.sqrt(math.sqrt(2)/(abs(clowndx)**2+abs(clowndy)**2))
            else:
                lives -= 1
                misssound.play()


    clownrect.x +=  clowndx*clownvel*balanceby
    clownrect.y +=  clowndy*clownvel*balanceby

    if clownrect.left <= 0 or clownrect.right >= WINDOWW:
        clowndx = -1*clowndx
    if clownrect.top <=0 or clownrect.bottom >= WINDOWH:
        clowndy = -1*clowndy

    scoretext = font.render("score :" +str(score), True, YELLOW)
    livestext = font.render("lives: " + str(lives), True, YELLOW)

    if lives == 0:
        window.blit(gameovertext,gameoverrect)
        window.blit(continuetext,continuerect)
        pygame.display.update()

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    lives = STARTINGLIVES
                    clownvel = STARTINGVEL
                    clownrect.center = (WINDOWW//2,WINDOWH//2)
                    clowndx = random.choice ([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
                    clowndy = random.choice ([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
                    balanceby = math.sqrt(math.sqrt(2)/(abs(clowndx)**2+abs(clowndy)**2))
                    pygame.mixer.music.play(-1,0.0)
                    paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False

    

    window.blit(backgroundimage,backgroundrect)
    window.blit(titletext,titlerect)
    window.blit(scoretext,scorerect)
    window.blit(clownimage,clownrect)
    window.blit(livestext,livesrect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

