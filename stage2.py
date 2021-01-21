import pygame
from pygame.locals import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas

pygame.init()

window_size = (1000, 1000)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# define constants
g = 1
r = 30
ground = window_size[1]*0.9
elasticity = 0.1

# initialise variables
x = window_size[0] // 2
y = 50
v = 0

running = True
while running:

	# check for exit button press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	
	# update velocity
    if y > ground - r and v > 0:
        v *= -elasticity
    else :
        v += g

	# update y-pos
    y += v

    # check whether ball will
    # bounce back above ground
    if (y - (ground-r)) * g > 0.5 * v**2:
    # stop the animation at this point
        y = ground - r
        v = 0

	# draw onto screen
    display.fill((20, 20, 20))
    pygame.draw.circle(display, (255, 0, 0), (x, int(y)), r)
    pygame.draw.line(display, (255, 255, 255), (0, ground), (window_size[0], ground))
    pygame.display.flip() # display the frame
    clock.tick(30) # limits fps
