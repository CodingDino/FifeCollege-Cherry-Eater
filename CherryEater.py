# --------------------------------------
# Title: CherryEater.py
# Purpose: First example pygame Game
# Author: Sarah Herzog
# Date: 10/03/2022
# --------------------------------------


# --------------------------------------
# Import Libraries
# --------------------------------------
import pygame
# --------------------------------------


# --------------------------------------
# Initialisation and Setup
# --------------------------------------
# Initialize python so we can use it
pygame.init()

# Set up the drawing window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])

# Set up some variables to use later in our game
running = True

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up player
PLAYERSIZE = 50
player = pygame.Rect(WINDOWWIDTH/2 - PLAYERSIZE/2, WINDOWHEIGHT/2 - PLAYERSIZE/2, PLAYERSIZE, PLAYERSIZE)
MOVESPEED = 10
# --------------------------------------


# --------------------------------------
# Game Loop
# --------------------------------------
# Run over and over until the user asks to quit
while running:
    
    # ----------------------------------
    # Input
    # ----------------------------------
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left -= MOVESPEED
            if event.key == pygame.K_RIGHT:
                player.left += MOVESPEED
            if event.key == pygame.K_UP:
                player.top -= MOVESPEED
            if event.key == pygame.K_DOWN:
                player.top += MOVESPEED
    # ----------------------------------

    
    # ----------------------------------
    # Update
    # ----------------------------------
    # ----------------------------------

    
    # ----------------------------------
    # Draw
    # ----------------------------------
    # Fill the background with a colour
    screen.fill(WHITE)

    # Draw Everything
    pygame.draw.rect(screen, BLACK, player)
    

    # Flip the display
    pygame.display.flip()
    # ----------------------------------
    

# END of Game Loop
# --------------------------------------


# --------------------------------------
# Program Exit
# --------------------------------------
pygame.quit()
# --------------------------------------



