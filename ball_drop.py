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

x = window_size[0] // 2
y = 50
v = 0
g = 0.5
r = 30

y_vals = []
v_vals = []

ground = window_size[1]*0.9

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y_vals.append(ground-r-y)
    v_vals.append(v)

    if y > ground - r and v > 0:
        v *= -1
    else :
        v += g
    y += v
    if (y - (ground-r)) * g > 0.5 * v**2:
        # stop the animation at this point
        y = ground - r
        v = 0

    display.fill((20, 20, 20))
    pygame.draw.circle(display, (255, 0, 0), (x, int(y)), r)
    pygame.draw.line(display, (255, 255, 255), (0, ground), (window_size[0], ground))
    pygame.display.flip()
    clock.tick(120)
    print(clock.get_fps())


y_vals = pandas.Series(y_vals)
v_vals = pandas.Series(v_vals)
fig, ax = plt.subplots()
ax.plot(y_vals.index, y_vals)
ax.plot(v_vals.index, v_vals)
# plt.xticks(np.arange(0, len(y_vals.index)))
plt.grid(True)
plt.show()


