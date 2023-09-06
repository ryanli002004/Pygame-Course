import pygame, random, os

pygame.init()

WINDOWW = 600
WINDOWH = 600
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("snake")

clock = pygame.time.Clock()
FPS = 20

SNAKESIZE = 20

headx = WINDOWW//2
heady = WINDOWH//2 +100
snakedx = 0
snakedy = 0

score = 0

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
RED = (255,0,0)
DARKRED = (150,0,0)
WHITE = (255,255,255)

font = pygame.font.SysFont('gabriola', 48)

titletext = font.render("Snake", True, GREEN, DARKRED)
titlerect = titletext.get_rect()
titlerect.center = (WINDOWW//2,WINDOWH//2)

scoretext = font.render("Score: " + str(score), True, GREEN, DARKRED)
scorerect = scoretext.get_rect()
scorerect.topleft = (0,0)

gameovertext = font.render("gameover", True, RED, DARKGREEN)
gameoverrect = gameovertext.get_rect()
gameoverrect.center = (WINDOWW//2, WINDOWH//2)

continuetext = font.render("press any key to play again", True, RED, DARKGREEN)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2, WINDOWH//2+64)

pickupsound = pygame.mixer.Sound(os.path.join("snake","pick_up_sound.wav"))

applecord = (500,500,SNAKESIZE,SNAKESIZE)
headcord = (headx, heady, SNAKESIZE,SNAKESIZE)
bodycord = []

applerect = pygame.draw.rect(window,RED,applecord)
headrect = pygame.draw.rect(window,GREEN, headcord)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snakedx = -1*SNAKESIZE
                snakedy = 0
            if event.key == pygame.K_d:
                snakedy = 0
                snakedx = 1*SNAKESIZE
            if event.key == pygame.K_w:
                snakedx = 0
                snakedy = -1*SNAKESIZE
            if event.key == pygame.K_s:
                snakedx = 0
                snakedy = 1*SNAKESIZE

    bodycord.insert(0,headcord)
    bodycord.pop()

    headx += snakedx
    heady += snakedy
    headcord = (headx,heady,SNAKESIZE,SNAKESIZE)
    
    if headrect.left <0 or headrect.right > WINDOWW or headrect.top < 0 or headrect.bottom > WINDOWH or headcord in bodycord:
        window.blit(gameovertext,gameoverrect)
        window.blit(continuetext,continuerect)
        pygame.display.update()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    headx = WINDOWW//2
                    heady = WINDOWH//2 +100
                    headcord = (headx,heady, SNAKESIZE,SNAKESIZE)
                    bodycord = []
                    snakedx = 0
                    snakedy=0
                    paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False

    if headrect.colliderect(applerect):
        score += 1
        pickupsound.play()
        applex = random.randint(0,WINDOWW - SNAKESIZE)
        appley = random.randint(0,WINDOWH-SNAKESIZE)
        applecord = (applex,appley, SNAKESIZE, SNAKESIZE)
        bodycord.append(headcord)

    scoretext = font.render("Score: " + str(score), True, GREEN, DARKRED)
    window.fill(WHITE)
    window.blit(titletext,titlerect)
    window.blit(scoretext,scorerect)
    headrect = pygame.draw.rect(window, GREEN, headcord)
    applerect = pygame.draw.rect(window,RED,applecord)
    for body in bodycord:
        pygame.draw.rect(window, DARKGREEN,body)
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()