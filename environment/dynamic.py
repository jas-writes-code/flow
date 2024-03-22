import vars
import pygame
import time
import math
import os
pygame.init()

def flashEnv(strength):  # create flashes on transparent sections of the background, where available
    strength = (vars.config['video']['amp'] / 100) * strength
    bright = 0
    target = strength * 2.55
    for i in range (0, 20):
        if i <= 6:
            bright = bright + (target / 6)
            vars.screen.fill((bright, bright, bright))
        if i > 10:
            bright = bright - (target / 10)
            vars.screen.fill((bright, bright, bright))

def flashElements(strength):  # create flashes on transparent sections of individual elements
    elements = 14  # this does nothing
