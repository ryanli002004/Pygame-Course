import pygame
import os
import random

pygame.init()

WINDOWW = 800
WINDOWH = 600
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("sprite groups")

FPS = 60
clock = pygame.time.Clock()

class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join("intpygame","blue_monster.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = random.randint(1,10)
    
    def update(self):
        self.rect.y += self.velocity

monstergroup = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64,10)
    monstergroup.add(monster)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((0,0,0))
    monstergroup.update()
    monstergroup.draw(window)
    pygame.display.update()

pygame.quit()