# This file set up all the global variables

import pygame

# value for choice
NONE = 4
ROCK = 0
PAPER = 1
SCISSORS = 2
# AI win when (player choice + 1) % 3 equal ai choice

# Text constants
START_TEXT = "CLICK YOUR CHOICE"
PLAYER_WIN = "YOU WIN!!! CLICK ANYWHERE TO PLAY AGAIN"
AI_WIN = "YOU LOSE :(((( CLICK ANYWHERE TO PLAY AGAIN"
DRAW_TEXT = "IT'S A DRAW ._. CLICK ANYWHERE TO PLAY AGAIN"

# set up variables for the screen size in pixels
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BUTTON_SIZE = BUTTON_WIDTH, BUTTON_HEIGHT = 75, 75
DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 150, 150

# background color
BACKGROUND_COLOR = (69, 69, 69)
TEXT_COLOR = (255, 255, 255)

# Image assets
ROCK_IMG = pygame.image.load('images/rock.png')
PAPER_IMG = pygame.image.load('images/paper.png')
SCISSORS_IMG = pygame.image.load('images/scissors.png')
NONE_IMG = pygame.image.load('images/none.png')