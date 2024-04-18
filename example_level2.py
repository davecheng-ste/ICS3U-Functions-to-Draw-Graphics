"""
File: example2.py
Author: DAVE CHENG
Date: 2024-04-18
Description: Draws graphics using functions, Level 2 example.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flags")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
BLUE = (0, 51, 204)
RED = (204, 0, 0)
GOLD = (255, 206, 0)

# Define functions for composite shapes
# --(FUNCTIONS START HERE)-----------------------------------------------

def draw_flag_france(x_origin, y_origin):
    """
    Draws a French flag of 90x60 dimensions.

    Parameters:
        x_origin (int): x-value coordinate of top left corner of the flag.
        y_origin (int): y-value coordinate of top left corner of the flag.
    """
    pygame.draw.rect(screen, BLUE, (x_origin, y_origin, 30, 60))
    pygame.draw.rect(screen, WHITE, (x_origin + 30, y_origin, 30, 60))
    pygame.draw.rect(screen, RED, (x_origin + 60, y_origin, 30, 60))

# --(FUNCTIONS END HERE)-------------------------------------------------

# Define main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(YOUR CODE STARTS HERE)-----------------------------------------------

    screen.fill(GREY)

    # Draw the top row, single flag
    draw_flag_france(350, 150)

    # Draw the bottom row, multiple flags
    for x in range(0, 800, 95):
        draw_flag_france(x, 420)

    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
