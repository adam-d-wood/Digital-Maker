import pygame
from pygame.locals import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas

class Ball:

    def __init__(self, x, y, r, elasticity, colour):
        self.x = x
        self.y = y
        self.r = r
        self.elasticity = elasticity
        self.v = 0
        self.colour = colour
        self.past_positions = [[int(x), int(y)]]

    def update_velocity(self, g, ground):
        if self.y > ground - self.r and self.v > 0:
            self.v *= -self.elasticity
        else :
            self.v += g
    
    def update_y_pos(self):
        self.y += self.v
        self.past_positions.append([int(self.x), int(self.y)])
    
    def check_energy(self, g, ground):
        if (self.y - (ground-self.r)) * g > 0.5 * self.v**2:
            # stop the animation at this point
            self.y = ground - self.r
            self.v = 0

    def update_dynamics(self, g, ground):
        self.update_velocity(g, ground)
        self.update_y_pos()
        self.check_energy(g, ground)

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, int(self.y)), self.r)
    
    def draw_trail(self, surface, n, k):
        N = min(n, len(self.past_positions))
        for i in range(0, N, k):
            position = self.past_positions[-N+i]
            colour = adjust_hsla(self.colour, 0, 0, 50/n*(N-i), 0)
            pygame.draw.circle(surface, colour, (position[0], position[1]), self.r)


def fromHSLA(h, s, l, a):
    '''returns a pygame.Color object with the specified HSLA vals'''
    colour = pygame.Color(0, 0, 0)
    colour.hsla = (h,s,l,a)
    return colour

def adjust_hsla(colour, h_pcent, s_pcent, l_pcent, a_pcent):
    pcent_changes = [h_pcent, s_pcent, l_pcent, a_pcent]
    [h, s, l, a] = [int(colour.hsla[i] * (1 + pcent_changes[i]/100)) for i in range(4)]
    # new_l = int(l * (1 + h_pcent/100))
    new_colour = pygame.Color(0, 0, 0)
    new_colour.hsla = (h % 360, s, l, a)
    return new_colour

pygame.init()

window_size = (1920, 1080)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# define constants
g = 1
ground = window_size[1]*0.9

# initialise balls
balls = []
n = 25 # number of balls
sep = window_size[0] / n # the seperation between balls
hue_increment = 360 / n
for i in range(n):
    colour = fromHSLA(i * hue_increment, 40, 50, 100)
    x = int((i + 0.5) * sep)
    ball = Ball(x, 50 + 33 * i , 30, 1, colour)
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
        ball.draw_trail(display, 10, 2)
        ball.draw(display)

    pygame.display.flip() # display the frame
    clock.tick(30) # limits fps
