import pygame
import time
import math
import os

import vars
pygame.init()

title_img = pygame.image.load('assets/title.png')
btnStart = pygame.image.load('assets/newgame.png')
btnOpt = pygame.image.load('assets/options.png')
btnQuit = pygame.image.load('assets/quit.png')
btnCredits = pygame.image.load('assets/credits.png')
_frames = vars.config['video']['fps']
if _frames == True:
    frames = 60
else:
    frames = 30
vars.titleSize = 1

def titleSwoop():
    nsize = 150
    if vars.titleSize <= nsize:
        title = pygame.transform.scale(title_img, (vars.titleSize * 4, vars.titleSize * 3))
        vars.screen.blit(title, (800 - vars.titleSize * 2, 50))
    else:
        title = pygame.transform.scale(title_img, (nsize * 4, nsize * 3))
        vars.screen.blit(title, (800 - nsize * 2, 50))

def menuButtons():
    nsize = 150
    delay = 90

    if delay < vars.titleSize < nsize:
        btnStart_scaled = pygame.transform.scale(btnStart, ((vars.titleSize - delay) * 8, vars.titleSize * 1.25 - delay))
        vars.screen.blit(btnStart_scaled, (800 - (vars.titleSize - delay) * 4, 500))

        btnOpt_scaled = pygame.transform.scale(btnOpt, ((vars.titleSize - delay) * 4, vars.titleSize - delay))
        vars.screen.blit(btnOpt_scaled, (600 - (vars.titleSize - delay) * 2, 650))

        btnQuit_scaled = pygame.transform.scale(btnQuit, ((vars.titleSize - delay) * 2, vars.titleSize - delay))
        vars.screen.blit(btnQuit_scaled, (800 - (vars.titleSize - delay), 750))

        btnCredits_scaled = pygame.transform.scale(btnCredits, ((vars.titleSize - delay) * 4, vars.titleSize - delay))
        vars.screen.blit(btnCredits_scaled, (1000 - (vars.titleSize - delay) * 2, 650))

    elif vars.titleSize >= nsize:
        btnStart_scaled = pygame.transform.scale(btnStart, ((nsize - delay) * 8, nsize * 1.25 - delay))
        vars.screen.blit(btnStart_scaled, (800 - (nsize - delay) * 4, 500))

        btnOpt_scaled = pygame.transform.scale(btnOpt, ((nsize - delay) * 4, nsize - delay))
        vars.screen.blit(btnOpt_scaled, (600 - (nsize - delay) * 2, 650))

        btnQuit_scaled = pygame.transform.scale(btnQuit, ((nsize - delay) * 2, nsize - delay))
        vars.screen.blit(btnQuit_scaled, (800 - (nsize - delay), 750))

        btnCredits_scaled = pygame.transform.scale(btnCredits, ((nsize - delay) * 4, nsize - delay))
        vars.screen.blit(btnCredits_scaled, (1000 - (nsize - delay) * 2, 650))

    return nsize, delay

def titleSun():
    nsize = 833
    if vars.titleSize <= nsize:
        pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+vars.titleSize), vars.titleSize)
    else:
        pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+nsize), nsize)


def titleScreen():
    vars.screen.fill('#94167f')
    titleSun()
    titleSwoop()
    nsize, delay = menuButtons()
    vars.titleSize += 1
    if vars.gameState != 0:
        print(vars.gameState)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            loc = pygame.mouse.get_pos()
            if delay < vars.titleSize < nsize:
                if (800 - (vars.titleSize - delay) * 4) < loc[0] < (800 + (vars.titleSize - delay) * 4) and 500 < loc[1] < (500 + (vars.titleSize * 1.25 - delay)):
                    vars.gameState = 1  # do this if the start button is pressed
                if 800 - (vars.titleSize - delay) * 2 < loc[0] < 800 + (vars.titleSize - delay) and 750 < loc[1] < 750 + vars.titleSize - delay:
                    vars.gameState = -1  # do this if the quit button is pressed
                if 600 - (vars.titleSize - delay) * 2 < loc[0] < 600 + (vars.titleSize - delay) * 2 and 650 < loc[1] < 650 + vars.titleSize - delay:
                    vars.gameState = 4  # do this if the options button is pressed
                if 1000 - (vars.titleSize - delay) * 2 < loc[0] < 1000 + (vars.titleSize - delay) * 2 and 650 < loc[1] < 650 + vars.titleSize - delay:
                    vars.gameState = 3  # do this if the credits button is pressed
            if vars.titleSize >= nsize:  # same pattern as above
                if (800 - (nsize - delay) * 4) < loc[0] < (800 + (nsize - delay) * 4) and 500 < loc[1] < (500 + (nsize * 1.25 - delay)):
                    vars.gameState = 1
                if 800 - (nsize - delay) * 2 < loc[0] < 800 + (nsize - delay) and 750 < loc[1] < 750 + nsize - delay:
                    vars.gameState = -1
                if 600 - (nsize - delay) * 2 < loc[0] < 600 + (nsize - delay) * 2 and 650 < loc[1] < 650 + nsize - delay:
                    vars.gameState = 4
                if 1000 - (nsize - delay) * 2 < loc[0] < 1000 + (nsize - delay) * 2 and 650 < loc[1] < 650 + nsize - delay:
                    vars.gameState = 3
        if event.type == pygame.QUIT:
            vars.gameState = -1
    vars.clock.tick(frames)
