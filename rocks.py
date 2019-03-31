import pygame
from math import *
import random
from assets import *
from global_vars import *

# -- GreyRocks Class
class greyRocks(pygame.sprite.Sprite):
    def __init__(self, image, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y
        self.speedy = 3
        self.originY = y
        self.mask = pygame.mask.from_surface(self.image, 127)
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom <= 0:
            self.rect.y = 900

# -- BlackRocks Class
class blackRocks(pygame.sprite.Sprite):
    def __init__(self, image, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y
        self.speedy = 1
        self.originY = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom <= 0:
            self.rect.y = 900

greyRocksSegment1 = greyRocks(greyrocks1, 0)            # GreyRocks Objects
greyRocksSegment2 = greyRocks(greyrocks2, 300)
greyRocksSegment3 = greyRocks(greyrocks3, 600)
greyRocksSegment4 = greyRocks(greyrocks4, 900)
blackRocksSegment1 = blackRocks(blackrocks1, 0)         # BlackRocks Objects
blackRocksSegment2 = blackRocks(blackrocks2, 300)
blackRocksSegment3 = blackRocks(blackrocks3, 600)
blackRocksSegment4 = blackRocks(blackrocks4, 900)

RocksGroup.add(blackRocksSegment1)                      # Rocks added to Group
RocksGroup.add(blackRocksSegment2)
RocksGroup.add(blackRocksSegment3)
RocksGroup.add(blackRocksSegment4)
RocksGroup.add(greyRocksSegment1)
RocksGroup.add(greyRocksSegment2)
RocksGroup.add(greyRocksSegment3)
RocksGroup.add(greyRocksSegment4)
greyRocksGroup.add(greyRocksSegment1)
greyRocksGroup.add(greyRocksSegment2)
greyRocksGroup.add(greyRocksSegment3)
greyRocksGroup.add(greyRocksSegment4)
blackRocksGroup.add(blackRocksSegment1)                      # Rocks added to Group
blackRocksGroup.add(blackRocksSegment2)
blackRocksGroup.add(blackRocksSegment3)
blackRocksGroup.add(blackRocksSegment4)
