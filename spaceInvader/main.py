import pygame
import random
import os

pygame.init()

WINDOWW = 1200
WINDOWH = 700
window = pygame.display.set_mode(WINDOWW,WINDOWH)
pygame.display.set_caption("Space Invaders")

FPS = 60
clock = pygame.time.Clock()

class Game():

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def shiftAliens(self):
        pass

    def checkCollisions(self):
        pass

    def StartNewRound(self):
        pass

    def checkRoundCompletion(self):
        pass

    def checkGameStatus(self):
        pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()