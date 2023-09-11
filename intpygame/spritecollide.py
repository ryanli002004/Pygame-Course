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

class Player(pygame.sprite.Sprite):

    def __init__(self, x,y, monstergroup):
        super().__init__()
        self.image = pygame.image.load(os.path.join("intpygame","knight.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.monstergroup = monstergroup
        self.velocity = 10

    def update(self):
        self.move()
        self.checkcollisions()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity

    def checkcollisions(self):
        if pygame.sprite.spritecollide(self, self.monstergroup, True):
            print(len(self.monstergroup))
        

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

playergroup = pygame.sprite.Group()
player = Player(500,500, monstergroup)
playergroup.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((0,0,0))
    playergroup.update()
    playergroup.draw(window)
    monstergroup.update()
    monstergroup.draw(window)
    pygame.display.update()

pygame.quit()