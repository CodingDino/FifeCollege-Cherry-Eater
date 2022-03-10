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

# Set up the game clock
mainClock = pygame.time.Clock()

# Set up the drawing window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])

# Set up some variables to use later in our game
running = True

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up player
PLAYERSIZE = 50
playerPos = [float(WINDOWWIDTH/2 - PLAYERSIZE/2), float(WINDOWHEIGHT/2 - PLAYERSIZE/2)]
player = pygame.Rect(playerPos[0], playerPos[1], PLAYERSIZE, PLAYERSIZE)
MOVESPEED = 50

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
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
                moveLeft = True
                moveRight = False
            if event.key == pygame.K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == pygame.K_UP:
                moveUp = True
                moveDown = False
            if event.key == pygame.K_DOWN:
                moveDown = True
                moveUp = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False
    # ----------------------------------

    
    # ----------------------------------
    # Update
    # ----------------------------------
    # Get the frame time in miliseconds
    frameMs = mainClock.tick(60)
    frameSec = frameMs / 1000

    # Process Movement
    # Scale move speed by time passed since the last frame for consistant movement
    # Use our own position list for this so we can use decimal points!
    if moveLeft == True:
        playerPos[0] -= MOVESPEED * frameSec
    if moveRight == True:
        playerPos[0] += MOVESPEED * frameSec
    if moveUp == True:
        playerPos[1] -= MOVESPEED * frameSec
    if moveDown == True:
        playerPos[1] += MOVESPEED * frameSec
    # Move the player's rectangle based on the position variable
    player.left = playerPos[0]
    player.top = playerPos[1]
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



