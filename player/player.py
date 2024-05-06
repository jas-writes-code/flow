# manages player, including state switches
# basically the entire way the player interacts with the environment
# lots to do here
import pygame
from game import physics, score
import vars
from screens import viewport
from player import movements
pygame.init()

idle = physics.DoPhysics('player/idle', 66, 100, 400, 600, 0.3, 0.9, 0) # the height should almost always be 100
idle.load('player/idle')
running = physics.DoPhysics('player/placeholder', 100, 100, 400, 600, 0.3, 0.9, 0)
running.load('player/placeholder')
swinging = physics.DoPhysics('player/swinging', 128, 100, 400, 600, 0.3, 0.9, 0)
player = idle
keys = 0

def setState(state, player):
    states = [idle, running, swinging]
    temp_x = player.cur_x
    temp_y = player.cur_y
    temp_vx = player.vel_x
    temp_vy = player.vel_y
    player = states[state]
    player.cur_x = temp_x
    player.cur_y = temp_y
    player.vel_x = temp_vx
    player.vel_y = temp_vy
    return player

def findHook():
    for element in vars.trackableHooks:
        if element.cur_x - player.cur_x <= 50:
            pass
        else:
            return element.get_x

def spawn():
    global player, keys
    key = pygame.key.get_pressed() # controls
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        physics.DoPhysics.move(player, - vars.speed)
        player = setState(1, player)
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        physics.DoPhysics.move(player, vars.speed)
        player = setState(1, player)
    if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
        physics.DoPhysics.doJump(player)
        player = setState(1, player)
    if key[pygame.K_q]:
        player = setState(2, player)
        player.vel_x, player.vel_y = movements.swing(player.cur_x, player.cur_y, player.vel_x, player.vel_y, findHook())
    if key[pygame.K_e]:
        player = setState(2, player)
        player.vel_x, player.vel_y = movements.pull(player.cur_x, player.cur_y, player.vel_x, player.vel_y, findHook())
    if ((key[pygame.K_d] or key[pygame.K_RIGHT]) or player.vel_x > 0) and player.cur_x > 725:
        if abs(viewport.BGSPEED) <= 99:
            viewport.BGSPEED += 0.5
    else:
        viewport.BGSPEED *= 0.95

    for event in pygame.event.get(): # reset back to idle state when you release a key
        if event.type == pygame.KEYDOWN:
            keys += 1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT, pygame.K_w, pygame.K_SPACE, pygame.K_UP, pygame.K_q, pygame.K_e]:
                if keys != 1:
                    keys -= 1
                else:
                    player = setState(0, player)
                    keys -= 1
        if event.type == pygame.QUIT:
            vars.gameState = -1

    player.spawn()
    player.vel_y, player.vel_x = player.getCollisions()
    player.updateVel()
