import pygame
from math import *
import random
from assets import *
from global_vars import *

class Player(pygame.sprite.Sprite):
    #Define the constructor for player
    def __init__(self):
        super().__init__()                                          # Call the sprite constructor
        self.image = pygame.Surface([128, 128])
        self.image = playerSinkingLeft                                 # Draw the player
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 100
    def MoveRight(self, pixels):
        self.rect.x += pixels
        self.image = playerSinkingRight
        self.mask = pygame.mask.from_surface(self.image)
    def MoveLeft(self, pixels):
        self.rect.x -= pixels
        self.image = playerSinkingLeft
        self.mask = pygame.mask.from_surface(self.image)
    def MoveUp(self, pixels):
        self.rect.y -= pixels
        self.image = playerLeft
        self.mask = pygame.mask.from_surface(self.image)
    def MoveDown(self, pixels):
        self.rect.y += pixels
        self.image = playerSinkingLeft
        self.mask = pygame.mask.from_surface(self.image)
    def shootRight(self):
        oldState = self.image
        self.image = playerShootRight
        self.mask = pygame.mask.from_surface(self.image)
        countdown = PLAYER_MOVE_TIME
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootLeft(self):
        oldState = self.image
        self.image = playerShootLeft
        self.mask = pygame.mask.from_surface(self.image)
        countdown = PLAYER_MOVE_TIME
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootTop(self):
        oldState = self.image
        self.image = playerShootTop
        self.mask = pygame.mask.from_surface(self.image)
        countdown = PLAYER_MOVE_TIME
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootBottom(self):
        oldState = self.image
        self.image = playerShootBottom
        self.mask = pygame.mask.from_surface(self.image)
        countdown = PLAYER_MOVE_TIME
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def getPos(self):
        return [self.rect.x, self.rect.y]
    def update(self):
        if self.rect.right > PLAYER_MARGINS[2]:
            self.rect.right = PLAYER_MARGINS[2]
        if self.rect.left < PLAYER_MARGINS[0]:
            self.rect.left = PLAYER_MARGINS[0]
        if self.rect.bottom > PLAYER_MARGINS[3]:
            self.rect.bottom = PLAYER_MARGINS[3]
        if self.rect.top  < PLAYER_MARGINS[1]:
            self.rect.top = PLAYER_MARGINS[1]
