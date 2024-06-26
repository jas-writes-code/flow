import pygame
import vars

from game import procgen, score
from screens import viewport
from player import player
pygame.init()

# start viewport and spawn player
# start game
# increase score
# run proc gen every 10 ticks

_frames = vars.config['video']['fps']
if _frames == True:
    frames = 60
else:
    frames = 30

def notYet():
    clearstate()
    viewport.paint()  # background elements including score
    if vars.clock % 10 == 0:
        procgen.tick()  # obstacles and hooks
    score.update()
    player.spawn()
    vars.clock.tick(frames)

def start():
    viewport.paint()
    procgen.tick()
    player.spawn()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vars.gameState = -1
