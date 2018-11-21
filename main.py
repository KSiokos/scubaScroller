import pygame
import random
import math
import time

# -- Global Contants

WIDTH = 900
HEIGHT = 900
FPS = 40

# -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BRIGHTRED = (255, 0, 0)
DARKRED = (200, 0, 0)
OCEANBLUE = (51, 153, 255)
DARKGOGREEN = (0, 153, 76)
BRIGHTGOGREEN =(0, 204, 102)

# -- Initialise Pygame
pygame.init()
# -- Blank Screen
size = (900,900)
pause = False
stinganti = 3
depth = 0
plasticcollect = 0

screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()

##blackrocks = pygame.image.load("BlackRocks(SS).png").convert_alpha()
##y = 0
##rocks = pygame.image.load("Rock(SS).png").convert_alpha()
##y2 = 0

backround = pygame.image.load("oceangradient.png").convert_alpha()
player_sinking = pygame.image.load("ScubaDiver(Sinking)2.png").convert_alpha()
player_sinkingRIGHT = pygame.image.load("ScubaDiver(Sinking)RIGHT2.png").convert_alpha()
player_neutral = pygame.image.load("ScubaDiver(Neutral)2.png").convert_alpha()
player_neutralRIGHT = pygame.image.load("ScubaDiver(Neutral)RIGHT2.png").convert_alpha()
jellyfishbasic_neutral = pygame.image.load("SmallJellyFish(Neutral).png").convert_alpha()
bottle = pygame.image.load("Bottle.png").convert_alpha()
blackrocks1 = pygame.image.load("BlackRocks(SS)PART1.png").convert_alpha()
blackrocks2 = pygame.image.load("BlackRocks(SS)PART2.png").convert_alpha()
blackrocks3 = pygame.image.load("BlackRocks(SS)PART3.png").convert_alpha()
blackrocks4 = pygame.image.load("BlackRocks(SS)PART4.png").convert_alpha()
greyrocks1 = pygame.image.load("Rock(SS)PART1.png").convert_alpha()
greyrocks2 = pygame.image.load("Rock(SS)PART2.png").convert_alpha()
greyrocks3 = pygame.image.load("Rock(SS)PART3.png").convert_alpha()
greyrocks4 = pygame.image.load("Rock(SS)PART4.png").convert_alpha()



# -- Title of new window/screen
pygame.display.set_caption("Scuba Scroller")
def quitgame():
    pygame.quit()
    quit()

def game_over():
    screen.fill(BLACK)
    screen.blit(backround, (0,0))
    text = pygame.font.SysFont('bubblegums', 50, True, False).render("GAME OVER",True,WHITE)
    screen.blit(text, [220,400])
    text1 = pygame.font.SysFont('bubblegums', 20, True, False).render("You reached " + '%0.0f'%depth + "m",True,WHITE)
    screen.blit(text1, [305,470])
    text1 = pygame.font.SysFont('bubblegums', 20, True, False).render("You cleaned up " + str(plasticcollect) + ' bottles',True,WHITE)
    screen.blit(text1, [230,505])
    pygame.display.flip()
    time.sleep(3)
    quitgame()
##    game_intro()

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
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

##        screen.fill(BLACK)
##        screen.blit(backround, (0,0))
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
                done = True

        screen.fill(BLACK)
        screen.blit(backround, (0,0))
        text = pygame.font.SysFont('bubblegums',45, True, False).render("Scuba Scroller",True,WHITE)
        screen.blit(text, [170,400])

        button( 275, 500, 100, 50, DARKGOGREEN, BRIGHTGOGREEN,game_loop)
        button( 535, 500, 100, 50, DARKRED, BRIGHTRED,quitgame)

        text1 = pygame.font.SysFont('bubblegums', 24, True, False).render("Play",True,WHITE)
        screen.blit(text1, [278, 510])

        text2 = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit",True,WHITE)
        screen.blit(text2, [540, 510])

        pygame.display.flip()

def make_new_jelly(number):
    for i in range(number):
        JB = JellyBasic()
        all_sprites_list.add(JB)
        jellybasicgroup.add(JB)

def make_new_plastic(number):
    for i in range(number):
        P = Plastic()
        all_sprites_list.add(P)
        plasticgroup.add(P)

# - Classes
# -- Define the class invader which is a sprite
class Player(pygame.sprite.Sprite):
    #Define the constructor for player
    def __init__(self):
        #Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.image.set_colorkey(WHITE)
        # Draw the player
        self.image = player_sinking
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Object starting position
        self.rect.x = 425
        self.rect.y = 100

    def MoveRight(self, pixels):
        self.rect.x += pixels
        self.image = player_sinkingRIGHT
        self.mask = pygame.mask.from_surface(self.image)

    def MoveLeft(self, pixels):
        self.rect.x -= pixels
        self.image = player_sinking
        self.mask = pygame.mask.from_surface(self.image)

    def MoveUp(self, pixels):
        self.rect.y -= pixels
        self.image = player_neutral
        self.mask = pygame.mask.from_surface(self.image)

    def MoveDown(self, pixels):
        self.rect.y += pixels
        self.image = player_sinking
        self.mask = pygame.mask.from_surface(self.image)

class JellyBasic(pygame.sprite.Sprite):
    #Define the constructor for player
    def __init__(self):
        #Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([30, 40])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.image.set_colorkey(WHITE)
        # Draw the player
        self.image = jellyfishbasic_neutral
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Object starting position
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(1400, 1550)
        self.speedy = random.randrange(2, 5)
        self.mask = pygame.mask.from_surface(self.image)

