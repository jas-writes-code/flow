import pygame
import json
pygame.init()

global gameState
gameState = 0
global key
key = pygame.key.get_pressed()
global screen
screen = pygame.display.set_mode((1600, 900))
global clock
clock = pygame.time.Clock()
global config
config = json.load(open('settings.json'))
global running
running = True
