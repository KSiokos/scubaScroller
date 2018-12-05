import pygame
from math import *
import random
from assets import *
from global_vars import *
from jelly import *
from plastics import *

def make_new_jelly(number, type):
    for i in range(number):
        JB = Jelly(type)
        all_sprites_list.add(JB)
        jellyFishGroup.add(JB)

def make_new_plastic(number):
    plasticChoices = [bottle, bag]
    plasticType = random.choice(plasticChoices)
    for i in range(number):
        P = Plastic(plasticType)
        all_sprites_list.add(P)
        plasticsGroup.add(P)

def button(x, y, width, height, inactivecolour, activecolour):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, activecolour, (x, y, width, height))
        if click[0] == 1:
            return True
        else:
            return False
    else:
        pygame.draw.rect(screen, inactivecolour, (x, y, width, height))

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

def damage(cause):
    global HEALTH, RED, GREEN
    damage = 0
    if cause == "blackRocks":
        if HEALTH > BLACK_ROCKS_DAMAGE:
            damage = BLACK_ROCKS_DAMAGE
        else:
            damage = HEALTH
    elif cause == "greyRocks":
        if HEALTH > GREY_ROCKS_DAMAGE:
            damage = GREY_ROCKS_DAMAGE
        else:
            damage = HEALTH
    elif cause == "jelly":
        if HEALTH > JELLY_DAMAGE:
            damage = JELLY_DAMAGE
        else:
            damage = HEALTH
    HEALTH -= damage
    greenDecrease = damage/1.25
    redIncrease = 255 - greenDecrease
    if GREEN >= greenDecrease:
        GREEN -= greenDecrease
    if RED <= redIncrease:
        RED += greenDecrease

def regenrateHealth():
    global HEALTH, RED, GREEN
    if HEALTH < 320:
        HEALTH += REGENERATE
    if GREEN < 255:
        GREEN += REGENERATE
    if RED > 0:
        RED -= REGENERATE

def cleanSlate():
    global DEPTH, PLASTICS, JELLYID, HEALTH, RED, GREEN
    
    # Kill all sprites
    for each in all_sprites_list.sprites():
        each.kill()
    # Reset all global variables
    DEPTH = INITIAL_DEPTH
    PLASTICS = INITIAL_PLASTICS
    JELLYID = INITIAL_JELLYID
    HEALTH = INITIAL_HEALTH
    RED = INITIAL_RED
    GREEN = INITIAL_GREEN

# def addText(font, size, location, text):