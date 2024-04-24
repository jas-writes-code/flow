import pygame
import vars
pygame.init()

dynBG = []  # moves the semi-transparent boxes that overlay the reactive background
bgBox = pygame.image.load('assets/background.png')
scoreTitle = pygame.image.load('assets/score.png')
banner = pygame.image.load('assets/banner.png')
scoreNums = []
for i in range(0, 10):
    scoreNums.append(pygame.image.load(f'assets/numbers/{i}.png'))
box = pygame.transform.scale(bgBox, (100, 100))
banner = pygame.transform.scale(banner, (1600, 200))
BGSPEED = 0

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
        vars.speed += 1
    if vars.gameScore != 0:
        to_remove = []
        for element in dynBG:
            element[1] -= BGSPEED  # shift the boxes to the left
            if element[1] < -100:  # despawn them if they're off screen
                to_remove.append(element)
        for element in to_remove:
            dynBG.remove(element)
        for moveBox in dynBG:
            vars.screen.blit(box, (moveBox[1], moveBox[2]))

        # Check if it's time to spawn new boxes
        if dynBG and dynBG[-1][1] <= 1500:  # is the newest box fully visible?
            for j in range(100, 700, 100):
                vars.screen.blit(box, (1600, j))
                dynBG.append([box, 1600, j])

def showScore(): # shows the score at the top of the screen
    ones = int(vars.gameScore % 10)
    tens = int((vars.gameScore % 100 - ones) / 10)
    huns = int((vars.gameScore % 1000 - tens) / 100)
    thous = int((vars.gameScore % 10000 - huns) / 1000)

    vars.screen.blit(scoreTitle, (775 - 415, 11))

    if vars.gameScore <= 1000:
        vars.screen.blit(scoreNums[thous], (825, 11))
        vars.screen.blit(scoreNums[huns], (825 + scoreNums[thous].get_width(), 11))
        vars.screen.blit(scoreNums[tens], (825 + scoreNums[thous].get_width() + scoreNums[huns].get_width(), 11))
        vars.screen.blit(scoreNums[ones], (825 + scoreNums[thous].get_width() + scoreNums[huns].get_width() + scoreNums[tens].get_width(), 11))
    else:
        dist = 0
        for digit in str(vars.gameScore):
            vars.screen.blit(scoreNums[int(digit)], ((825 + dist), 11))
            dist += scoreNums[int(digit)].get_width()

def padding():
    inverted = []
    for element in vars.dynamicColour:
        inverted.append(255 - element)
    pygame.draw.line(vars.screen, inverted, (0, 700), (1600, 700), 5)
    vars.screen.blit(banner, (0, 700))

def paint():
    vars.screen.fill(vars.dynamicColour)
    boxLoop()
    padding()
    showScore()
