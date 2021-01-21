import pygame
from pygame.locals import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas

class Ball:

    def __init__(self, x, y, r, elasticity):
        self.x = x
        self.y = y
        self.r = r
        self.elasticity = elasticity
        self.v = 0

    def update_velocity(self, g, ground):
        if self.y > ground - self.r and self.v > 0:
            self.v *= -self.elasticity
        else :
            self.v += g
    
    def update_y_pos(self):
        self.y += self.v
    
    def check_energy(self, ground):
        if (self.y - (ground-self.r)) * g > 0.5 * self.v**2:
            # stop the animation at this point
            self.y = ground - self.r
            self.v = 0

    def update_dynamics(self, g, ground):
        self.update_velocity(g, ground)
        self.update_y_pos()
        self.check_energy(ground)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (self.x, int(self.y)), self.r)


pygame.init()

window_size = (1000, 1000)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# define constants
g = 1
ground = window_size[1]*0.9

# initialise balls
balls = []
n = 10 # number of balls
sep = window_size[0] / n # the seperation between balls
for i in range(n):
    x = int((i + 0.5) * sep)
    ball = Ball(x, 50 + 60 * i , 30, 1)
    balls.append(ball)


running = True
while running:

	# check for exit button press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
	
    for ball in balls:
        ball.update_dynamics(g, ground)

	# draw onto screen
    display.fill((20, 20, 20))
    pygame.draw.line(display, (255, 255, 255), (0, ground), (window_size[0], ground))

    #draw balls
    for ball in balls:
        ball.draw(display)

    pygame.display.flip() # display the frame
    clock.tick(30) # limits fps
