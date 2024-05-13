import pygame
import vars

pygame.init()
screen = vars.screen

load = ["code", "graphics", "text", "created", "supervised", "schwaninger", "audio", "pyaudio", "withthanksto", "nobody"]
loaded = []
menu = pygame.image.load('assets/mainmenu.png')
menu = pygame.transform.scale(menu, (menu.get_width() / 1.5, menu.get_height() / 1.25))
for element in load:
    loaded.append(pygame.image.load(f'assets/credits/{element}.png'))
    loaded[-1] = pygame.transform.scale(loaded[-1], (loaded[-1].get_width() / 1.25, loaded[-1].get_height() / 1.25))  # Correctly scaling images

def credits():
    screen.fill((0, 0, 60))
    gap = 50
    for element in loaded:
        screen.blit(element, (800 - element.get_width() / 2, gap))  # Blitting each image onto the screen
        gap += element.get_height() + 10  # Adding some gap between images
    screen.blit(menu, (800 - menu.get_width() / 2, gap))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            loc = pygame.mouse.get_pos()
            if 800 - menu.get_width() / 2 < loc[0] < 800 + menu.get_width() / 2 and gap < loc[1] < menu.get_height() + gap:
                vars.titleSize = 0
                vars.clearstate()
                vars.gameState = 0 # main menu button
        if event.type == pygame.QUIT:
            vars.gameState = -1
