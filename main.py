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
if _frames == "high":
    frames = 60
else:
    frames = 30
size = 1

while True:
    screen.fill('#94167f')
    pygame.draw.circle(screen, '#f9ac53', (800, 450), size)
    size += 1
    pygame.display.update()
    clock.tick(frames)
