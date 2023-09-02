import pygame
import os

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("add sound")

sound_1 = pygame.mixer.Sound(os.path.join("tutorial","sound_1.wav"))
sound_2 = pygame.mixer.Sound(os.path.join("tutorial","sound_2.wav"))

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(.1)
sound_2.play()

pygame.mixer.music.load(os.path.join("tutorial","music.wav"))
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(10000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()