import pygame
import time
import math
import os

import vars
pygame.init()

def titleScreen():
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
    size = 1

    def titleSwoop():
        nonlocal size
        nsize = 150
        if size <= nsize:
            title = pygame.transform.scale(title_img, (size * 4, size * 3))
            vars.screen.blit(title, (800 - size * 2, 50))
        else:
            title = pygame.transform.scale(title_img, (nsize * 4, nsize * 3))
            vars.screen.blit(title, (800 - nsize * 2, 50))

    def menuButtons():
        nonlocal size
        nsize = 120
        delay = 60
        btnStart_scaled = None
        btnOpt_scaled = None
        btnQuit_scaled = None
        btnCredits_scaled = None

        if delay < size < nsize:
            btnStart_scaled = pygame.transform.scale(btnStart, ((size - delay) * 6, size - delay))
            vars.screen.blit(btnStart_scaled, (800 - (size - delay) * 3, 500))

            btnOpt_scaled = pygame.transform.scale(btnOpt, ((size - delay) * 4, size - delay))
            vars.screen.blit(btnOpt_scaled, (500 - (size - delay) * 2, 650))

            btnQuit_scaled = pygame.transform.scale(btnQuit, ((size - delay) * 2, size - delay))
            vars.screen.blit(btnQuit_scaled, (800 - (size - delay), 650))

            btnCredits_scaled = pygame.transform.scale(btnCredits, ((size - delay) * 4, size - delay))
            vars.screen.blit(btnCredits_scaled, (1100 - (size - delay) * 2, 650))

        elif size >= nsize:
            btnStart_scaled = pygame.transform.scale(btnStart, ((nsize - delay) * 6, nsize - delay))
            vars.screen.blit(btnStart_scaled, (800 - (nsize - delay) * 3, 500))

            btnOpt_scaled = pygame.transform.scale(btnOpt, ((nsize - delay) * 4, nsize - delay))
            vars.screen.blit(btnOpt_scaled, (500 - (nsize - delay) * 2, 650))

            btnQuit_scaled = pygame.transform.scale(btnQuit, ((nsize - delay) * 2, nsize - delay))
            vars.screen.blit(btnQuit_scaled, (800 - (nsize - delay), 650))

            btnCredits_scaled = pygame.transform.scale(btnCredits, ((nsize - delay) * 4, nsize - delay))
            vars.screen.blit(btnCredits_scaled, (1100 - (nsize - delay) * 2, 650))

        return btnStart_scaled, btnOpt_scaled, btnQuit_scaled, btnCredits_scaled

    def titleSun():
        nonlocal size
        nsize = 833
        if size <= nsize:
            pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+size), size)
        else:
            pygame.draw.circle(vars.screen, '#f9ac53', (800, 300+nsize), nsize)

    while vars.running:
        vars.screen.fill('#94167f')
        titleSun()
        titleSwoop()
        start, opt, quit, credits = menuButtons()
        size += 1
        pygame.display.update()
        vars.clock.tick(frames)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                loc = pygame.mouse.get_pos()
                if start.get_rect().collidepoint(loc):
                    vars.gameState = 1
                    break
                if quit.get_rect().collidepoint(loc):
                    vars.running = False
                if opt.get_rect().collidepoint(loc):
                    vars.gameState = 2
                    print(vars.gameState)
                    break
                if credits.get_rect().collidepoint(loc):
                    vars.gameState = 3
                    break
            if event.type == pygame.QUIT:
                vars.running = False
