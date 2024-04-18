"""
File: example1.py
Author: DAVE CHENG
Date: 2024-04-18
Description: Draws graphics using functions, Level 1 example.
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

def draw_flag_france():
    """
    Draws a French flag with top left corner at (50, 50).

    Parameters:
        none
    """
    pygame.draw.rect(screen, BLUE, (50, 50, 30, 60))
    pygame.draw.rect(screen, WHITE, (80, 50, 30, 60))
    pygame.draw.rect(screen, RED, (110, 50, 30, 60))


def draw_flag_germany():
    """
    Draws a German flag with top left corner at (200, 50).

    Parameters:
        none
    """
    pygame.draw.rect(screen, BLACK, (200, 50, 90, 20))
    pygame.draw.rect(screen, RED, (200, 70, 90, 20))
    pygame.draw.rect(screen, GOLD, (200, 90, 90, 20))


def draw_flag_japan():
    """
    Draws a Japanese flag with top left corner at (350, 50).

    Parameters:
        none
    """
    pygame.draw.rect(screen, WHITE, (350, 50, 90, 60))
    pygame.draw.circle(screen, RED, (395, 80), 20)

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

    draw_flag_france()
    draw_flag_germany()
    draw_flag_japan()

    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
