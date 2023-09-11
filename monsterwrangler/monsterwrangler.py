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
        pass

    def update(self):
        pass

    def warp(self):
        pass

    def resetplayer(self):
        pass


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def update(self):
        pass

    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()