# - Jellfish creation update function
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < -10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(1000, 1100)
            self.speedy = random.randrange(2, 5)

class Plastic(pygame.sprite.Sprite):
    #Define the constructor for player
    def __init__(self):
        #Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([30, 40])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.image.set_colorkey(WHITE)
        # Draw the player
        self.image = bottle
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Object starting position
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(2500, 2600)
        self.speedy = random.randrange(2, 6)
        self.mask = pygame.mask.from_surface(self.image)

    # - Bottle creation update function
    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < -200:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(3000, 3100)
            self.speedy = random.randrange(2, 6)

class greyRocks(pygame.sprite.Sprite):
    def __init__(self, image, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # Object starting position
        self.rect.x = 0
        self.rect.y = y
        self.speedy = 3
        self.originY = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom <= 0:
            self.rect.y = 900

class blackRocks(pygame.sprite.Sprite):
    def __init__(self, image, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # Object starting position
        self.rect.x = 0
        self.rect.y = y
        self.speedy = 1
        self.originY = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom <= 0:
            self.rect.y = 900

blackRocksSegment1 = blackRocks(blackrocks1, 0)
blackRocksSegment2 = blackRocks(blackrocks2, 300)
blackRocksSegment3 = blackRocks(blackrocks3, 600)
blackRocksSegment4 = blackRocks(blackrocks4, 900) #change 1 to 4 and add image
greyRocksSegment1 = greyRocks(greyrocks1, 0)
greyRocksSegment2 = greyRocks(greyrocks2, 300)
greyRocksSegment3 = greyRocks(greyrocks3, 600)
greyRocksSegment4 = greyRocks(greyrocks4, 900) #change 1 to 4 and add image

RocksGroup = pygame.sprite.Group()
RocksGroup.add(blackRocksSegment1)
RocksGroup.add(blackRocksSegment2)
RocksGroup.add(blackRocksSegment3)
RocksGroup.add(blackRocksSegment4)
RocksGroup.add(greyRocksSegment1)
RocksGroup.add(greyRocksSegment2)
RocksGroup.add(greyRocksSegment3)
RocksGroup.add(greyRocksSegment4)
# Create a list of the jelly fish (basic) objects
jellybasicgroup = pygame.sprite.Group()
plasticgroup = pygame.sprite.Group()

# -- Creates a list of all sprites
all_sprites_list = pygame.sprite.Group()

player = Player()
jelly = JellyBasic()
plastic = Plastic()

# Add the player to the list of objects
all_sprites_list.add(player)

make_new_jelly(6)
make_new_plastic(1)

# -- Exit game flag set to false
done = False

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
    ### -- Game Loop

    # - Global Variables
    global pause
    global stinganti
    global depth
    global plasticcollect

    # - The clock ticks over
    clock.tick(FPS)

    # -- Exit game flag set to false
    done = False

    while not done:

            # -- User input and controls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_ESCAPE:
                    done = True
                    game_over()
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
        screen.blit(backround, (0,0))
        RocksGroup.draw(screen)
        RocksGroup.update()
        
        font = pygame.font.SysFont('calibri', 16, True, False)
        text = font.render('Sting Antidote Left: ' + str(stinganti), True, WHITE)
        screen.blit(text, [50, 50])
        font = pygame.font.SysFont('AGENTORANGE', 55, True, False)
        depthText = font.render('%0.0f'%depth + 'm', True, WHITE)
        blit_alpha(screen, depthText, (375,200), 128)
        font = pygame.font.SysFont('calibri', 16, True, False)
        text = font.render('Clean Up: ' + str(plasticcollect), True, WHITE)
        screen.blit(text, [50, 70])

        all_sprites_list.draw(screen)


                # -- Sprite Update
        all_sprites_list.update()

        # -- flip display to reveal new position of objects

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
        if stinganti <= 0:
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

            #End If
        collects = pygame.sprite.spritecollide(player, plasticgroup, True, pygame.sprite.collide_mask)
        for collect in collects:
            make_new_plastic(1)

        for i in range (0, len(collects)):
            plasticcollect = plasticcollect + 1

        # - If player hits jellyfish make new one and remove hit one off screen
        hits = pygame.sprite.spritecollide(player, jellybasicgroup, True, pygame.sprite.collide_mask)
        for hit in hits:
            make_new_jelly(1)

        # - For how many jellyfish player hits remove sting antidote
        for i in range (0, len(hits)):
            stinganti = stinganti - 1

        # - Depth increases as clock ticks
        depth = depth + 0.1
       
##        # - Infinate scrolling black rocks
##        global y
##        rel_y = y % blackrocks.get_rect().height
##        screen.blit(blackrocks, (0,rel_y - blackrocks.get_rect().height))
##        if rel_y < HEIGHT:
##            screen.blit(blackrocks, (0, rel_y))
##        y -= 1
##
##        # - Infinate scrolling grey rocks
##        global y2
##        rel_y2 = y2 % rocks.get_rect().height
##        screen.blit(rocks, (0,rel_y2 - rocks.get_rect().height))
##        if rel_y2 < HEIGHT:
##            screen.blit(rocks, (0, rel_y2))
##        y2 -= 3

        # - Information on screen (depth, sting antidote etc)

     
        pygame.display.flip()

        #End While - End of game loop


game_intro()
game_loop()
