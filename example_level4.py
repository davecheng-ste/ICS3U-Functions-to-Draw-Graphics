"""
File: example4.py
Author: DAVE CHENG
Date: 2024-04-18
Description: Draws graphics using functions, Level 4 example.
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
GREY = (70, 70, 70)
BLUE = (0, 51, 204)
RED = (204, 0, 0)
GOLD = (255, 206, 0)
GREEN = (0, 153, 51)

# Define functions for composite shapes
# --(FUNCTIOSN START HERE)-----------------------------------------------

def draw_flag_vertical(x_origin, y_origin, width, colour1=RED, colour2=WHITE, colour3=RED):
    """
    Draws a three-stripe vertical flag.

    Parameters:
        x_origin (int): x-value coordinate of top left corner of the flag.
        y_origin (int): y-value coordinate of top left corner of the flag.
        width (int): Width of flag in pixels.
        colour1 (tuple, optional): RGB colour of the first bar. Default is RED.
        colour2 (tuple, optional): RGB colour of the second bar. Default is WHITE.
        colour3 (tuple, optional): RGB colour of the third bar. Default is RED.

    Returns:
        height (int): Height of the flag in pixels.
    """
    height = width / 1.5

    pygame.draw.rect(screen, colour1, (x_origin, y_origin, width / 3, height))
    pygame.draw.rect(screen, colour2, (x_origin + width / 3, y_origin, width / 3, height))
    pygame.draw.rect(screen, colour3, (x_origin + 2 * width / 3, y_origin, width / 3, height))
    
    return height


def draw_flag_horizontal(x_origin, y_origin, width, colour1=RED, colour2=WHITE, colour3=RED):
    """
    Draws a three-stripe horizontal flag.

    Parameters:
        x_origin (int): x-value coordinate of top left corner of the flag.
        y_origin (int): y-value coordinate of top left corner of the flag.
        width (int): Width of flag in pixels.
        colour1 (tuple, optional): RGB colour of the first bar. Default is RED.
        colour2 (tuple, optional): RGB colour of the second bar. Default is WHITE.
        colour3 (tuple, optional): RGB colour of the third bar. Default is RED.

    Returns:
        height (int): Height of the flag in pixels.
    """
    height = width / 1.5

    pygame.draw.rect(screen, colour1, (x_origin, y_origin, width, height / 3))
    pygame.draw.rect(screen, colour2, (x_origin, y_origin + height / 3, width, height / 3))
    pygame.draw.rect(screen, colour3, (x_origin, y_origin + 2 * height / 3, width, height / 3))
    
    return height

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
    draw_flag_vertical(300, 50, 200)
    
    # Iterate to draw row of small German flags
    for x in range(0, 800, 55):
        draw_flag_horizontal(x, 250, 50, BLACK, RED, GOLD)
        
        # DEBUG: For debugging, output info to terminal w/ flag size and position
        #        using the function's return value to get height.
        #
        # flag_height = draw_flag_horizontal(x, 250, 50, BLACK, RED, GOLD)
        
        # print(f"Drawing 50w x {flag_height}h at x={x}, y=250")

    # Iterate to draw row of medium Italian flags
    for x in range(0, 800, 105):
        draw_flag_vertical(x, 300, 100, GREEN, WHITE, RED)

    # Iterate to draw row of large Lithuanian flags
    for x in range(0, 800, 155):
        draw_flag_horizontal(x, 380, 150, GOLD, GREEN, RED)

    # Iterate to draw row of extra large Nigerian flags
    for x in range(0, 800, 255):
        draw_flag_vertical(x, 500, 250, GREEN, WHITE, GREEN)

    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
