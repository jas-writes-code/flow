# updates score
# do some maths with the multiplier in settings, the current score, the speed and the chaos level
# not entirely sure how to do said maths yet
import math
import vars
chaos = vars.config["gameplay"]["chaos"]
multiplier = vars.config["gameplay"]["multiplier"]
accel = 1

def update():
    global accel
    vars.gameScore = math.ceil(vars.gameScore + (1 - 1 / chaos) + (2 - 1 / vars.speed) + (2 * multiplier) + 1)
    if vars.gameScore < 0:
        vars.gameScore += abs(vars.gameScore) + 1
    if 10 > vars.gameScore / accel > 1:
        vars.speed *= 1.3
        accel *= 10

def bonus(amt):
    vars.gameScore = vars.gameScore + multiplier * amt

def dock(amt):
    vars.gameScore = vars.gameScore - 3 * multiplier * amt

# not sure if the bonus/dock functions are gonna be used yet but it's probably nice to have them
