import pygame
import pyaudio
import random
import time
import math
import os
import json

import vars
pygame.init()

def titleScreen():
    _settings = json.load(open('settings.json'))
    _frames = _settings['video']['fps']
    false = True
    if _frames == "high":
        frames = 60
    else:
        frames = 30
    size = 1

    def titleSwoop():
        title = pygame.image.load('assets/title.png')
        nsize = 150
        if size <= nsize:
            title = pygame.transform.scale(title, (size * 4, size * 3))
            vars.screen.blit(title, (800 - size * 2, 50))
        else:
            title = pygame.transform.scale(title, (nsize * 4, nsize * 3))
            vars.screen.blit(title, (800 - nsize * 2, 50))

    def titleSun():
        nsize = 833
        if size <= nsize:
            pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+size), size)
        else:
            pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+nsize), nsize)

    while false:
        vars.screen.fill('#94167f')
        titleSun()
        titleSwoop()
        size += 1
        pygame.display.update()
        vars.clock.tick(frames)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vars.gameState = -1
