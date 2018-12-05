import pygame
from math import *
import random
from assets import *
from global_vars import *

class Jelly(pygame.sprite.Sprite):
    def __init__(self, type):
        global JELLYID
        super().__init__() 
        JELLYID += 1
        self.id = JELLYID
        self.image = pygame.Surface([128, 128])
        self.jellyColours = [jellyFishRed, jellyFishBrown, jellyFishGreen, jellyFishBlue, jellyFishPurple]
        self.jellyColoursMove = [jellyFishRedMove, jellyFishBrownMove, jellyFishGreenMove, jellyFishBlueMove, jellyFishPurpleMove]
        self.jellyColoursInBubble = [jellyFishRedInBubble, jellyFishBrownMoveInBubble, jellyFishGreenInBubble, jellyFishBlueInBubble, jellyFishPurpleInBubble]
        self.jellyColoursMoveInBubble = [jellyFishRedMoveInBubble, jellyFishBrownMoveInBubble, jellyFishGreenMoveInBubble, jellyFishBlueMoveInBubble, jellyFishPurpleMoveInBubble]
        self.jellyType = type
        self.refresh = 40
        self.movement = self.refresh
        self.image = self.jellyColours[self.jellyType]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(1000, 1200)
        self.speedy = random.randrange(2, 5)
        self.mask = pygame.mask.from_surface(self.image)
        self.inBubble = False
        self.killTime = JELLY_KILL_TIME
    def update(self):
        if self.inBubble == True:
            self.killTime -= 1
            self.image = self.jellyColoursInBubble[self.jellyType]
            self.mask = pygame.mask.from_surface(self.image)
            self.movement -= 1
            if self.movement > (self.refresh/2):
                self.image = self.jellyColoursMoveInBubble[self.jellyType]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.jellyColoursInBubble[self.jellyType]
                self.mask = pygame.mask.from_surface(self.image)
            if self.movement == 0:
                self.movement = self.refresh
            self.rect.x += random.randrange(-1, 2)
            if self.killTime == 0:
                self.inBubble = False
                self.killTime = JELLY_KILL_TIME
        else:
            self.movement -= 1
            if self.movement > (self.refresh/2):
                self.image = self.jellyColoursMove[self.jellyType]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.jellyColours[self.jellyType]
                self.mask = pygame.mask.from_surface(self.image)
            if self.movement == 0:
                self.movement = self.refresh
            self.rect.y -= self.speedy
            self.rect.x += random.randrange(-1, 2)
        if self.rect.bottom < -10:
            self.kill()
    def setBubble(self):
        self.inBubble = True
    def getBubble(self):
        return self.inBubble
    def getID(self):
        return self.id

