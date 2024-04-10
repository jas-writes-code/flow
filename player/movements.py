import math
import vars

def swing(curX, curY, velX, velY, hookID):
    for element in vars.trackableHooks:
        if element.id == hookID:
            polarVel = math.sqrt(velX ** 2 + velY ** 2)
            diffX = element.cur_x - curX
            dist = math.sqrt(abs(element.cur_x - curX)**2 + abs(element.cur_y - curY))
            velY = math.cos(90 - math.sin(diffX / dist)) * polarVel
            velX = math.sin(90 - math.sin(diffX / dist)) * polarVel
    return velX, velY

def pull(curX, curY, velX, velY, hookID):
    for element in vars.trackableHooks:
        if element.id == hookID:
            dist = math.sqrt(abs(element.cur_x - curX)**2 + abs(element.cur_y - curY))
            diffX = element.cur_x - curX
            diffY = element.cur_x - curX
            boost = dist / vars.maxSpeed
            velY = boost * diffY
            velX = boost + diffX
    return velX, velY
