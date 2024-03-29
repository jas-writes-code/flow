# this main file will determine the game's state
# and what screen to show at what time
# it will also do the dev credits on game start

import pygame
import time
import math
import os

from screens import title, credits, options
from environment import beats
from game import flowman
import vars
pygame.init()

pygame.display.set_caption("FlowGame")
while vars.running:
    beats.detect()  # still needs writing
    
    if vars.gameState == 0:
        title.titleScreen()

    if vars.gameState == 1:
        flowman.start()

    if vars.gameState == 2:
        options.options()

    if vars.gameState == 3:
        credits.credits()

    if vars.gameState == -1:
        print("Game exited in state " + str(vars.gameState))
        vars.running = False
