import pygame
import os
vector = pygame.math.Vector2

pygame.init()

WINDOWW = 960
WINDOWH = 640
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("Making a tile map")

FPS = 60
clock = pygame.time.Clock()



mainTileGroup = pygame.sprite.Group()
grassTileGroup = pygame.sprite.Group()
waterTileGroup = pygame.sprite.Group()
myPlayerGroup = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, imageInt, mainGroup, subGroup=""):
        super().__init__()
        if imageInt ==1:
            self.image = pygame.image.load(os.path.join("advancedpygame","dirt.png"))
        elif imageInt == 2:
            self.image = pygame.image.load(os.path.join("advancedpygame","grass.png"))
            subGroup.add(self)
        elif imageInt ==3:
            self.image = pygame.image.load(os.path.join("advancedpygame","water.png"))
            subGroup.add(self)
        mainGroup.add(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Player(pygame.sprite.Sprite):

    def __init__(self,x,y,grassTiles,waterTiles):
        super().__init__()
        self.image = pygame.image.load(os.path.join("advancedpygame","knight.png"))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        self.grassTiles = grassTiles
        self.waterTiles = waterTiles

        self.position = vector(x,y)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

        self.HACCL = 2
        self.HFRIC = 0.15
        self.VACCL = 0.5

    def update(self):

        self.acceleration = vector(0,self.VACCL)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acceleration.x = -1*self.HACCL
        if keys[pygame.K_d]:
            self.acceleration.x = self.HACCL

        self.acceleration.x -= self.velocity.x*self.HFRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        self.rect.bottomleft = self.position

        collidedPlatforms = pygame.sprite.spritecollide(self,self.grassTiles,False) 
        if collidedPlatforms:
            


tileMap = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1]
]

for i in range(len(tileMap)):
    for j in range(len(tileMap[i])):
            if tileMap[i][j] == 1:
                Tile(j*32,i*32, 1, mainTileGroup)
            elif tileMap[i][j] == 2:
                Tile(j*32,i*32, 2, mainTileGroup,grassTileGroup)
            elif tileMap[i][j] ==3:
                Tile(j*32,i*32,3,mainTileGroup,waterTileGroup)
            elif tileMap[i][j] == 4:
                myPlayer = Player(j*32,i*32+32,grassTileGroup,waterTileGroup)
                myPlayerGroup.add(myPlayer)

backgroundImage = pygame.image.load(os.path.join("advancedpygame","background.png"))
backgroundRect = backgroundImage.get_rect()
backgroundRect.topleft = (0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(backgroundImage,backgroundRect)

    mainTileGroup.draw(window)

    myPlayerGroup.update()
    myPlayerGroup.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()