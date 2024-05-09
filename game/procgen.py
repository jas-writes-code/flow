import copy
import pygame
import random
from game import physics
import vars
pygame.init()

hookid = 0 # incremental id is deprecated now; the id is used to identify obstacle type instead
hooks = []
chaos = vars.config["gameplay"]["chaos"] # determines chance of obstacles spawning -- default: 16
square2 = physics.DoPhysics('obstacles/chess2', 125, 125, 0, 0, 0, 0, 4)
square1 = physics.DoPhysics('obstacles/chessboard', 150, 150, 0, 0, 0, 0, 3)
tall = physics.DoPhysics('obstacles/tall', 157, 300, 0, 0, 0, 0, 2)
laser = physics.DoPhysics('obstacles/laser', 600, 60, 0, 0, 0, 0, 1)
hook = physics.DoPhysics('obstacles/hook', 72, 100, 0, 0, 0, 0, hookid)
square1.load('obstacles/chessboard')
tall.load('obstacles/tall')
laser.load('obstacles/laser')
hook.load('obstacles/hook')
square2.load('obstacles/chess2')
available = (tall, square1, square2)

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
        newLaser = copy.copy(laser)
        laserRect = newLaser.setRect()
        newLaser.cur_y = 650
        newLaser.cur_x = 1850
        laserRect.x = newLaser.cur_x - newLaser.size_x / 2
        laserRect.y = newLaser.cur_y - newLaser.size_y / 2
        vars.obstacleRects.append(laserRect)
        vars.obstacles.append(newLaser)
    elif object == 3: # this should only trigger at the start
        object = random.randint(0, len(available) - 1)
        newObs = copy.copy(available[object - 1])
        newObs.cur_y = 100 * random.randint(1, 7)
        newObs.cur_x = 1700
        obsRect = newObs.setRect()
        obsRect.x = newObs.cur_x - newObs.size_x / 2
        obsRect.y = newObs.cur_y - newObs.size_y / 2
        vars.obstacleRects.append(obsRect)
        vars.obstacles.append(newObs)
    else:
        object = random.randint(0, len(available) - 1)
        newObs = copy.copy(available[object - 1])
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

    for element in vars.obstacles:
        index = vars.obstacles.index(element)
        if element.cur_x <= -250:
            vars.obstacles.remove(element)
            vars.obstacleRects.remove(vars.obstacleRects[index])
        element.spawn()
    for element in hooks: # update lists and remove old objects
        if 600 < element.cur_x < 1350 and element not in vars.trackableHooks:
            vars.trackableHooks.append(element)
        if element.cur_x < 600 and element in vars.trackableHooks:
            vars.trackableHooks.remove(element)
        if element.cur_x < -50:
            hooks.remove(element)
        element.spawn()

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
                    try:
                        if vars.obstacles[-2].id != 1:
                            if lasernhook() == 1: # only spawn lasers if there is a hook nearby
                                spawn(1)
                                return
                    except IndexError:
                        pass
                    spawn(0)

    # for element in vars.obstacleRects:
    #     pygame.draw.rect(vars.screen, '#00ff00', element, 10, 0)
    # if len(vars.obstacleRects) != len(vars.obstacles):
    #     for element in vars.obstacleRects:
    #         print(element.x)
    #     print("-------------")
    #     for element in vars.obstacles:
    #         print(int(element.cur_x - element.size_x))
    #     print("===============")
