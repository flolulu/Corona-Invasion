import pygame
import os
import time
import random

#
# let's load the images
CORONA = pygame.image.load(os.path.join("images", "enemy.png"))
PLAYER = pygame.image.load(os.path.join("images", "doctor.png"))

# Lasers
VACCINE = pygame.image.load(os.path.join("images", "bullet.png"))

# Background
HOSPITAL = pygame.image.load(os.path.join("images", "Hospital_background.jpg"))
