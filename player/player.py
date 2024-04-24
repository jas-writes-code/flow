# manages player, including state switches
# basically the entire way the player interacts with the environment
# lots to do here
import pygame
from game import physics, score
import vars
from screens import viewport
pygame.init()

player = physics.DoPhysics('player/placeholder', 100, 100, 400, 600, 0.3, 0.9, 0)
player.load('player/placeholder')
def spawn():
    player.spawn()
    player.vel_y, player.vel_x = player.getCollisions()
    player.updateVel()

    key = pygame.key.get_pressed() # controls
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        physics.DoPhysics.move(player, - vars.speed)
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        physics.DoPhysics.move(player, vars.speed)
    if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
        physics.DoPhysics.doJump(player)
    if ((key[pygame.K_d] or key[pygame.K_RIGHT]) or player.vel_x > 0) and player.cur_x > 725:
        if abs(viewport.BGSPEED) <= 99:
            viewport.BGSPEED += 0.1
    else:
        viewport.BGSPEED *= 0.95
