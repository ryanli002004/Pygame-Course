import pygame
import random
import os

pygame.init()

WINDOWW = 1200
WINDOWH = 700
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("monster wrangler")

FPS = 60
clock = pygame.time.Clock()

class Game():

    def __init__(self,player,monsterGroup):
        super().__init__()
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player 
        self.monsterGroup = monsterGroup

        self.nextLevelSound = pygame.mixer.Sound(os.path.join("monsterwrangler","next_level.wav"))

        self.font = pygame.font.Font(os.path.join("monsterwrangler","Abrushow.ttf"),24)

        blueImage = pygame.image.load(os.path.join("monsterwrangler","blue_monster.png"))
        greenImage = pygame.image.load(os.path.join("monsterwrangler","green_monster.png"))
        purpleImage = pygame.image.load(os.path.join("monsterwrangler","purple_monster.png"))
        yellowImage = pygame.image.load(os.path.join("monsterwrangler","yellow_monster.png"))
        self.targetMonsterImages = [blueImage,greenImage,purpleImage,yellowImage]
        self.targetMonsterType = random.randint(0,3)
        self.targetMonsterImage = self.targetMonsterImages[self.targetMonsterType]
        self.targetMonsterRect = self.targetMonsterImage.get_rect()
        self.targetMonsterRect.centerx = WINDOWW//2
        self.targetMonsterRect.top = 30

    def update(self):
        self.frame_count += 1
        if self.frame_count == FPS:
            self.frame_count = 0
            self.round_time += 1
        self.checkcollisions()

    def draw(self):
        WHITE = (255,255,255)
        BLUE = (20,176,235)
        GREEN = (87,201,47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157,20)
        colors = [BLUE, GREEN, PURPLE, YELLOW]
        catchText = self.font.render("Current Catch", True, WHITE)
        catchRect = catchText.get_rect()
        catchRect.centerx = WINDOWW//2
        catchRect.top = 5

        scoreText = self.font.render("Score "+str(self.score),True,WHITE)
        scoreRect = scoreText.get_rect()
        scoreRect.topleft = (5,5)

        livesText = self.font.render("Lives: "+str(self.player.lives), True, WHITE)
        livesRect = livesText.get_rect()
        livesRect.topleft = (5,35)

        roundText = self.font.render("Current Round: "+ str(self.round_number), True, WHITE)
        roundRect = roundText.get_rect()
        roundRect.topleft = (5,65)

        timeText = self.font.render("Round Time: " + str(self.round_time),True, WHITE)
        timeRect = timeText.get_rect()
        timeRect.topright = (WINDOWW-10, 5)

        warpText = self.font.render("Warps: "+ str(self.player.warps),True, WHITE )
        warpRect = warpText.get_rect()
        warpRect.topright = (WINDOWW-10,35)

        window.blit(catchText,catchRect)
        window.blit(scoreText,scoreRect)
        window.blit(livesText,livesRect)
        window.blit(timeText,timeRect)
        window.blit(warpText,warpRect)
        window.blit(roundText,roundRect)
        window.blit(self.targetMonsterImage,self.targetMonsterRect)

        pygame.draw.rect(window, colors[self.targetMonsterType],(WINDOWW//2 - 32,30,64,64),2)
        pygame.draw.rect(window, colors[self.targetMonsterType],(0,100,WINDOWW,WINDOWH-200),4)
    def checkcollisions(self):
        collidedMonster = pygame.sprite.spritecollideany(self.player, self.monsterGroup)
        if collidedMonster:
            if collidedMonster.type == self.targetMonsterType:
                self.score += 100*self.round_number
                collidedMonster.remove(self.monsterGroup)
                if (self.monsterGroup):
                    self.player.catchsound.play()
                    self.choosenewtarget()
                else:
                    self.player.reset()
                    self.startnewround()
            else:
                self.player.diesound.play()
                self.player.lives -= 1
                if self.player.lives <= 0:
                    self.pausegame("Final Score: "+str(self.score),"Press 'Enter' to play again")
                    self.resetgame()
                self.player.reset()


    def startnewround(self):
        self.score += int(10000*self.round_number/(1+self.round_time))
        self.round_time = 0
        self.round_number += 1
        self.frame_count =0
        self.player.warps += 1
        for monster in self.monsterGroup:
            self.monsterGroup.remove(monster)
        for i in range(self.round_number):
            self.monsterGroup.add(Monster(random.randint(0,WINDOWW-64),random.randint(100,WINDOWH-164),self.targetMonsterImages[0],0))
            self.monsterGroup.add(Monster(random.randint(0,WINDOWW-64),random.randint(100,WINDOWH-164),self.targetMonsterImages[1],1))
            self.monsterGroup.add(Monster(random.randint(0,WINDOWW-64),random.randint(100,WINDOWH-164),self.targetMonsterImages[2],2))
            self.monsterGroup.add(Monster(random.randint(0,WINDOWW-64),random.randint(100,WINDOWH-164),self.targetMonsterImages[3],3))
        self.choosenewtarget()
        self.nextLevelSound.play()

    def choosenewtarget(self):
        targetMonster = random.choice(self.monsterGroup.sprites())
        self.targetMonsterType = targetMonster.type
        self.targetMonsterImage = targetMonster.image

    def pausegame(self, mainText, subText):
        global running
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        mainText = self.font.render(mainText, True, WHITE)
        mainRect = mainText.get_rect()
        mainRect.center = (WINDOWW//2,WINDOWH//2)
        subText = self.font.render(subText, True, WHITE)
        subRect = subText.get_rect()
        subRect.center=(WINDOWW//2,WINDOWH//2+64)
        window.fill(BLACK)
        window.blit(mainText,mainRect)
        window.blit(subText,subRect)
        pygame.display.update()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
    def resetgame(self):
        self.score = 0
        self.round_number = 0
        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()

        self.startnewround()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("monsterwrangler","knight.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOWW//2
        self.rect.bottom = WINDOWH
        self.lives = 5
        self.warps = 2
        self.vel = 8
        self.catchsound = pygame.mixer.Sound(os.path.join("monsterwrangler","catch.wav"))
        self.diesound =pygame.mixer.Sound(os.path.join("monsterwrangler","die.wav"))
        self.warpsound = pygame.mixer.Sound(os.path.join("monsterwrangler","warp.wav"))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.vel
        if keys[pygame.K_d] and self.rect.right < WINDOWW:
            self.rect.x += self.vel
        if keys[pygame.K_w] and self.rect.top > 100:
            self.rect.y -= self.vel
        if keys[pygame.K_s] and self.rect.bottom <WINDOWH - 100:
            self.rect.y += self.vel


    def warp(self):
        if self.warps > 0:
            self.warpsound.play()
            self.warps -=1
            self.rect.bottom = WINDOWH

    def reset(self):
        self.rect.centerx = WINDOWW//2
        self.rect.bottom = WINDOWH


class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y, image, monsterType):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.type = monsterType
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        self.velocity = random.randint(1,5)

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity
        if self.rect.left <= 0 or self.rect.right >= WINDOWW:
            self.dx = -1*self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOWH-100:
            self.dy = -1*self.dy

myplayergroup = pygame.sprite.Group()
myplayer = Player()
myplayergroup.add(myplayer)

mymonstergroup = pygame.sprite.Group()
mygame = Game(myplayer,mymonstergroup)
mygame.pausegame("Monster Wrangler", "Press 'Enter' to begin")
mygame.startnewround()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myplayer.warp()

    window.fill((0,0,0))

    myplayergroup.update()
    myplayergroup.draw(window)

    mymonstergroup.update()
    mymonstergroup.draw(window)

    mygame.update()
    mygame.draw() 


    clock.tick(FPS)
    pygame.display.update()

pygame.quit()