import pygame
import random
import math
import time

# -- Global Constants

WIDTH = 900
HEIGHT = 900
FPS = 60

# -- Global Variable
PAUSE = False
ANTIDOTES = 3
DEPTH = 0
PLASTICS = 0

# -- Colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
BRIGHTRED = (255, 0, 0)
DARKRED = (200, 0, 0)
OCEANBLUE = (51, 153, 255)
DARKGOGREEN = (0, 153, 76)
BRIGHTGOGREEN = (0, 204, 102)

# -- Initialise Pygame

pygame.init()                                           # Initialises pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))       # Creates screen with given width & height
pygame.display.set_caption("Scuba Scroller")            # Title of new window/screen

# -- Assets
backround = pygame.image.load("assets/background.png").convert_alpha()
playerSinkingLeft = pygame.image.load("assets/player/playerSinkingLeft.png").convert_alpha()
playerSinkingRight = pygame.image.load("assets/player/playerSinkingRight.png").convert_alpha()
playerLeft = pygame.image.load("assets/player/playerLeft.png").convert_alpha()
playerRight = pygame.image.load("assets/player/playerRight.png").convert_alpha()
jellyFishRed = pygame.image.load("assets/jellyFish/red.png").convert_alpha()
bottle = pygame.image.load("assets/plastics/bottle.png").convert_alpha()
blackrocks1 = pygame.image.load("assets/blackRocks/blackRocks1.png").convert_alpha()
blackrocks2 = pygame.image.load("assets/blackRocks/blackRocks2.png").convert_alpha()
blackrocks3 = pygame.image.load("assets/blackRocks/blackRocks3.png").convert_alpha()
blackrocks4 = pygame.image.load("assets/blackRocks/blackRocks4.png").convert_alpha()
greyrocks1 = pygame.image.load("assets/greyRocks/greyRocks1.png").convert_alpha()
greyrocks2 = pygame.image.load("assets/greyRocks/greyRocks2.png").convert_alpha()
greyrocks3 = pygame.image.load("assets/greyRocks/greyRocks3.png").convert_alpha()
greyrocks4 = pygame.image.load("assets/greyRocks/greyRocks4.png").convert_alpha()


# -- Functions

# -- 
def quitgame():
    pygame.quit()

# --
def game_over():
    screen.fill(BLACK)
    screen.blit(backround, (0,0))
    
    # Create function for fonts usage throughout the code

    text = pygame.font.SysFont('bubblegums', 50, True, False).render("GAME OVER",True,WHITE)
    screen.blit(text, [220,400])
    text1 = pygame.font.SysFont('bubblegums', 20, True, False).render("You reached " + '%0.0f'%DEPTH + "m",True,WHITE)
    screen.blit(text1, [305,470])
    text1 = pygame.font.SysFont('bubblegums', 20, True, False).render("You cleaned up " + str(PLASTICS) + ' bottles',True,WHITE)
    screen.blit(text1, [230,505])
    pygame.display.flip()
    time.sleep(3)
    quitgame()

