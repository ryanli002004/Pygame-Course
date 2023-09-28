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
        self.moveRightSprites = []
        self.moveLeftSprites = []
        self.idleRightSprites = []
        self.idleLeftSprites = []

        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (1).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (2).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (3).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (4).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (5).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (6).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (7).png")),(64,64)))
        self.moveRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Run (8).png")),(64,64)))

        for sprite in self.moveRightSprites:
            self.moveLeftSprites.append(pygame.transform.flip(sprite, True, False))

        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (1).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (2).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (3).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (4).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (5).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (6).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (7).png")),(64,64)))
        self.idleRightSprites.append(pygame.transform.scale(pygame.image.load(os.path.join("advancedpygame","boy","Idle (8).png")),(64,64)))

        for sprite in self.idleRightSprites:
            self.idleLeftSprites.append(pygame.transform.flip(sprite,True,False))

        self.currentSprite = 0

        self.image = self.moveRightSprites[self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        self.startingx = x
        self.startingy = y

        self.grassTiles = grassTiles
        self.waterTiles = waterTiles

        self.position = vector(x,y)
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

        self.HACCL = 2
        self.HFRIC = 0.15
        self.VACCL = 0.5
        self.VJUMPS = 15

    def animate(self, spriteList,speed):
        if self.currentSprite < len(spriteList) -1:
            self.currentSprite+=speed
        else: 
            self.currentSprite = 0
            
        self.image = spriteList[int(self.currentSprite)]

    def update(self):
        self.move()
        self.checkCollisions()
    
    def move(self):
        self.acceleration = vector(0,self.VACCL)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acceleration.x = -1*self.HACCL
            self.animate(self.moveLeftSprites,.5)
        elif keys[pygame.K_d]:
            self.acceleration.x = self.HACCL
            self.animate(self.moveRightSprites, .5)
        else:
            if self.velocity.x >0:
                self.animate(self.idleRightSprites,.5)
            else:
                self.animate(self.idleLeftSprites,.5)

        self.acceleration.x -= self.velocity.x*self.HFRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        self.rect.bottomleft = self.position

        if self.position.x<0:
            self.position.x = WINDOWW
        if self.position.x > WINDOWW:
            self.position.x = 0

    def checkCollisions(self):
        
        collidedPlatforms = pygame.sprite.spritecollide(self,self.grassTiles,False) 
        if collidedPlatforms:
            if self.velocity.y > 0:
                self.position.y = collidedPlatforms[0].rect.top+1
                self.velocity.y = 0

        if pygame.sprite.spritecollide(self, self.waterTiles, False):
            self.position = vector(self.startingx,self.startingy)
            self.velocity = vector(0,0)

    def jump(self):
        if pygame.sprite.spritecollide(self,self.grassTiles,False):
            self.velocity.y = -1*self.VJUMPS
        
            


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
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myPlayer.jump()

    window.blit(backgroundImage,backgroundRect)

    mainTileGroup.draw(window)

    myPlayerGroup.update()
    myPlayerGroup.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()