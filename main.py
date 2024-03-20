import pygame
import pyaudio
import random
import time
import math
import os
import json

pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("FlowGame")
clock = pygame.time.Clock()

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
        screen.blit(title, (800 - size * 2, 50))
    else:
        title = pygame.transform.scale(title, (nsize * 4, nsize * 3))
        screen.blit(title, (800 - nsize * 2, 50))

def titleSun():
    nsize = 833
    if size <= nsize:
        pygame.draw.circle(screen, '#f9ac53', (800, 300+size), size)
    else:
        pygame.draw.circle(screen, '#f9ac53', (800, 300+nsize), nsize)

while false:
    screen.fill('#94167f')
    titleSun()
    titleSwoop()
    size += 1
    pygame.display.update()
    clock.tick(frames)
