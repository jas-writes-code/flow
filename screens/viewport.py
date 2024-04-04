import pygame
import vars
pygame.init()

dynBG = []  # moves the semi-transparent boxes that overlay the reactive background
bgBox = pygame.image.load('assets/background.png')
scoreTitle = pygame.image.load('assets/score.png')
scoreNums = []
for i in range(0, 10):
    scoreNums.append(pygame.image.load(f'assets/numbers/{i}.png'))
box = pygame.transform.scale(bgBox, (100, 100))
BGSPEED = vars.speed * 0.8

# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
# boxes are 100x100, top 1 and bottom 2 rows are excluded
# top rect 1600x100, bottom rect 1600x200
# thick line for collisions on bottom rect

def boxLoop():
    global BGSPEED
    if vars.gameScore == 0:
        for i in range(0, 1600, 100):
            for j in range(100, 700, 100):
                vars.screen.blit(box, (i, j))
                dynBG.append([box, i, j])
        vars.gameScore += 1  # comment this out if you don't want the boxes to move
    if vars.gameScore != 0:
        to_remove = []
        for element in dynBG:
            element[1] -= BGSPEED  # Move the box to the left based on BGSPEED
            if element[1] < -100:  # Remove if completely off-screen
                to_remove.append(element)
        for element in to_remove:
            dynBG.remove(element)
        for moveBox in dynBG:
            vars.screen.blit(box, (moveBox[1], moveBox[2]))

        # Check if it's time to spawn new boxes
        if dynBG and dynBG[-1][1] <= 1500:  # Check if the rightmost box is almost off-screen
            for j in range(100, 700, 100):
                vars.screen.blit(box, (1600, j))
                dynBG.append([box, 1600, j])

def showScore(): # shows the score at the top of the screen
    ones = int(vars.gameScore % 10)
    tens = int((vars.gameScore % 100 - ones) / 10)
    huns = int((vars.gameScore % 1000 - tens) / 100)
    thous = int((vars.gameScore % 10000 - huns) / 1000)

    vars.screen.blit(scoreTitle, (775 - 415, 11))

    if vars.gameScore >= 10:
        vars.screen.blit(scoreNums[huns], (825, 11))
        vars.screen.blit(scoreNums[tens], (825 + scoreNums[huns].get_width() + 5, 11))
        vars.screen.blit(scoreNums[ones], (825 + scoreNums[huns].get_width() + scoreNums[tens].get_width() + 5, 11))

def lowerSec():
    pass # draws the lower section

def paint():
    vars.screen.fill(vars.dynamicColour)
    boxLoop()
    showScore()
    pygame.display.update()
