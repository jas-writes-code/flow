import pygame
import json
pygame.init()

global gameState
gameState = 0
global screen
screen = pygame.display.set_mode((1600, 900))
global clock
clock = pygame.time.Clock()
global config
config = json.load(open('settings.json'))
global running
running = True
global titleSize
titleSize = 0
global gameScore
gameScore = 0
global speed
speed = 3
global maxSpeed
maxSpeed = 15
global special
special = False
global dynamicColour
dynamicColour = [255, 255, 255]
global obstacles
obstacles = []
global obstacleRects
obstacleRects = []
global trackableHooks
trackableHooks = []
