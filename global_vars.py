import pygame

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
BRIGHTRED = (255, 0, 0)
DARKRED = (200, 0, 0)
OCEANBLUE = (51, 153, 255)
DARKGOGREEN = (0, 153, 76)
BRIGHTGOGREEN = (0, 204, 102)
GREY = (240, 240, 240)

# Global Constants
WIDTH = 900
HEIGHT = 900
FPS = 60
INITIAL_SCORE = 0
INITIAL_DEPTH = 0
INITIAL_PLASTICS = 0
INITIAL_JELLYID = 0
INITIAL_HEALTH = 320
INITIAL_RED = 0
INITIAL_GREEN = 255
INITIAL_PLASTICS_MISSED = 0
INITIAL_JELLY_TYPE = 0
INITIAL_JELLY_KILLED = 0
DEPTHRATE = 0.03
USERDEPTHRATE = 0.01
REGENERATE = 0.09
JELLY_DAMAGE = 40
GREY_ROCKS_DAMAGE = 2
BLACK_ROCKS_DAMAGE = 0.1
MARGIN_LR = 20
MARGIN_TB = 30
PLAYER_MARGINS = [-MARGIN_LR, MARGIN_TB, WIDTH+MARGIN_LR, HEIGHT+MARGIN_TB]        # left, top, right, bottom
BUBBLE_LIMIT = 3
PLAYER_MOVE_TIME = 50
JELLY_KILL_TIME = 50
TUTORIAL_DEPTH = 25
JELLY_CHANGE_INTERVAL = 5

# Global Variable
SCORE = INITIAL_SCORE
DEPTH = INITIAL_DEPTH
PLASTICS = INITIAL_PLASTICS
PLASTICS_MISSED = INITIAL_PLASTICS_MISSED
JELLYID = INITIAL_JELLYID
HEALTH = INITIAL_HEALTH
RED = INITIAL_RED
GREEN = INITIAL_GREEN
JELLY_TYPE = INITIAL_JELLY_TYPE
JELLY_KILLED = INITIAL_JELLY_KILLED

all_sprites_list = pygame.sprite.Group()                # All Sprites Group
jellyFishGroup = pygame.sprite.Group()                  # JellyFish Group
BubbleGroup = pygame.sprite.Group()                     # Bubble Group
RocksGroup = pygame.sprite.Group()                      # Rocks Group
greyRocksGroup = pygame.sprite.Group()                  # Grey Rocks Group
blackRocksGroup = pygame.sprite.Group()                 # Black Rocks Group
plasticsGroup = pygame.sprite.Group()
