import pygame
import random
from game import physics
import vars
pygame.init()

chaos = vars.config["gameplay"]["chaos"] # determines chance of obstacles spawning -- default: 16


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
    randomnumber = random.randint(0,100)
    if randomnumber < chaos:
        if obstacles50y() != 0:
            if obstacles150y():
                spawnable = obstacles150y()
                spawnY = random.randint(0, len(spawnable))
                if avaiblehook() == 0:
                    if lasernhook() == 0:
pass