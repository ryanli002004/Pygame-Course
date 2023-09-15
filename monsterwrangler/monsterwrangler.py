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

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def checkcollisions(self):
        pass

    def startnewround(self):
        pass

    def choosenewtarget(self):
        pass

    def pausegame(self):
        pass

    def resetgame(self):
        pass


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
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.vel
        if keys[pygame.K_s] and self.rect.bottom <WINDOWH:
            self.rect.y += self.vel


    def warp(self):
        if self.warps > 0:
            self.warpsound.play()
            self.warps -=1
            self.rect.bottom = WINDOWH

    def resetplayer(self):
        self.rect.centerx = WINDOWW//2
        self.rect.bottom = WINDOWH


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def update(self):
        pass

myplayergroup = pygame.sprite.Group()
myplayer = Player()
myplayergroup.add(myplayer)

mymonstergroup = pygame.sprite.Group()

mygame = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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