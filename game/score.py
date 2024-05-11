import math
import vars
chaos = vars.config["gameplay"]["chaos"]
multiplier = vars.config["gameplay"]["multiplier"]

def update():
    vars.gameScore = math.ceil(vars.gameScore + (1 - 1 / chaos) + (2 - 1 / vars.speed) + (2 * multiplier) + 1)
    if vars.gameScore < 0:
        vars.gameScore += abs(vars.gameScore) + 1
    if 10 > vars.gameScore / vars.accel > 1:
        vars.speed *= 1.3 * multiplier
        vars.maxSpeed *= 1.3 * multiplier
        vars.accel *= 10

def bonus(amt):
    vars.gameScore = vars.gameScore + multiplier * amt

def dock(amt):
    vars.gameScore = vars.gameScore - 3 * multiplier * amt
