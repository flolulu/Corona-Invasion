import pygame  # Game Graphics Library
import random  # Random Numbers Library
import math  # Math 

# Initialize Pygame
pygame.init()

# Initialize a screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # (x,y) or (w,h)

# Title and Icon
pygame.display.set_caption("CORONA INVASION GAME")


# Player Image
PLAYER = pygame.image.load('doctor.png') # playerImg
# X and Y axis values Center
playerX = 350
playerY = 520
player_ChangeX = 0

# Creating A List Of Enemies
enemyImg = []
enemyX = []
enemyY = []
enemy_ChangeX = []
enemy_ChangeY = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(100, 300))
    enemy_ChangeX.append(0.4)
    enemy_ChangeY.append(20)

# Background
background = pygame.image.load('Hospital_background.jpg')

# Bullet Image
bulletImg = pygame.image.load('bullet.png')
# X and Y axis values
bulletX = 0
bulletY = 520
bullet_ChangeY = 2
bullet_state = 'ready'  # when ready, bullet can't be seen else fire

# Score
score_value = 0
scoreFont = pygame.font.Font('SPACEBOY.TTF', 50)

def_font = pygame.font.SysFont("comicsansms", 72)

textX = 6
textY = 10

# GAME OVER
overFont = pygame.font.Font('lasercorps.ttf', 100)


def game_over():
    """
    To Draw GAME OVER! On The Screen
    :return: Nothing
    """
    over = overFont.render("GAME OVER!", True, (255, 0, 0))
    screen.blit(over, (100, 250))


def show_score(x, y):
    """
    To Draw The Score On The Screen
    :return: Nothing
    """
    score = scoreFont.render(str(score_value), True, (255, 153, 51))
    screen.blit(score, (x, y))


def shoot(x, y):
    """
    Change the bullet state and draw the image on the screen
    """
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))  # Bullet to be at the center and top


def player(x, y):
    """
    To Draw The Player Image On The Screen
    :return: Nothing
    """
    screen.blit(PLAYER, (x, y))


def enemy(x, y, j):
    """
    To Draw The Enemy Image On The Screen
    :return: Nothing
    """
    screen.blit(enemyImg[j], (x, y))


def border():
    """
    To Draw Border Of Collision On The Screen
    :return: Nothing
    """
    player_border = def_font.render("---------------------------------------------------", True, (218, 165, 32))
    screen.blit(player_border, (0, 473))


def is_collision(x1, y1, x2, y2):
    """
    To Draw Check If The Bullet Collides With The Enemy
    :return: True if Collision Happens
    """
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 27:
        return True
    return False


# FUN
scoreUpdate = True
# Game LOOP VAR
running = True

# GOING THROUGH THE EVENTS AND CLOSING IF X IS CLICKED
while running:
    # Change Background Color
    # screen.fill((32, 32, 32))  # RGB

    # Set Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check For Keypress
        if event.type == pygame.KEYDOWN:  # KEYDOWN -> IS KEY PRESSED
            if event.key == pygame.K_LEFT:
                player_ChangeX = -0.8
            if event.key == pygame.K_RIGHT:
                player_ChangeX = 0.8
            if event.key == pygame.K_SPACE:
                # ALLOWS ONLY ONE BULLET BEFORE RESET
                if bullet_state == 'ready':
                    bulletX = playerX
                    shoot(bulletX, bulletY)
        # Key Release
        if event.type == pygame.KEYUP:  # KEYUP -> IS KEY RELEASED
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_ChangeX = 0

    playerX += player_ChangeX
    # Setting Border Boundaries
    if playerX >= 736:
        playerX = 736  # 800 - 64
    if playerX <= 0:
        playerX = 0

    # Setting Border Boundaries
    for i in range(num_of_enemies):
        # GAME OVER
        if enemyY[i] >= 440:  # Coordinate Of Collision
            scoreUpdate = False
            game_over()
            break
        if enemyX[i] >= 736:  # BOUNDARY
            enemy_ChangeX[i] = -0.8
            enemyY[i] += enemy_ChangeY[i]
        if enemyX[i] <= 0:
            enemy_ChangeX[i] = 0.8
            enemyY[i] += enemy_ChangeY[i]

        # Enemy Movement
        enemyX[i] += enemy_ChangeX[i]
        if scoreUpdate:
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:  # Creating Another Enemy Image And Updating Score if True
                bulletY = 520
                bullet_state = 'ready'
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(40, 300)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bullet_state == 'fire':
        shoot(bulletX, bulletY)
        bulletY -= bullet_ChangeY
    if bulletY <= 0:
        bulletY = 520
        bullet_state = 'ready'

    # Setting player coordinates
    player(playerX, playerY)
    show_score(textX, textY)
    border()
    pygame.display.update()  # Display updation is required after each change
