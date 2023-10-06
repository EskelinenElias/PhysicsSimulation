import pygame
import sys
import math
import random
import numpy as np
import time
from typing import List
from objects import Objects

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1400, 800
BG_COLOR = (0, 0, 0)
OBJECT_COLOR = (255, 255, 255)
T = 0.01
S = 1

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")
        
def drawCircles(objects: Objects, color: tuple = (255, 255, 255)) -> None: 
    for i in range(0, len(objects)):
        pygame.draw.circle(screen, color, (objects.x[0][i], objects.y[0][i]), objects.radius[0][i])
    return None

def drawPaths(objects: Objects) -> None:
    r, g, b, = 0, 0, 0
    for i in range(0, np.size(objects.path_x, axis=0)):
        for j in range(0, np.size(objects.path_x, axis=1)):
            pygame.draw.circle(screen, (r, g, b), (objects.path_x[i][j], objects.path_y[i][j]), 1)
        r += (1 * (r < 255))
        g += (1 * (g < 255))
        b += (1 * (b < 255))
    return None

def drawPathsLines(objects: Objects) -> None:
    for i in range(0, np.size(objects.x, axis=1)):
        path_points = list(zip(objects.path_x[:, i], objects.path_y[:, i]))
        if len(path_points) > 1:
            pygame.draw.lines(screen, OBJECT_COLOR, False, path_points, 1)
    return None
 
# create objects
objects = Objects()
objects.addObject(WIDTH/2, HEIGHT/2, 0, 0, 1E9, 2E5)
objects.generateObjects(15, (WIDTH*0.25, WIDTH*0.75), (HEIGHT*0.25, HEIGHT*0.75), (1E5, 1E6), (2E3, 2E4))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Calculate gravitational forces
    objects.update(T)
    drawPaths(objects)
    drawCircles(objects)

    # Update the display
    pygame.display.flip()
    time.sleep(T/S)

# Quit Pygame
pygame.quit()
sys.exit()