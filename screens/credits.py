import vars
import pygame

pygame.init()

screen = vars.screen
pygame.display.set_caption("Credits")

image1 = pygame.image.load('Code-by-James-and-Virgil.png')
image2 = pygame.image.load('Graphics-by-Virgil.png')
image3 = pygame.image.load('Text-from-textcraft.png')
image4 = pygame.image.load('created-with-pygame.png')

image1_scaled = pygame.transform.scale(image1, (400, 300))  
image2_scaled = pygame.transform.scale(image2, (300, 225))
image3_scaled = pygame.transform.scale(image3, (200, 150))
image4_scaled = pygame.transform.scale(image4, (200, 150))  

image1_rect = image1_scaled.get_rect()
image1_rect.center = (vars.screen[0] // 2, vars.screen[1] // 4)
image2_rect = image2_scaled.get_rect()
image2_rect.center = (vars.screen[0] // 2, vars.screen[1] // 4 + 150)
image3_rect = image3_scaled.get_rect()
image3_rect.center = (vars.screen[0] // 2, vars.screen[1] // 4 + 300)
image4_rect = image4_scaled.get_rect()
image4_rect.center = (vars.screen[0] // 2, vars.screen[1] // 4 + 450)

def credits():
    screen.fill((0, 0, 255))
    screen.blit(image1_scaled, image1_rect)
    screen.blit(image2_scaled, image2_rect)
    screen.blit(image3_scaled, image3_rect)
    screen.blit(image4_scaled, image4_rect)











  
