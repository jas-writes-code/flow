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
if _frames == "high":
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

def clearstate():
    vars.gameScore = 0
    vars.speed = 0

def start():
    viewport.paint()
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_a]:
        if viewport.BGSPEED > -10:
            viewport.BGSPEED -= 1
    if keys_pressed[pygame.K_d]:
        if viewport.BGSPEED < 99: # for some reason this breaks if it goes above 100
            viewport.BGSPEED += 1
    if keys_pressed[pygame.K_SPACE]:
        viewport.BGSPEED = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vars.gameState = -1
