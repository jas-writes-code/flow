# manages player, including state switches
# basically the entire way the player interacts with the environment
# lots to do here
import pygame
from game import physics, score, procgen
import vars
from screens import viewport
from player import movements
pygame.init()

idle = physics.DoPhysics('player/idle', 66, 100, 400, 600, 0.3, 0.9, 0) # the height should almost always be 100
idle.load('player/idle')
running = physics.DoPhysics('player/running', 82, 100, 400, 600, 0.3, 0.9, 0)
running.load('player/running')
swinging = physics.DoPhysics('player/swinging', 128, 100, 400, 600, 0.3, 0.9, 0)
swinging.load('player/swinging')
destroyer = physics.DoPhysics('obstacles/destroyer', 1600, 900, -600, 450, 0, 0, -1)
destroyer.load('obstacles/destroyer')
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
            return vars.trackableHooks.index(element)


def spawn():
    global player, keys
    playerspeed = vars.speed * 0.9
    key = pygame.key.get_pressed() # controls
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        physics.DoPhysics.move(player, - playerspeed)
        player = setState(1, player)
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        physics.DoPhysics.move(player, playerspeed)
        player = setState(1, player)
    if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
        physics.DoPhysics.doJump(player)
        player = setState(1, player)
    if key[pygame.K_q]:
        player = setState(2, player)
        try:
            player.vel_x, player.vel_y = movements.swing(swinging, findHook())
        except TypeError:
            pass
    if key[pygame.K_e]:
        player = setState(2, player)
        try:
            player.vel_x, player.vel_y = movements.pull(swinging, findHook())
        except TypeError:
            pass

    if ((key[pygame.K_d] or key[pygame.K_RIGHT]) or player.vel_x > 0) and player.cur_x > 800 - player.size_x * 1.5 and vars.speed < vars.maxSpeed:
        # infinite scroll effect
        speed = vars.speed
        if destroyer.cur_x > -600:
            destroyer.cur_x -= speed
        if vars.special:
            speed = player.vel_x
        if viewport.BGSPEED < 1000:
            viewport.BGSPEED = speed * 0.5
        for element in vars.hooks:
            element.cur_x -= speed
        for element in vars.obstacles:
            element.cur_x -= speed
            index = vars.obstacles.index(element)
            if vars.obstacleRects:
                hitbox = vars.obstacleRects[index]
                hitbox.x = element.cur_x - element.size_x
                hitbox.y = element.cur_y - element.size_y
        score.update()
    else:
        if viewport.BGSPEED > 0.01:
            viewport.BGSPEED *= 0.9
        else:
            viewport.BGSPEED = 0
        for element in vars.obstacles:
            element.vel_x *= 0.9
        for element in vars.hooks:
            element.vel_x *= 0.9
        if vars.gameScore >= 5000:
            destroyer.cur_x += 2

    if player.cur_x < destroyer.cur_x:
        vars.gameState = 2

    for event in pygame.event.get(): # reset back to idle state when you release a key
        if keys < 0:
            keys = 0
        if event.type == pygame.KEYDOWN:
            keys += 1
            if event.key == pygame.K_ESCAPE:
                vars.gameState = -1
            if event.key == pygame.K_o:
                vars.gameState = 2
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT, pygame.K_w, pygame.K_SPACE, pygame.K_UP, pygame.K_q, pygame.K_e]:
                if keys != 1:
                    keys -= 1
                else:
                    player = setState(0, player)
                    keys = 0
        if event.type == pygame.QUIT:
            vars.gameState = -1

    player.spawn()
    destroyer.spawn()
    player.vel_y, player.vel_x = player.getCollisions()
    player.updateVel()
    destroyer.updateVel()
