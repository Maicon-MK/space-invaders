import pygame
import os
import math
from random import randint

pygame.init()
FPS = 120
CLOCK = pygame.time.Clock()

# Create the screen
SCREEN = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader")
ICON = pygame.image.load(os.path.join("assets", "ufo.png"))
pygame.display.set_icon(ICON)

def main():
    ...

#x receive the folder and y the file
bullet_img = pygame.image.load(os.path.join("assets", "bullet.png"))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bullet_img, (x + 16, y + 10))

def carregar_imagem(x, y):
    return pygame.image.load(os.path.join(x, y))

def initialize_aliens(x, alien_img, alienX, alienY, alienX_change, alienY_change, alien_down, num_aliens):
    for i in range(num_aliens):
        alien_img.append(pygame.image.load(f"assets/{x}"))
        alienX.append(randint(0, 735))
        alienY.append(randint(50, 150))
        alienX_change.append(1)
        alienY_change.append(40)
        alien_down.append(False)

def check_collision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(alienX - bulletX, 2)) + (math.pow(alienY - bulletY, 2))
    )
    return distance < 27

def initialize_bullet():
    bullet_img = pygame.image.load("assets/bullet.png")
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 5
    bullet_state = "ready"
    return bullet_img, bulletX, bulletY, bulletX_change, bulletY_change, bullet_state

def map_size(x,y):
    SCREEN = pygame.display.set_mode((x, y))

main()
