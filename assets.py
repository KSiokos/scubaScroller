import pygame
from global_vars import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))       # Creates screen with given width & height
pygame.display.set_caption("Scuba Scroller")            # Title of new window/screen

# -- Assets
backround = pygame.image.load("assets/background.png").convert_alpha()
bubble = pygame.image.load("assets/bubble.png").convert_alpha()

# Player
playerSinkingLeft = pygame.image.load("assets/player/playerSinkingLeft.png").convert_alpha()
playerSinkingRight = pygame.image.load("assets/player/playerSinkingRight.png").convert_alpha()
playerLeft = pygame.image.load("assets/player/playerLeft.png").convert_alpha()
playerRight = pygame.image.load("assets/player/playerRight.png").convert_alpha()
playerShootRight = pygame.image.load("assets/player/playerSinkingRight.png").convert_alpha()
playerShootLeft = pygame.image.load("assets/player/playerSinkingLeft.png").convert_alpha()
playerShootTop = pygame.image.load("assets/player/playerSinkingLeft.png").convert_alpha()
playerShootBottom = pygame.image.load("assets/player/playerSinkingLeft.png").convert_alpha()
# Jelly Fish Images
jellyFishRed = pygame.image.load("assets/jellyFish/red.png").convert_alpha()
jellyFishRedMove = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()
jellyFishRedInBubble = pygame.image.load("assets/jellyFish/red.png").convert_alpha()
jellyFishRedMoveInBubble = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()

jellyFishBlue = pygame.image.load("assets/jellyFish/blue.png").convert_alpha()
jellyFishBlueMove = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()
jellyFishBlueInBubble = pygame.image.load("assets/jellyFish/blue.png").convert_alpha()
jellyFishBlueMoveInBubble = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()

jellyFishGreen = pygame.image.load("assets/jellyFish/green.png").convert_alpha()
jellyFishGreenMove = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()
jellyFishGreenInBubble = pygame.image.load("assets/jellyFish/green.png").convert_alpha()
jellyFishGreenMoveInBubble = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()

jellyFishPurple = pygame.image.load("assets/jellyFish/purple.png").convert_alpha()
jellyFishPurpleMove = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()
jellyFishPurpleInBubble = pygame.image.load("assets/jellyFish/purple.png").convert_alpha()
jellyFishPurpleMoveInBubble = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()

jellyFishBrown = pygame.image.load("assets/jellyFish/brown.png").convert_alpha()
jellyFishBrownMove = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()
jellyFishBrownInBubble = pygame.image.load("assets/jellyFish/brown.png").convert_alpha()
jellyFishBrownMoveInBubble = pygame.image.load("assets/jellyFish/red-move.png").convert_alpha()

# Plastics
bottle = pygame.image.load("assets/plastics/bottle.png").convert_alpha()
bag = pygame.image.load("assets/plastics/bottle.png").convert_alpha()

# Rocks
blackrocks1 = pygame.image.load("assets/blackRocks/blackRocks1.png").convert_alpha()
blackrocks2 = pygame.image.load("assets/blackRocks/blackRocks2.png").convert_alpha()
blackrocks3 = pygame.image.load("assets/blackRocks/blackRocks3.png").convert_alpha()
blackrocks4 = pygame.image.load("assets/blackRocks/blackRocks4.png").convert_alpha()
greyrocks1 = pygame.image.load("assets/greyRocks/greyRocks1.png").convert_alpha()
greyrocks2 = pygame.image.load("assets/greyRocks/greyRocks2.png").convert_alpha()
greyrocks3 = pygame.image.load("assets/greyRocks/greyRocks3.png").convert_alpha()
greyrocks4 = pygame.image.load("assets/greyRocks/greyRocks4.png").convert_alpha()
