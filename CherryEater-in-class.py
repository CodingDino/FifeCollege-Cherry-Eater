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
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])

# Set up some variables to use later in our game
running = True

# Set up player
position = [WINDOWWIDTH / 2, WINDOWHEIGHT / 2]
PLAYERSIZE = 50
player = pygame.Rect(position[0], position[1], PLAYERSIZE, PLAYERSIZE)
MOVESPEED = 100 

# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up movement variables
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
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True
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
    # Get the frame time
    frameMs = mainClock.tick()
    frameSec = frameMs / 1000
    
    # Move based on bool variables set by keypress
    if moveLeft == True:
        # MOVESPEED is in pixels / second
        # Get amount moved by mult speed by time passed
        position[0] -= MOVESPEED * frameSec
    if moveRight == True:
        position[0] += MOVESPEED * frameSec
    if moveUp == True:
        position[1] -= MOVESPEED * frameSec
    if moveDown == True:
        position[1] += MOVESPEED * frameSec

    # Update player rectangle based on position
    player.left = position[0]
    player.top = position[1]
    # ----------------------------------

    
    # ----------------------------------
    # Draw
    # ----------------------------------
    # Fill the background with a colour
    screen.fill(WHITE)

    # Draw Everything
    pygame.draw.rect(screen, BLUE, player)
    

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



