import pygame
import os
import time
import random

# main window
WIDTH, HEIGHT = 576, 1024
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corona Invasion Game")

# let's load the images
CORONA = pygame.image.load(os.path.join("images", "enemy.png"))
PLAYER = pygame.image.load(os.path.join("images", "doctor.png"))


# Lasers
VACCINE = pygame.image.load(os.path.join("images", "bullet.png"))


# Background
HOSPITAL = pygame.image.load(os.path.join("images", "Hospital_background.jpg"))

# main loop
def main():
    run = True
    # confirms if the while loop will run
    FPS = 60
    # how fast the game runs
    clock = pygame.time.Clock()
    # helps keep the game consistent on any device

    while run:
        clock.tick(FPS)

        # event is every interaction for user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # for exiting game