def button( x, y, width, height, inactivecolour, activecolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(screen, activecolour, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, inactivecolour, (x,y,width,height))

def unpause():
    global PAUSE
    PAUSE = False

def paused():

    while PAUSE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        text = pygame.font.SysFont('bubblegums', 45, True, False).render("Paused",True,WHITE)
        screen.blit(text, [325,400])

        button( 275, 500, 160, 50, DARKGOGREEN, BRIGHTGOGREEN,unpause)
        button( 535, 500, 100, 50, DARKRED, BRIGHTRED,quitgame)

        text1 = pygame.font.SysFont('bubblegums', 24, True, False).render("Resume",True,WHITE)
        screen.blit(text1, [278, 510])

        text2 = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit",True,WHITE)
        screen.blit(text2, [540, 510])

        pygame.display.flip()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(backround, (0,0))
        text = pygame.font.SysFont('bubblegums', 45, True, False).render("Scuba Scroller", True, WHITE)
        screen.blit(text, [170,400])

        button(275, 500, 100, 50, DARKGOGREEN, BRIGHTGOGREEN, game_loop)
        button(535, 500, 100, 50, DARKRED, BRIGHTRED, quitgame)

        playButton = pygame.font.SysFont('bubblegums', 24, True, False).render("Play", True,WHITE)
        screen.blit(playButton, [278, 510])

        text2 = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit", True, WHITE)
        screen.blit(text2, [540, 510])

        pygame.display.flip()

def make_new_jelly(number):
    for i in range(number):
        JB = JellyBasic()
        all_sprites_list.add(JB)
        jellyFishGroup.add(JB)

def make_new_plastic(number):
    for i in range(number):
        P = Plastic()
        all_sprites_list.add(P)
        plasticsGroup.add(P)

# -- Class Definition

# -- Player Class
class Player(pygame.sprite.Sprite):
    #Define the constructor for player
    def __init__(self):
        super().__init__()                                          # Call the sprite constructor
        self.image = pygame.Surface([128, 128])
        self.image = playerSinkingLeft                                 # Draw the player
        self.rect = self.image.get_rect()
        self.rect.x = 425
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

# -- Player Object
player = Player()

# -- JellyFish Class
class JellyBasic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([128, 128])
        self.image = jellyFishRed
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(1400, 1550)
        self.speedy = random.randrange(2, 5)
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < -10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(1000, 1100)
            self.speedy = random.randrange(2, 5)

# -- JellyFish Object
jelly = JellyBasic()

# -- JellyFish Group
jellyFishGroup = pygame.sprite.Group()


# -- Plastics Class
class Plastic(pygame.sprite.Sprite):
    def __init__(self, plasticType):
        super().__init__()
        self.image = pygame.Surface([25,70])
        self.image = plasticType
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(2500, 2600)
        self.speedy = random.randrange(2, 6)
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < -200:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(3000, 3100)
            self.speedy = random.randrange(2, 6)

# -- Plactics Object
bottle = Plastic(bottle)

# -- Plastics Group
plasticsGroup = pygame.sprite.Group()
plasticsGroup.add(bottle)

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
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom <= 0:
            self.rect.y = 900

# -- GreyRocks Objects
greyRocksSegment1 = greyRocks(greyrocks1, 0)
greyRocksSegment2 = greyRocks(greyrocks2, 300)
greyRocksSegment3 = greyRocks(greyrocks3, 600)
greyRocksSegment4 = greyRocks(greyrocks4, 900)

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

# -- BlackRocks Objects
blackRocksSegment1 = blackRocks(blackrocks1, 0)
blackRocksSegment2 = blackRocks(blackrocks2, 300)
blackRocksSegment3 = blackRocks(blackrocks3, 600)
blackRocksSegment4 = blackRocks(blackrocks4, 900)

# -- Rocks Group
RocksGroup = pygame.sprite.Group()
RocksGroup.add(blackRocksSegment1)
RocksGroup.add(blackRocksSegment2)
RocksGroup.add(blackRocksSegment3)
RocksGroup.add(blackRocksSegment4)
RocksGroup.add(greyRocksSegment1)
RocksGroup.add(greyRocksSegment2)
RocksGroup.add(greyRocksSegment3)
RocksGroup.add(greyRocksSegment4)

make_new_jelly(6)
make_new_plastic(1)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

def game_loop():
    # - Global Variables
    global PAUSE, ANTIDOTES, DEPTH, PLASTICS
    clock.tick(FPS)                                                     # The clock ticks over

    # -- Exit game flag set to false
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quitgame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    game_over()
                if event.key == pygame.K_p:
                    PAUSE = True
                    paused()
                    
        # -- Setup Background
        screen.blit(backround, (0,0))

        # -- Setup and move Rocks
        RocksGroup.draw(screen)
        RocksGroup.update()

        # - Information on screen (DEPTH, sting antidote etc)        
        font = pygame.font.SysFont('calibri', 16, True, False)
        text = font.render('Sting Antidote Left: ' + str(ANTIDOTES), True, WHITE)
        screen.blit(text, [50, 50])
        font = pygame.font.SysFont('AGENTORANGE', 55, True, False)
        depthText = font.render('%0.0f'%DEPTH + 'm', True, WHITE)
        blit_alpha(screen, depthText, (375,200), 128)
        font = pygame.font.SysFont('calibri', 16, True, False)
        text = font.render('Clean Up: ' + str(PLASTICS), True, WHITE)
        screen.blit(text, [50, 70])

        # - Player movements
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.MoveLeft(4)
        if keys[pygame.K_d]:
            player.MoveRight(4)
        if keys[pygame.K_w]:
            player.MoveUp(4)
        if keys[pygame.K_s]:
            player.MoveDown(4)

        # - Game over requirements
        if ANTIDOTES <= 0:
            done = True
            game_over()

        # - Player constraints
        if player.rect.right > WIDTH + 20:
            player.rect.right = WIDTH + 20
        if player.rect.left < -20:
            player.rect.left = -20
        if player.rect.bottom > HEIGHT + 30:
            player.rect.bottom = HEIGHT + 30
        if player.rect.top  < 30:
            player.rect.top = 30

        collects = pygame.sprite.spritecollide(player, plasticsGroup, True, pygame.sprite.collide_mask)
        for collect in collects:
            make_new_plastic(1)
            PLASTICS = PLASTICS + 1
            
        # - If player hits jellyfish make new one and remove hit one off screen
        hits = pygame.sprite.spritecollide(player, jellyFishGroup, True, pygame.sprite.collide_mask)
        for hit in hits:
            make_new_jelly(1)
            ANTIDOTES = ANTIDOTES - 1
            
        # - Depth increases as clock ticks
        DEPTH = DEPTH + 0.1

        # -- flip display to reveal new position of objects
        pygame.display.flip()


game_intro()
game_loop()
