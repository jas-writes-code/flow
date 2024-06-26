import math
import vars
import pygame
pygame.init()

def swing(player, index):
    try:
        element = vars.trackableHooks[index]
        polarVel = math.sqrt(player.vel_x ** 2 + player.vel_y ** 2)
        diffX = element.cur_x - player.cur_x
        dist = math.sqrt(abs(element.cur_x - player.cur_x)**2 + abs(element.cur_y - player.cur_y))
        velY = math.cos(90 - math.sin(diffX / dist)) * polarVel
        velX = math.sin(90 - math.sin(diffX / dist)) * polarVel + vars.speed * 0.45
        pygame.draw.line(vars.screen, '#6666ff', (player.cur_x + player.size_x - 16, player.cur_y - player.size_y + 9), (element.cur_x, element.cur_y), 5)
        vars.special = True
        return velX, velY
    except TypeError:
        vars.special = False

def pull(player, index):
    try:
        element = vars.trackableHooks[index]
        dist = math.sqrt(abs(element.cur_x - player.cur_x)**2 + abs(element.cur_y - player.cur_y)**2)
        diffX = element.cur_x - player.cur_x
        diffY = element.cur_x - player.cur_x
        boost = dist / vars.maxSpeed
        velY = -(boost + diffY) / 20
        velX = (boost + diffX) / 20
        pygame.draw.line(vars.screen, '#6666ff', (player.cur_x + player.size_x - 16, player.cur_y - player.size_y + 9), (element.cur_x, element.cur_y), 5)
        vars.special = True
        return velX, velY
    except TypeError:
        vars.special = False
