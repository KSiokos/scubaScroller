import pygame
import random
import math
import time
# from helpers import *

# -- Global Constants

WIDTH = 900
HEIGHT = 900
FPS = 60
DEPTHRATE = 0.03
USERDEPTHRATE = 0.01
DONE = False

# -- Global Variable
PAUSE = False
ANTIDOTES = 3
DEPTH = 0
PLASTICS = 0
BUBBLE_LIMIT = 3
test_countdown = 50
JELLY_KILL_TIME = 50
JELLYID = 0

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

# Health Bar
# hb1 = pygame.image.load("assets/healthBar/hb1.png").convert_alpha()
# .
# .
# .
# healthBar = [hb1, hb2, hb3, hb4, ...]



# Plastics
bottle = pygame.image.load("assets/plastics/bottle.png").convert_alpha()

# Rocks
blackrocks1 = pygame.image.load("assets/blackRocks/blackRocks1.png").convert_alpha()
blackrocks2 = pygame.image.load("assets/blackRocks/blackRocks2.png").convert_alpha()
blackrocks3 = pygame.image.load("assets/blackRocks/blackRocks3.png").convert_alpha()
blackrocks4 = pygame.image.load("assets/blackRocks/blackRocks4.png").convert_alpha()
greyrocks1 = pygame.image.load("assets/greyRocks/greyRocks1.png").convert_alpha()
greyrocks2 = pygame.image.load("assets/greyRocks/greyRocks2.png").convert_alpha()
greyrocks3 = pygame.image.load("assets/greyRocks/greyRocks3.png").convert_alpha()
greyrocks4 = pygame.image.load("assets/greyRocks/greyRocks4.png").convert_alpha()


# -- Functions
def make_new_jelly(number):
    for i in range(number):
        JB = Jelly()
        all_sprites_list.add(JB)
        jellyFishGroup.add(JB)

def make_new_plastic(number, plasticType):
    for i in range(number):
        P = Plastic(plasticType)
        all_sprites_list.add(P)
        plasticsGroup.add(P)

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

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
# -- 

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


# -- Class Definitions

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
    def shootRight(self):
        oldState = self.image
        self.image = playerShootRight
        self.mask = pygame.mask.from_surface(self.image)
        countdown = test_countdown
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootLeft(self):
        oldState = self.image
        self.image = playerShootLeft
        self.mask = pygame.mask.from_surface(self.image)
        countdown = test_countdown
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootTop(self):
        oldState = self.image
        self.image = playerShootTop
        self.mask = pygame.mask.from_surface(self.image)
        countdown = test_countdown
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def shootBottom(self):
        oldState = self.image
        self.image = playerShootBottom
        self.mask = pygame.mask.from_surface(self.image)
        countdown = test_countdown
        while countdown > 0:
            countdown -= 1
        self.image = oldState
        self.mask = pygame.mask.from_surface(self.image)
    def getPos(self):
        return [self.rect.x, self.rect.y]

# -- JellyFish Class
class Jelly(pygame.sprite.Sprite):
    def __init__(self):
        global JELLYID
        super().__init__() 
        JELLYID += 1
        self.id = JELLYID
        self.image = pygame.Surface([128, 128])
        self.jellyColours = [jellyFishRed, jellyFishBlue, jellyFishGreen, jellyFishPurple, jellyFishBrown]
        self.jellyColoursMove = [jellyFishRedMove, jellyFishBlueMove, jellyFishGreenMove, jellyFishPurpleMove, jellyFishBrownMove]
        self.jellyColoursInBubble = [jellyFishRedInBubble, jellyFishBlueInBubble, jellyFishGreenInBubble, jellyFishPurpleInBubble, jellyFishBrownMoveInBubble]
        self.jellyColoursMoveInBubble = [jellyFishRedMoveInBubble, jellyFishBlueMoveInBubble, jellyFishGreenMoveInBubble, jellyFishPurpleMoveInBubble, jellyFishBrownMoveInBubble]
        self.jellyType = 0
        self.refresh = 40
        self.movement = self.refresh
        self.image = self.jellyColours[self.jellyType]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(1400, 1550)
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

# -- Plastics Class
class Plastic(pygame.sprite.Sprite):
    def __init__(self, plasticType):
        super().__init__()
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

# -- Bubble Class
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

