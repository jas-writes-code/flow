import pygame
pygame.init()

global gameState
gameState = 0
global key
key = pygame.key.get_pressed()
global screen
screen = pygame.display.set_mode((1600, 900))
global clock
clock = pygame.time.Clock()
