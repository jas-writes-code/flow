import pygame
import json
pygame.init()

gameState = 0
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
config = json.load(open('settings.json'))
running = True
titleSize = 0
gameScore = 0
speed = 5
maxSpeed = 15
special = False
dynamicColour = [0, 0, 0]
obstacles = []
obstacleRects = []
trackableHooks = []
hooks = []
accel = 1


def clearstate():
    global gameState, screen, clock, config, running, titleSize, gameScore, speed, maxSpeed, special, dynamicColour, obstacles, obstacleRects, trackableHooks, hooks, accel
    gameState = 0
    screen = pygame.display.set_mode((1600, 900))
    clock = pygame.time.Clock()
    config = json.load(open('settings.json'))
    running = True
    titleSize = 0
    gameScore = 0
    speed = 6.5
    maxSpeed = 15
    special = False
    dynamicColour = [0, 0, 0]
    obstacles = []
    obstacleRects = []
    trackableHooks = []
    hooks = []
    accel = 1
