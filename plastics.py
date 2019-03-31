import pygame
from math import *
import random
from assets import *
from global_vars import *

class Plastic(pygame.sprite.Sprite):
    def __init__(self, plasticType):
        super().__init__()
        self.image = plasticType
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(300, WIDTH-300)
        self.rect.y = random.randrange(1100, 1600)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(2, 12)
        directions = [-1, 1]
        self.direction = random.choice(directions)
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        global PLASTICS_MISSED
        self.rect.y -= self.speedy
        if self.direction == -1:
            self.rect.x -= self.speedx
        elif self.direction == 1:
            self.rect.x += self.speedx
        if self.rect.bottom < 0:
            PLASTICS_MISSED += 1
            self.kill()
        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.kill()
    def changeDirection(self):
        self.direction = -self.direction


