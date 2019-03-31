import pygame
from math import *
import random
from assets import *
from global_vars import *


class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y, directionX, directionY):
        super().__init__()
        self.image = bubble
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.directionX = directionX
        self.directionY = directionY
    def update(self):
        if (self.rect.x > WIDTH) or (self.rect.x < 0) or (self.rect.y < 0) or (self.rect.y > HEIGHT):
            self.kill()
        self.rect.x += self.directionX
        self.rect.y += self.directionY
        if self.directionX == 0:
            self.rect.x += random.randrange(-1, 2)
        if self.directionY == 0:
            self.rect.y += random.randrange(-1, 2)
