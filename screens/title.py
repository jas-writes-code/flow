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
if _frames == "high":
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
    btnStart_scaled = pygame.transform.scale(btnStart, (1, 1))
    btnOpt_scaled = pygame.transform.scale(btnOpt, (1, 1))
    btnQuit_scaled = pygame.transform.scale(btnQuit, (1, 1))
    btnCredits_scaled = pygame.transform.scale(btnCredits, (1, 1))

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

    return btnStart_scaled, btnOpt_scaled, btnQuit_scaled, btnCredits_scaled

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
    start, opt, quit, credits = menuButtons()
    if vars.titleSize < 834:
        vars.titleSize += 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            loc = pygame.mouse.get_pos()
            if start.get_rect().collidepoint(loc):
                vars.gameState = 1
            if quit.get_rect().collidepoint(loc):
                vars.gameState = -1
            if opt.get_rect().collidepoint(loc):
                vars.gameState = 2
                print(vars.gameState)
            if credits.get_rect().collidepoint(loc):
                vars.gameState = 3
                print(vars.gameState)
        if event.type == pygame.QUIT:
            vars.gameState = -1
    pygame.display.update()
    vars.clock.tick(frames)
