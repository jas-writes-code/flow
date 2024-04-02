import pygame
import vars
pygame.init()

dynBG = []  # moves the semi-transparent boxes that overlay the reactive background
# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

def paint():
    backgroundBox = pygame.draw.rect(vars.screen, '#ff0000', pygame.Rect(50, 30, 30, 90), 5, 6) # i want to change this later
    dynBG.append(backgroundBox)
    for shift in dynBG:
        shift.x -= vars.speed * 0.6
        if shift <= -80:
            dynBG.remove(shift)
    pygame.display.update()

