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
screen = pygame.display.set_mode([500, 500])

# Set up some variables to use later in our game
running = True

# Set up player
position = [250, 250]
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
                position[0] -= 10
            if event.key == pygame.K_RIGHT:
                position[0] += 10
            if event.key == pygame.K_UP:
                position[1] -= 10
            if event.key == pygame.K_DOWN:
                position[1] += 10
    # ----------------------------------

    
    # ----------------------------------
    # Update
    # ----------------------------------
    # ----------------------------------

    
    # ----------------------------------
    # Draw
    # ----------------------------------
    # Fill the background with a colour
    screen.fill((255, 255, 255))

    # Draw Everything
    pygame.draw.circle(screen, (0, 0, 255), position, 75)
    

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



