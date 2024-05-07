import copy
import threading

import pygame
import random
from game import physics
import vars
pygame.init()


idlist = 0
hookid = 0
hooks = []
chaos = vars.config["gameplay"]["chaos"] # determines chance of obstacles spawning -- default: 16
tall = physics.DoPhysics('obstacles/tall', 157, 300, 0, 0, 0, 0, idlist)
laser = physics.DoPhysics('obstacles/laser', 400, 40, 0, 0, 0, 0, idlist)
hook = physics.DoPhysics('obstacles/hook', 72, 100, 0, 0, 0, 0, hookid)
tall.load('obstacles/tall')
laser.load('obstacles/laser')
hook.load('obstacles/hook')
available = (tall, tall)

def obstacles50y():
    count = 0
    for element in vars.obstacles:
        if element.cur_x + element.size_x > 1550:
            count += 1
    return count

def obstacles150y():
    spawnvalue = []
    for element in vars.obstacles:
        for i in range(100, 700, 100):
            if element.cur_x + element.size_x > 1450 and element.cur_y == i:
                pass
            else:
                spawnvalue.append(i)
    return spawnvalue

def avaiblehook():
    count = len(vars.trackableHooks)
    return count

def lasernhook():
    if hooks[-1].cur_x > 1500:
        return 1
    else:
        return 0

def spawn(object):
    global idlist
    if object == 1:
        idlist += 1
        newLaser = copy.copy(laser)
        newLaser.id = idlist
        laserRect = newLaser.setRect()
        newLaser.cur_y = 650
        newLaser.cur_x = 1700
        laserRect.x = newLaser.cur_x - newLaser.size_x / 2
        laserRect.y = newLaser.cur_y - newLaser.size_y / 2
        vars.obstacleRects.append(laserRect)
        vars.obstacles.append(newLaser)
    elif object == 3: # this should only trigger at the start
        idlist += 1
        object = random.randint(0, len(available))
        newObs = copy.copy(available[object - 1])
        newObs.id = idlist
        newObs.cur_y = 100 * random.randint(1, 7)
        newObs.cur_x = 1700
        obsRect = newObs.setRect()
        obsRect.x = newObs.cur_x - newObs.size_x / 2
        obsRect.y = newObs.cur_y - newObs.size_y / 2
        vars.obstacleRects.append(obsRect)
        vars.obstacles.append(newObs)
    else:
        idlist += 1
        object = random.randint(0, len(available))
        newObs = copy.copy(available[0])
        newObs.id = idlist
        spawnable = obstacles150y()
        newObs.cur_y = spawnable[random.randint(0, len(obstacles150y()) - 1)]
        newObs.cur_x = 1700
        obsRect = newObs.setRect()
        obsRect.x = newObs.cur_x - newObs.size_x / 2
        obsRect.y = newObs.cur_y - newObs.size_y / 2
        vars.obstacleRects.append(obsRect)
        vars.obstacles.append(newObs)

def tick():
    global hookid
    randomnumber = random.randint(0,100)

    for element in hooks: # update lists and remove old things
        if 600 < element.cur_x < 1350 and element not in vars.trackableHooks:
            vars.trackableHooks.append(element)
        if element.cur_x < 600 and element in vars.trackableHooks:
            vars.trackableHooks.remove(element)
        if element.cur_x < -50:
            hooks.remove(element)
        element.spawn()
    for element in vars.obstacles:
        index = vars.obstacles.index(element)
        if vars.obstacleRects:
            if vars.obstacleRects[index].x + element.size_x < -100:
                vars.obstacleRects.remove(vars.obstacleRects[index])
        if element.cur_x <= -100:
            vars.obstacles.remove(element)
        element.spawn()
        pygame.draw.rect(vars.screen, '#ff0000', element, 15, 0) # hitbox on elements, doesn't affect collision

    if hooks == [] or hooks[-1].cur_x < 1000: # if a hook can be spawned, spawn it
        if randomnumber / 3 * 2 < chaos:
            hookid += 1
            newHook = copy.copy(hook)
            newHook.id = hookid
            newHook.cur_y = 125
            newHook.cur_x = 1650
            hooks.append(newHook)

    if vars.obstacles == []: # if no obstacles are in the list, add one
        spawn(3)
    if randomnumber < chaos: # if we can spawn a new obstacle, do that
        check1 = obstacles50y()
        check2 = obstacles150y()
        check3 = avaiblehook()
        if check1 == 0:
            if check2 is not None:
                if check3 != 0:
                    if lasernhook() == 1: # only spawn lasers if there is a hook nearby
                        spawn(1)
                        return
                    spawn(0)
