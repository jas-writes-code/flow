# see settings.json
import json

import pygame
import vars
pygame.init()

dragging = (False, False)
def drawSlider(x, y, action):
    dist = action * 6
    slidecolour = '#555555'
    thingcolour = '#94167f'
    slider = pygame.draw.rect(vars.screen, slidecolour, (x, y + 25, 600, 50))
    thing = pygame.draw.rect(vars.screen, thingcolour, (x + dist - 50, y, 100, 100))
    return thing

def drawToggle(x, y, action):
    colour = '#00ff00'
    if action == False:
        colour = '#ff0000'
    rect = pygame.draw.rect(vars.screen, colour, (x, y, 200, 100))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            loc = pygame.mouse.get_pos()
            if x < loc[0] < x + 200:
                if y < loc[1] < y + 100:
                    action = not action
    return rect

def options():
    global dragging
    vars.screen.fill('#000000')
    with open('settings.json', 'r') as file:
        data = json.load(file)

    fullscreen = drawToggle(550, 100, data['video']['fullscreen'])
    fps = drawToggle(1350, 100, data['video']['fps'])
    contrast = drawToggle(550, 250, data['video']['contrast'])
    amp = drawSlider(900, 250, data['video']['amp'])
    chaos = drawSlider(100, 500, data['gameplay']['chaos'])
    multiplier = drawSlider(900, 500, data['gameplay']['multiplier'])
    gravity = drawSlider(500, 750, data['gameplay']['gravity'])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click detected")
            if fullscreen.collidepoint(event.pos):
                data['video']['fullscreen'] = not data['video']['fullscreen']
                with open('settings.json', 'w') as file:
                    json.dump(data, file, indent=4)
            if fps.collidepoint(event.pos):
                print("click on fps detected")
                data['video']['fps'] = not data['video']['fps']
                with open('settings.json', 'w') as file:
                    json.dump(data, file, indent=4)
            if contrast.collidepoint(event.pos):
                data['video']['contrast'] = not data['video']['contrast']
                with open('settings.json', 'w') as file:
                    json.dump(data, file, indent=4)
            if amp.collidepoint(event.pos):
                dragging = (True, amp)
                mouse_x, mouse_y = event.pos
                offset_x = amp.x - mouse_x
            if chaos.collidepoint(event.pos):
                dragging = (True, chaos)
                mouse_x, mouse_y = event.pos
                offset_x = chaos.x - mouse_x
            if multiplier.collidepoint(event.pos):
                dragging = (True, multiplier)
                mouse_x, mouse_y = event.pos
                offset_x = multiplier.x - mouse_x
            if gravity.collidepoint(event.pos):
                dragging = (True, gravity)
                mouse_x, mouse_y = event.pos
                offset_x = gravity.x - mouse_x
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = (False, False)
        elif event.type == pygame.MOUSEMOTION:
            if dragging[0] and dragging[1].x < mouse_x < dragging[1].size[0]:
                mouse_x, mouse_y = event.pos
                dragging[1].x = mouse_x + offset_x
        if event.type == pygame.QUIT:
            vars.gameState = -1
