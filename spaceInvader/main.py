import pygame
import random
import os


pygame.init()

WINDOWW = 1200
WINDOWH = 700
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("Space Invaders")

FPS = 60
clock = pygame.time.Clock()


class Game():

    def __init__(self, player, alienGroup, playerBulletGroup, alienBulletGroup):
        self.roundNumber = 1
        self.score = 0
        self.player = player
        self.alienGroup = alienGroup
        self.playerBulletGroup = playerBulletGroup
        self.alienBulletGroup = alienBulletGroup

        self.newRoundSound = pygame.mixer.Sound(os.path.join("spaceInvader","new_round.wav"))
        self.breachSound = pygame.mixer.Sound(os.path.join("spaceInvader","breach.wav"))
        self.alienHitSound = pygame.mixer.Sound(os.path.join("spaceInvader","alien_hit.wav"))
        self.playerHitSound = pygame.mixer.Sound(os.path.join("spaceInvader","player_hit.wav"))

        self.font = pygame.font.Font(os.path.join("spaceInvader","Facon.ttf"),32)

    def update(self):
        self.shiftAliens()
        self.checkCollisions()
        self.checkRoundCompletion()

    def draw(self):
        WHITE = (255,255,255)
        scoreText = self.font.render("Score; "+ str(self.score), True, WHITE)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx = WINDOWW//2
        scoreRect.top = 10

        roundText = self.font.render("Round: " + str(self.roundNumber), True, WHITE)
        roundRect = roundText.get_rect()
        roundRect.topleft = (20,10)

        livesText = self.font.render("Lives: "+ str(self.player.lives),True,WHITE)
        livesRect = livesText.get_rect()
        livesRect.topright = (WINDOWW - 20, 10)

        window.blit(scoreText,scoreRect)
        window.blit(roundText,roundRect)
        window.blit(livesText,livesRect)
        pygame.draw.line(window, WHITE, (0,50),(WINDOWW,50),4)
        pygame.draw.line(window, WHITE, (0,WINDOWH-100), (WINDOWW,WINDOWH-100),4)

    def shiftAliens(self):
        shift = False
        for alien in (self.alienGroup.sprites()):
            if alien.rect.left <= 0 or alien.rect.right >= WINDOWW:
                shift = True
            
        if shift:
            breach = False
            for alien in (self.alienGroup.sprites()):
                alien.rect.y += 10*self.roundNumber
                alien.direction *= -1
                alien.rect.x += alien.direction*alien.velocity

                if alien.rect.bottom >= WINDOWH - 100:
                    breach = True

            if breach:
                self.breachSound.play()
                self.player.lives -=1
                self.checkGameStatus("Aliens breached the line","press 'enter' to continue")

    def checkCollisions(self):
        pass

    def StartNewRound(self):
        for i in range(11):
            for j in range(5):
                alien = Alien(64 + i*64,64 + j*64, self.roundNumber, self.alienBulletGroup)
                self.alienGroup.add(alien)

        self.newRoundSound.play()
        self.pauseGame("space invaders round: "+str(self.roundNumber), "press 'enter' to begin")

    def checkRoundCompletion(self):
        pass

    def checkGameStatus(self, mainText, subText):
        self.alienBulletGroup.empty()
        self.playerBulletGroup.empty()
        self.player.reset()
        for alien in self.alienGroup:
            alien.reset()

        if self.player.lives <= 0:
            self.resetGame()
        else:
            self.pauseGame(mainText,subText)

    def pauseGame(self, mainText, subText):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        mainText = self.font.render(mainText, True, WHITE)
        mainRect = mainText.get_rect()
        mainRect.center = (WINDOWW//2,WINDOWH//2)
        subText = self.font.render(subText, True, WHITE)
        subRect = subText.get_rect()
        subRect.center = (WINDOWW//2,WINDOWH//2+64)

        window.fill(BLACK)
        window.blit(mainText,mainRect)
        window.blit(subText,subRect)
        pygame.display.update()

        global running
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                if event.type == pygame.QUIT:
                    paused = False
                    running = False

    def resetGame(self):
        pass


class Player(pygame.sprite.Sprite):

    def __init__(self, bulletGroup):
        super().__init__()
        self.image = pygame.image.load(os.path.join("spaceInvader","player_ship.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOWW//2
        self.rect.bottom = WINDOWH

        self.lives = 5
        self.velocity = 5

        self.bulletGroup = bulletGroup

        self.shootSound = pygame.mixer.Sound(os.path.join("spaceInvader","player_fire.wav"))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_d] and self.rect.right < WINDOWW:
            self.rect.x += self.velocity
    
    def fire(self):
        if len(self.bulletGroup)<6:
            self.shootSound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bulletGroup)

    def reset(self):
        self.rect.centerx = WINDOWH//2


class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, velocity, bulletGroup):
        super().__init__()
        self.image = pygame.image.load(os.path.join("spaceInvader","alien.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.startingX = x
        self.startingY = y

        self.direction = 1
        self.velocity = velocity
        self.bulletGroup = bulletGroup

        self.shootSound = pygame.mixer.Sound(os.path.join("spaceInvader","alien_fire.wav"))

        
    def update(self):
        self.rect.x += self.direction*self.velocity

        if random.randint(0,800) > 799 and len(self.bulletGroup) < 4:
            self.shootSound.play()
            self.fire()


    def fire(self):
        AlienBullet(self.rect.centerx,self.rect.bottom, self.bulletGroup)

    def reset(self):
        self.rect.topleft = (self.startingX,self.startingY)
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bulletGroup):
        super().__init__()
        self.image = pygame.image.load(os.path.join("spaceInvader","green_laser.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        self.velocity = 10
        bulletGroup.add(self)

    def update(self):
        self.rect.y -= self.velocity 

        if self.rect.bottom < 0:
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, bulletGroup):
        super().__init__()
        self.image = pygame.image.load(os.path.join("spaceInvader","red_laser.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = x 
        self.rect.centery = y
        
        self.velocity = 10
        bulletGroup.add(self)

    def update(self):
        self.rect.y += self.velocity

        if self.rect.top > WINDOWH:
            self.kill()


myPlayerBulletGroup = pygame.sprite.Group()
myAlienBulletGroup = pygame.sprite.Group()
myPlayerGroup = pygame.sprite.Group()
myPlayer = Player(myPlayerBulletGroup)
myPlayerGroup.add(myPlayer)
myAlienGroup = pygame.sprite.Group()


myGame = Game(myPlayer,myAlienGroup,myPlayerBulletGroup,myAlienBulletGroup)
myGame.StartNewRound()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myPlayer.fire()

    window.fill((0,0,0))

    myPlayerGroup.update()
    myPlayerGroup.draw(window)

    myAlienGroup.update()
    myAlienGroup.draw(window)

    myAlienBulletGroup.update()
    myAlienBulletGroup.draw(window)

    myPlayerBulletGroup.update()
    myPlayerBulletGroup.draw(window)

    myGame.update()
    myGame.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()