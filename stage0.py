import pygame
from pygame.locals import *

pygame.init() # setup pygame

window_size = (1000, 1000) # set the window size to 1000px x 1000px
display = pygame.display.set_mode(window_size) # creates a pygame surface object

running = True
while running:

	# draw onto screen
    display.fill((20, 20, 20))
    pygame.display.flip() # display the frame

