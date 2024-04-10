import pygame
import vars
pygame.init()

screen = vars.screen
universalGravity = 0.45
maxBounce = 0.6

class DoPhysics:
    def __init__(self, image, size_x, size_y, cur_x, cur_y, bounce, sticky, id):
        self.image = image
        self.size_x = size_x
        self.size_y = size_y
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.bounce = bounce
        self.sticky = sticky
        self.vel_x = 0
        self.vel_y = 0
        self.id = id
        self.rect = pygame.rect

    def load(self, image):
        self.image = pygame.image.load(f'assets/{image}.png')
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))

    def spawn(self):
        self.rect = self.image.get_rect()
        self.size_x = self.image.get_width() / 2
        self.size_y = self.image.get_height() / 2
        self.rect.x = self.cur_x - self.size_x
        self.rect.y = self.cur_y - self.size_y
        pygame.draw.rect(vars.screen, '#000000', self.rect, 1, 0)
        vars.screen.blit(self.image, (self.cur_x - self.size_x, self.cur_y - self.size_y))

    def getCollisions(self):
        if self.cur_y < 700 - self.size_y: # lower bound including bounces
            self.vel_y += universalGravity
        elif self.vel_y > maxBounce:
            self.vel_y = -self.vel_y * self.bounce
        elif abs(self.vel_y) <= maxBounce:
            self.vel_y = 0
        if self.cur_y < 100 + self.size_y: # upper bound
            self.cur_y = self.cur_y + 5
            self.vel_y = -self.vel_y
        if self.cur_x < self.size_x + 200 and self.vel_x < 0: # left bound
            self.vel_x = 0
        if self.cur_x > 800 - self.size_x and self.vel_x > 0: # right bound
            self.vel_x = 0

        if self.rect.collidelist(vars.obstacles) >= 0: # object collision detection
            item = self.rect.collidelist(vars.obstacles)
            obs = vars.obstacles[item]
            if obs.cur_y <= self.cur_y - self.size_y: # invert vertical based on location
                self.vel_y = abs(self.vel_y) * self.bounce
                self.cur_y += 5
            if obs.cur_y >= self.cur_y + self.size_y:
                self.vel_y = -abs(self.vel_y) * self.bounce
            if obs.cur_x <= self.cur_x - self.size_x and not (obs.cur_y >= self.cur_y + self.size_y): # invert horizontal based on location
                self.vel_x = abs(self.vel_x) * self.sticky - obs.vel_x
            if obs.cur_x >= self.cur_x + self.size_x and not (obs.cur_y >= self.cur_y + self.size_y):
                self.vel_x = -abs(self.vel_x) * self.sticky + obs.vel_x

        if self.vel_x != 0 or self.rect.collidelist(vars.obstacles) >= 0: # friction
            if self.cur_y >= 650:
                self.vel_x *= self.sticky
            else:
                self.vel_x *= 0.98 # air friction

        return self.vel_y, self.vel_x

    def doJump(self):
        if self.cur_y >= 700 - self.size_y or self.rect.collidelist(vars.obstacles) >= 0:
            self.vel_y = -17.5

    def move(self, dir):
        if self.vel_x < vars.maxSpeed:
            self.vel_x += dir

    def updateVel(self):
        self.cur_x += self.vel_x
        self.cur_y += self.vel_y
