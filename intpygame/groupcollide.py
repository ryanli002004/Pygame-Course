import pygame
import os
import random

pygame.init()

WINDOWW = 800
WINDOWH = 600
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("group collide")

FPS = 60
clock = pygame.time.Clock()

class Game():

    def __init__(self, monstergroup, knightgroup):
        self.knightgroup = knightgroup
        self.monstergroup = monstergroup

    def update(self):
        self.checkcollisions()

    def checkcollisions(self):
        pygame.sprite.groupcollide(self.monstergroup, self.knightgroup, True, False)

class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join("intpygame","blue_monster.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = random.randint(1,5)
    
    def update(self):
        self.rect.y += self.velocity

class Knight(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join("intpygame","knight.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = random.randint(1,5)
    
    def update(self):
        self.rect.y -= self.velocity

monstergroup = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64,10)
    monstergroup.add(monster)

knightgroup = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOWH-64)
    knightgroup.add(knight)

game = Game(monstergroup,knightgroup)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    window.fill((0,0,0))
    monstergroup.update()
    monstergroup.draw(window)
    knightgroup.update()
    knightgroup.draw(window)
    game.update()
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()