import numpy as np
import matplotlib.pyplot as plt
import pygame as pg

import pygame
import sys

pygame.init()  # Initialize pygame modules

# Set up display
screen_size = (800, 600)
RESOLUTION = 20
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pygame Boilerplate")


clock = pygame.time.Clock()  # Create clock to manage frame rate
FPS = 30  # Set frames per second to 30
clock.tick(FPS)


def get_mouse_position():
    # Get mouse position if the game is running and mouse is on screen
    return pygame.mouse.get_pos()
# def color_desnsity()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            running = False

    screen.fill((0, 0, 0))  # Fill background with black
    mouse_pos = get_mouse_position()
    print("Mouse Position:", mouse_pos)
    # Draw a red square at mouse position
    rect = (RESOLUTION * (mouse_pos[0] // RESOLUTION), RESOLUTION *
            (mouse_pos[1] // RESOLUTION), RESOLUTION, RESOLUTION)
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()  # Update display
    clock.tick(FPS)  # Limit to 30 frames per second

pygame.quit()
sys.exit()
