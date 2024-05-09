import vars
import pygame
from screens import viewport
pygame.init()

gameOver = pygame.image.load('assets/gameover.png')
gameOver = pygame.transform.scale(gameOver, (948, 123))
finalScore = pygame.image.load('assets/urscore.png')
highscores = pygame.image.load('assets/pasthighscores.png')
highscores = pygame.transform.scale(highscores, (500, 45))
quit = pygame.image.load('assets/quitgame.png')
quit = pygame.transform.scale(quit, (314, 58))
menu = pygame.image.load('assets/mainmenu.png')
menu = pygame.transform.scale(menu, (338, 47))
count = -1

def postgame():
    global count
    if count < 0:
        fade_surface = pygame.Surface((1600, 900))
        fade_surface.fill((0, 0, 0))  # Fill with black color
        for alpha in range(0, 255, 5):
            fade_surface.set_alpha(alpha)
            vars.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(30)
        for i in range(0, 255):
            gameOver.set_alpha(i)
            finalScore.set_alpha(i)
            vars.screen.blit(gameOver, (800 - 948 / 2, 50))
            vars.screen.blit(finalScore, (800 - 755 / 2, 200))
        count += 1
    elif count == 0:
        vars.screen.blit(gameOver, (800 - 948 / 2, 50))
        vars.screen.blit(finalScore, (800 - 755 / 2, 200))
        viewport.postgame()
        vars.screen.blit(menu, (1200 - 338 / 2, 400))
        vars.screen.blit(quit, (1200 - 314 / 2, 475))
        vars.screen.blit(highscores, (400 - 500 / 2, 400))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            loc = pygame.mouse.get_pos()
            if 1200 - 338 / 2 < loc[0] < 1200 + 338 / 2 and 400 < loc[1] < 447:
                    vars.titleSize = 0
                    vars.gameState = 0 # main menu button
            if 1200 - 314 / 2 < loc[0] < 1200 + 314 / 2 and 475 < loc[1] < 475 + 58:
                    vars.gameState = -1 # quit button
        if event.type == pygame.QUIT:
            vars.gameState = -1
