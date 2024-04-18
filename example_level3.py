"""
File: example3.py
Author: DAVE CHENG
Date: 2024-04-18
Description: Draws graphics using functions, Level 3 example.
"""

import pygame
import sys
import random

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

def draw_flag_vertical(x_origin, y_origin, colour1=RED, colour2=WHITE, colour3=RED):
    """
    Draws a three-stripe vertical flag of 90x60 dimensions.

    Parameters:
        x_origin (int): x-value coordinate of top left corner of the flag.
        y_origin (int): y-value coordinate of top left corner of the flag.
        colour1 (tuple, optional): RGB colour of the first bar. Default is RED.
        colour2 (tuple, optional): RGB colour of the second bar. Default is WHITE.
        colour3 (tuple, optional): RGB colour of the third bar. Default is RED.
    """
    pygame.draw.rect(screen, colour1, (x_origin, y_origin, 30, 60))
    pygame.draw.rect(screen, colour2, (x_origin + 30, y_origin, 30, 60))
    pygame.draw.rect(screen, colour3, (x_origin + 60, y_origin, 30, 60))


def draw_flag_horizontal(x_origin, y_origin, colour1=RED, colour2=WHITE, colour3=RED):
    """
    Draws a three-stripe horizontal flag of 90x60 dimensions.

    Parameters:
        x_origin (int): x-value coordinate of top left corner of the flag.
        y_origin (int): y-value coordinate of top left corner of the flag.
        colour1 (tuple, optional): RGB colour of the first bar. Default is RED.
        colour2 (tuple, optional): RGB colour of the second bar. Default is WHITE.
        colour3 (tuple, optional): RGB colour of the third bar. Default is RED.
    """
    pygame.draw.rect(screen, colour1, (x_origin, y_origin, 90, 20))
    pygame.draw.rect(screen, colour2, (x_origin, y_origin + 20, 90, 20))
    pygame.draw.rect(screen, colour3, (x_origin, y_origin + 40, 90, 20))

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

    # Draw the top row, single flag, default colours
    draw_flag_vertical(350, 50)
    
    # Iterate to fill the bottom with German flags
    for x in range(0, 800, 95):
        for y in range(150, 500, 65):
            draw_flag_horizontal(x, y, BLACK, RED, GOLD)
                                 
    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