# -- Groups
all_sprites_list = pygame.sprite.Group()                # All Sprites Group
jellyFishGroup = pygame.sprite.Group()                  # JellyFish Group
plasticsGroup = pygame.sprite.Group()                   # Plastics Group
RocksGroup = pygame.sprite.Group()                      # Rocks Group
BubbleGroup = pygame.sprite.Group()                     # Bubble Group

# -- Objects
player = Player()                                       # Player Object
make_new_plastic(1, bottle)                             # Plastic Objects
greyRocksSegment1 = greyRocks(greyrocks1, 0)            # GreyRocks Objects
greyRocksSegment2 = greyRocks(greyrocks2, 300)
greyRocksSegment3 = greyRocks(greyrocks3, 600)
greyRocksSegment4 = greyRocks(greyrocks4, 900)
blackRocksSegment1 = blackRocks(blackrocks1, 0)         # BlackRocks Objects
blackRocksSegment2 = blackRocks(blackrocks2, 300)
blackRocksSegment3 = blackRocks(blackrocks3, 600)
blackRocksSegment4 = blackRocks(blackrocks4, 900)

all_sprites_list.add(player)                            # Player added to Group
RocksGroup.add(blackRocksSegment1)                      # Rocks added to Group
RocksGroup.add(blackRocksSegment2)
RocksGroup.add(blackRocksSegment3)
RocksGroup.add(blackRocksSegment4)
RocksGroup.add(greyRocksSegment1)
RocksGroup.add(greyRocksSegment2)
RocksGroup.add(greyRocksSegment3)
RocksGroup.add(greyRocksSegment4)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

def game_loop():
    # - Global Variables
    global DONE, PAUSE, ANTIDOTES, DEPTH, PLASTICS
    clock.tick(FPS)                                                     # The clock ticks over

    # -- Exit game flag set to false
    # DONE = False

    while not DONE and not PAUSE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True
                quitgame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    DONE = True
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

        # -- Draw and Update All Sprites
        all_sprites_list.draw(screen)
        all_sprites_list.update()

        # - Player Controls
        keys = pygame.key.get_pressed()
        # Movement
        if keys[pygame.K_a]:
            player.MoveLeft(4)
        if keys[pygame.K_d]:
            player.MoveRight(4)
        if keys[pygame.K_w]:
            player.MoveUp(4)
            DEPTH -= USERDEPTHRATE
        if keys[pygame.K_s]:
            player.MoveDown(4)
            DEPTH += USERDEPTHRATE
        # Shooting
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, 1, 0)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootRight()
                elif event.key == pygame.K_LEFT:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, -1, 0)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootLeft()
                elif event.key == pygame.K_UP:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, 0, -1)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootTop()
                elif event.key == pygame.K_DOWN:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, 0, 1)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootBottom()

        # - Game over requirements
        if ANTIDOTES <= 0:
            DONE = True
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

        # -- Collisions

        # Player and Plastics Collision
        collects = pygame.sprite.spritecollide(player, plasticsGroup, True, pygame.sprite.collide_mask)
        for collect in collects:
            make_new_plastic(1, bottle)
            PLASTICS = PLASTICS + 1
            
        # Player and JellyFish Collision 
        playerJellyCollision = pygame.sprite.spritecollide(player, jellyFishGroup, False, pygame.sprite.collide_mask)
        for jelly in playerJellyCollision:
            if jelly.getBubble():
                jelly.kill()
            else:
                jellyFishGroup.remove(jelly)
                ANTIDOTES = ANTIDOTES - 1


        # Bubble and JellyFish Collision
        bubbleJellyCollision = pygame.sprite.groupcollide(BubbleGroup, jellyFishGroup, True, False)
        for everyBubble in bubbleJellyCollision:
            # x = bubbleJellyCollision.values()
            # y = list(x)
            # z = y[0]
            # ans = z.pop()
            jellyFishBubbled = list(bubbleJellyCollision.values())[0].pop()
            if not jellyFishBubbled.getBubble():
                jellyFishBubbled.setBubble()
        
        # Keep 6 JellyFish alive at all times
        if len(jellyFishGroup) <= 6:
            difference = 6 - len(jellyFishGroup)
            make_new_jelly(difference)

        # - Depth increases as clock ticks
        DEPTH += DEPTHRATE

        # -- flip display to reveal new position of objects
        pygame.display.flip()


game_intro()
game_loop()
