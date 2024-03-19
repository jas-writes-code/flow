import pygame
import pyaudio
import random
import time
import math
import os
import json
pygame.init()

width = random.randint(100, 1000)
height = random.randint(100, 1000)
screen = pygame.display.set_mode((width, height))

_settings = json.load(open('settings.json'))
frames = _settings['video']['fps']
if frames == "high":
    _frames = 60
else:
    _frames = 30

while True:
    pygame.clock.tick(_frames)
