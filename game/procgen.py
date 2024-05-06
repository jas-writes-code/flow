import pygame
import random
from game import physics
import vars
pygame.init()


idlist = 0
hookid = 0
hooks = []
chaos = vars.config["gameplay"]["chaos"] # determines chance of obstacles spawning -- default: 16
tall = physics.DoPhysics('obstacles/tall', 600, 315, 0, 0, 0, 0, idlist)
laser = physics.DoPhysics('obstacles/laser', 400, 40, 0, 0, 0, 0, idlist)
hook = physics.DoPhysics('obstacles/hook', 72, 100, 0, 0, 0, 0, hookid)
tall.load('obstacles/tall')
laser.load('obstacles/laser')
hook.load('obstacles/hook')

def obstacles50y():
    for element in vars.obstacles:
        if element.cur_x > 1550:
            return 0


def obstacles150y():
    spawnvalue = []
    for element in vars.obstacles:
        for i in range(100, 700, 100):
            if element.cur_x > 1550:
                return
            else:
                spawnvalue.append(i)
            return spawnvalue


def avaiblehook():
    spawnvalue = []
    for element in vars.trackableHooks:
        if element.cur_x < 500:
            return 0


def lasernhook():
    for element in vars.trackableHooks:
        if element.cur_x > 1500:
            return 0


def tick():
    global idlist, hookid
    randomnumber = random.randint(0,100)

    if hooks == [] or hooks[-1].cur_x < 1500: # if a hook can be spawned, spawn it
        if randomnumber / 3 * 2 < chaos:
#            hookid += 1 <-- FIX THIS!!!
            hookid = hook
            hookid.cur_y = 125
            hookid.cur_x = 1550
            hooks.append(hookid)
            print("hook spawned with id ", hookid)

    if randomnumber < chaos:
        if obstacles50y() != 0:
            if obstacles150y():
                spawnable = obstacles150y()
                spawnY = random.randint(0, len(spawnable))
                if avaiblehook() == 0:
                    if lasernhook() == 0:
                        pass

    for element in hooks:
        if 600 < element.cur_x < 1200:
            vars.trackableHooks.append(element)
        if element.cur_x < 600:
            vars.trackableHooks.remove(element)
        if element.cur_x < 50:
            hooks.remove(element)
        element.spawn()
