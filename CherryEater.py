# --------------------------------------
# Title: CherryEater.py
# Purpose: First example pygame Game
# Author: Sarah Herzog
# Date: 10/03/2022
# --------------------------------------


# --------------------------------------
# Import Libraries
# --------------------------------------
import pygame, random
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
pygame.display.set_caption('Cherry Eater')

# Set up some variables to use later in our game
running = True

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up player
PLAYERSIZE = 50
playerPos = [float(random.randint(0, WINDOWWIDTH - PLAYERSIZE)), float(random.randint(0, WINDOWHEIGHT - PLAYERSIZE))]
player = pygame.Rect(playerPos[0], playerPos[1], PLAYERSIZE, PLAYERSIZE)
MOVESPEED = 50

# Set up movement variables.

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
            if event.key == pygame.K_x:
                # Teleport the player to a random location!
                playerPos[0] = random.randint(0, WINDOWWIDTH - PLAYERSIZE)
                playerPos[1] = random.randint(0, WINDOWHEIGHT - PLAYERSIZE)

    # Update our key list
    keys = pygame.key.get_pressed()
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
    if keys[pygame.K_LEFT]:
        playerPos[0] -= MOVESPEED * frameSec
    if keys[pygame.K_RIGHT]:
        playerPos[0] += MOVESPEED * frameSec
    if keys[pygame.K_UP]:
        playerPos[1] -= MOVESPEED * frameSec
    if keys[pygame.K_DOWN]:
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



