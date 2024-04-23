"""
File: example4_return_values.py
Author: DAVE CHENG
Date: 2024-04-23
Description: Examples of Level 4 drawing functions with return values.
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Functions")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (70, 70, 70)
RED = (255, 0, 0)


# Define functions for composite shapes
# --(FUNCTIONS START HERE)-----------------------------------------------

def draw_rectangle(x_top_left, y_top_left, width, color=WHITE):
    """
    Draws a rectangle.

    Parameteres:
        x_top_left (int): x-coordinate of the top-left corner of the rectangle.
        y_top_left (int): y-coordinate of the top-left corner of the rectangle.
        width (int): Width of the rectangle in pixels.
        color (tuple, optional): RGB colour of the rectangle. Default is WHITE.

    Returns:
        height (int): Height of the rectangle in pixels.
        
    """
    # Define the height of the rectangle based on specified width
    height = int(width // 2)
    
    # Draw rectangle at specified coordinates
    pygame.draw.rect(screen, color, (x_top_left, y_top_left, width, height))

    # Return the calculated height
    return height


def draw_flag(x_origin, y_origin, width, colour1=RED, colour2=WHITE, colour3=RED):
    """
    Draws a three-stripe vertical flag.

    Parameters:
        x_origin (int): x-coordinate of top-left corner of the flag.
        y_origin (int): y-coordinate of top-left corner of the flag.
        width (int): Width of flag in pixels.
        colour1 (tuple, optional): RGB colour of the first bar. Default is RED.
        colour2 (tuple, optional): RGB colour of the second bar. Default is WHITE.
        colour3 (tuple, optional): RGB colour of the third bar. Default is RED.

    Returns:
        height (int): Height of the flag in pixels.
    """
    # Define the height of the flag based on the specified width
    height = int(width // 1.5)

    # Draw vertical bars
    pygame.draw.rect(screen, colour1, (x_origin, y_origin, width / 3, height))
    pygame.draw.rect(screen, colour2, (x_origin + width / 3, y_origin, width / 3, height))
    pygame.draw.rect(screen, colour3, (x_origin + 2 * width / 3, y_origin, width / 3, height))
    
    # Returns the height of the flag in pixels for the specified width
    return height


def draw_church(x_base_left, y_base_bottom, width, colour=WHITE):
    """
    Draws a church with a triangular roof and a rectangular base.

    Parameters:
        x_base_left (int): x-coordinate of the bottom-left corner of the base.
        y_base_bottom (int): y-coordinate of the bottom-left corner of the base.
        width (int): Width of the church in pixels.
        colour (tuple, optional): RGB colour of the church. Default is WHITE.

    Returns:
        total_height (int): Height of the church from the base to the top in pixels.
    """
    # Calculate the height of the church
    height = width * 3 // 4  # Assuming a fixed ratio for the height relative to the width
    total_height = height + width // 2  # Total height from the base to the top

    # Define the coordinates of the roof points
    x_top_middle = x_base_left + width // 2
    y_top_middle = y_base_bottom - height

    # Draw the triangular roof
    pygame.draw.polygon(screen, colour, [(x_base_left, y_base_bottom),
                                         (x_top_middle, y_top_middle),
                                         (x_base_left + width, y_base_bottom)])

    # Draw the rectangular base of the church
    pygame.draw.rect(screen, colour, (x_base_left, y_base_bottom - width // 2, width, width // 2))

    return int(total_height)



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

    # Draw a red rectangle, 50 pixels wide
    draw_rectangle(400, 500, 50, RED)

    # For debugging, we can output the calculated height of this 50 pixel-width 
    # rectangle to the console by assigning its return value to a variable:
    #
    # rectangle_height = draw_rectangle(400, 500, 50, RED)
    # print(f"DEBUG: Drawing rectangle at (400, 500) size 50 x {rectangle_height}")
    

    # Draw an Austrian flag, 100 pixels wide
    draw_flag(100, 100, 100, RED, WHITE, RED)
        
    # For debugging, we can output the calculated height of this 100 pixel-wide
    # flag to the console by assigning its return value to a variable:
    #
    # flag_height = draw_flag(100, 100, 100, RED, WHITE, RED)
    # print(f"DEBUG: Drawing flag at (100, 100) size 100 x {flag_height}")


    # Draw a church, 200 pixels wide
    draw_church(400, 300, 200, WHITE)

    # For debugging, we can output the calculated height of this 200 pixel-wide
    # church to the console by assigning its return value to a variable:
    #
    # church_height = draw_church(400, 300, 200, WHITE)
    # print(f"DEBUG: Drawing church at (400, 300) with height = {church_height}")



    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
