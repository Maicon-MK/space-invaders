import pygame
import math
import os
from random import randint

# Initialize the pygame
pygame.init()
FPS = 120
CLOCK = pygame.time.Clock()

# Create the screen
SCREEN = pygame.display.set_mode((800, 600))

# BACKGROUND
BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))

# Title and Icon
pygame.display.set_caption("Space Invader")
ICON = pygame.image.load(os.path.join("assets", "ufo.png"))
pygame.display.set_icon(ICON)

# score
score_value = 0
FONT = pygame.font.Font("freesansbold.ttf", 32)
TEST_X = 10
TEST_Y = 10

def show_score(x, y):
    score = FONT.render("Score: " + str(score_value), True, (255, 255, 255))
    SCREEN.blit(score, (x, y))

# Game over
GAME_OVER_FONT = pygame.font.Font("freesansbold.ttf", 64)

def game_over_text():
    game_over = GAME_OVER_FONT.render("GAME OVER", True, (255, 255, 255))
    SCREEN.blit(game_over, (200, 250))

# Player
player_img = pygame.image.load(os.path.join("assets", "spaceship.png"))
playerX = 370
playerY = 480
change_playerX = 0

def player(x, y):
    SCREEN.blit(player_img, (x, y))

# Alien
alien_img = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
alien_down = []
num_aliens = 8
for i in range(num_aliens):
    alien_img.append(pygame.image.load("assets\\alien.png"))
    alienX.append(randint(0, 735))
    alienY.append(randint(50, 150))
    alienX_change.append(1)
    alienY_change.append(40)
    alien_down.append(False)

def alien(x, y):
    SCREEN.blit(alien_img[i], (x, y))

# Bullet
bullet_img = pygame.image.load("assets\\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bullet_img, (x + 16, y + 10))

def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(alienX - bulletX, 2)) + (math.pow(alienY - bulletY, 2))
    )
    if distance < 27:
        return True
    return False

# The program
running = True
game_state = "start"  # Adiciona um estado para a tela de inicialização

while running:
    CLOCK.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if game_state == "start":
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(BACKGROUND, (0, 0))
        
        # Exibe o título da tela de inicialização
        start_font = pygame.font.Font("freesansbold.ttf", 64)
        start_text = start_font.render("SPACE INVADER", True, (255, 255, 255))
        SCREEN.blit(start_text, (150, 250))
        
        start_instructions = FONT.render("Press SPACE to Start", True, (255, 255, 255))
        SCREEN.blit(start_instructions, (250, 350))
        
        if keys[pygame.K_SPACE]:
            game_state = "playing"  # Muda para o estado "playing" quando a tecla Espaço é pressionada
    
    elif game_state == "playing":
        # Spawning enemies
        for i in range(num_aliens):
            alien_img.append(pygame.image.load("assets\\alien.png"))
            alienX.append(randint(0, 735))
            alienY.append(randint(50, 150))
            alienX_change.append(1)
            alienY_change.append(40)
            alien_down.append(False)


def alien(x, y):
    SCREEN.blit(alien_img[i], (x, y))


# Bullet
bullet_img = pygame.image.load("assets\\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bullet_img, (x + 16, y + 10))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(alienX - bulletX, 2)) + (math.pow(alienY - bulletY, 2))
    )
    if distance < 27:
        return True
    return False


# The program
running = True
while running:
    # Clock
    CLOCK.tick(FPS)

    # RGB
    SCREEN.fill((0, 0, 0))

    # BACKGROUND
    SCREEN.blit(BACKGROUND, (0, 0))

    # Check if not quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if game_state == "start":
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(BACKGROUND, (0, 0))
        
        # Exibe o título da tela de inicialização
        start_font = pygame.font.Font("freesansbold.ttf", 64)
        start_text = start_font.render("SPACE INVADER", True, (255, 255, 255))
        SCREEN.blit(start_text, (150, 250))
        
        start_instructions = FONT.render("Press SPACE to Start", True, (255, 255, 255))
        SCREEN.blit(start_instructions, (250, 350))
        
        if keys[pygame.K_SPACE]:
            game_state = "playing"  # Muda para o estado "playing" quando a tecla Espaço é pressionada
    
    elif game_state == "playing":
    # Spawning enemies
     for i in range(num_aliens):
        # Game Over
        if alienY[i] > 440:
            for j in range(num_aliens):
                alienY[j] = 9999
            game_over_text()
            break

        alienX[i] += alienX_change[i]

        if alienX[i] > 736:
            alienX_change[i] *= -1
            alienX[i] = 736
            alienY[i] += alienY_change[i]
        elif alienX[i] < 0:
            alienX_change[i] *= -1
            alienX[i] = 0
            alienY[i] += alienY_change[i]

        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            alienX[i] = randint(0, 735)
            alienY[i] = randint(50, 150)
            score_value += 1

        alien(alienX[i], alienY[i])

    # Player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        change_playerX = -2
    elif keys[pygame.K_RIGHT]:
        change_playerX = 2
    else:
        change_playerX = 0

    if keys[pygame.K_SPACE] and bullet_state == "ready":
        bulletX = playerX
        fire_bullet(bulletX, bulletY)

    playerX += change_playerX

    if playerX <= 10:
        playerX = 10
    elif playerX >= 726:
        playerX = 726

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(TEST_X, TEST_Y)
    pygame.display.update()
