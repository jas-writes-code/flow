import pygame

import vars
from game import procgen, score, physics
from screens import viewport
pygame.init()

# start viewport and spawn player
# start game
# increase score
# run proc gen every 10 ticks

_frames = vars.config['video']['fps']
if _frames == "high":
    frames = 60
else:
    frames = 30

def start():
    clearstate()
    viewport.paint()
    if vars.clock % 10 == 0:
        procgen.tick()
    score.update()
    vars.clock.tick(frames)

def clearstate():
    vars.gameScore = 0
    vars.speed = 0
