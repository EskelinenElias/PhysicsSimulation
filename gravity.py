import pygame
import sys
import math
import random
import numpy
import time
from typing import List
from object import Object
from object import G

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1400, 800
BG_COLOR = (0, 0, 0)
OBJECT_COLOR = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]
T = 0.01

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")


def randomColor() -> tuple: 
    return (255, 255, 255)#(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generateObject(number: int = 3, massRange: tuple = (1e10, 1e15)) -> Object: 
    for _ in range(number): 
        yield Object(random.gauss(WIDTH / 2, WIDTH / 4), \
                      random.gauss(HEIGHT / 2, HEIGHT / 4), \
                        random.uniform(massRange[0], massRange[1]), \
                            randomColor(), random.gauss(0, 0.5), random.gauss(0, 0.5))
        
# Create three objects
objects: List[Object] = []
for object in generateObject(random.randint(10, 20), (1E3, 1E6)): 
    objects.append(object)
objects[-1].density = 2E5
objects[-1].setMass(1E9)
objects[-1].vel_x = 0
objects[-1].vel_y = 0
objects[-1].x = WIDTH / 2
objects[-1].y = HEIGHT / 2





# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BG_COLOR)

    # Calculate gravitational forces
    object: Object
    for i, object in enumerate(objects):
        otherObjects = []
        for j, otherObject in enumerate(objects): 
            if j != i: 
                otherObjects.append(otherObject)
        object.apply_gravity(otherObjects)
        object.update()
        r, g, b = 0, 0, 0
        for point in object.path:
            pygame.draw.circle(screen, (r, g, b), point, 1)
            r += (1 * (r < 255))
            g += (1 * (g < 255))
            b += (1 * (b < 255))
        pygame.draw.circle(screen, object.color, (int(object.x), int(object.y)), object.radius)


    # Update the display
    pygame.display.flip()
    time.sleep(T)

# Quit Pygame
pygame.quit()
sys.exit()