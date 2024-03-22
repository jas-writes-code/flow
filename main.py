# this main file will determine the game's state
# and what screen to show at what time
# it will also do the dev credits on game start

import pygame
import time
import math
import os

from screens import title
from environment import beats
import vars
pygame.init()

pygame.display.set_caption("FlowGame")
false = True
while false:
    beats.detect()  # still needs writing
    
    if vars.gameState == 0:
        title.titleScreen()

#    if vars.gameState == 1: <-- game is active

    if vars.gameState == -1:
        false = False
