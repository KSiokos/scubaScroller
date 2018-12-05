import pygame
import random
import time
from math import *
from assets import *
from global_vars import *
from rocks import *
from player import *
from plastics import *
from bubble import *
# from helpers import *
from jelly import *

# -- Initialise Pygame
pygame.init()
clock = pygame.time.Clock()

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
    JELLY_TYPE = INITIAL_JELLY_TYPE

# def addText(font, size, location, text):

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Background
        screen.blit(backround, (0,0))
        
        # Title
        text = pygame.font.SysFont('bubblegums', 45, True, False).render("Scuba Scroller", True, WHITE)
        screen.blit(text, [170,400])

        # Play Button
        playButton = button(275, 500, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        playText = pygame.font.SysFont('bubblegums', 24, True, False).render("Play", True, WHITE)
        screen.blit(playText, [278, 510])
        if playButton:
            intro = False

        # Quit Button
        quitButton = button(535, 500, 100, 50, DARKRED, BRIGHTRED)
        quitText = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit", True, WHITE)
        screen.blit(quitText, [540, 510])
        if quitButton:
            intro = False
            pygame.quit()

        pygame.display.flip()
def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Title
        text = pygame.font.SysFont('bubblegums', 45, True, False).render("Paused",True,WHITE)
        screen.blit(text, [325,400])

        # Resume Button
        resumeButton = button(275, 500, 160, 50, DARKGOGREEN, BRIGHTGOGREEN)
        resumeText = pygame.font.SysFont('bubblegums', 24, True, False).render("Resume", True, WHITE)
        screen.blit(resumeText, [278, 510])
        if resumeButton:
            pause = False

        # Quit Button
        quitButton = button(535, 500, 100, 50, DARKRED, BRIGHTRED)
        quitText = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit", True, WHITE)
        screen.blit(quitText, [540, 510])
        if quitButton:
            pause = False
            pygame.quit()

        pygame.display.flip()        
def game_over():
    global DEPTH, PLASTICS, JELLYID, HEALTH, RED, GREEN
    game = True
    retry = False
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Background
        screen.blit(backround, (0,0))

        # Title
        titleText = pygame.font.SysFont('bubblegums', 50, True, False).render("GAME OVER",True,WHITE)
        screen.blit(titleText, [220,400])

        # Depth Reached
        depthText = pygame.font.SysFont('bubblegums', 20, True, False).render("You reached " + '%0.0f'%DEPTH + "m",True,WHITE)
        screen.blit(depthText, [305,470])

        # Plastics Collected
        plasticText = pygame.font.SysFont('bubblegums', 20, True, False).render("You cleaned up " + str(PLASTICS) + ' bottles',True,WHITE)
        screen.blit(plasticText, [230,505])

        # Jelly Popped

        # Play Button
        retryButton = button(275, 500, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        retryText = pygame.font.SysFont('bubblegums', 24, True, False).render("Retry", True, WHITE)
        screen.blit(retryText, [278, 510])
        if retryButton:
            retry = True
            game = False

        # Quit Button
        quitButton = button(535, 500, 100, 50, DARKRED, BRIGHTRED)
        quitText = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit", True, WHITE)
        screen.blit(quitText, [540, 510])
        if quitButton:
            game = False
            pygame.quit()

        pygame.display.flip()
    cleanSlate()
    return retry
def game_loop():
    # - Global Variables
    global DEPTH, PLASTICS, HEALTH, RED, GREEN, JELLY_TYPE
    clock.tick(FPS)                                                     # The clock ticks over
    done = False
    player = Player()                                       # Player Object
    all_sprites_list.add(player)
    agentOrange = pygame.font.SysFont('AGENTORANGE', 55, True, False)
    incremented = False
    counter = 50
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()           
                    
        # -- Setup Background
        screen.blit(backround, (0,0))

        # -- Setup and move Rocks
        RocksGroup.draw(screen)
        RocksGroup.update()

        # - Information on screen
        depthFont = pygame.font.SysFont('AGENTORANGE', 55, True, False)
        depthText = depthFont.render('%0.0f'%DEPTH + 'm', True, WHITE)
        blit_alpha(screen, depthText, (375, 200), 128)
        font = pygame.font.SysFont('calibri', 32, True, False)
        screen.blit(bottle, [40, 50])
        plasticsText = font.render('x' + str(PLASTICS), True, WHITE)
        screen.blit(plasticsText, [70, 70])
        
        # - Health Bar
        healthBarColour = (int(RED), int(GREEN), 0)
        pygame.draw.rect(screen, healthBarColour, [290, 40, HEALTH, 20])
        healthBarText = pygame.font.SysFont('calibri', 26, True, False).render(str(int(100*HEALTH/INITIAL_HEALTH)) + "%", True, WHITE)
        screen.blit(healthBarText, [435,42])

        # -- Draw and Update All Sprites
        all_sprites_list.draw(screen)
        all_sprites_list.update()

        # Update Player
        player.update()

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
                elif event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_p:
                    paused()

        # - Game over requirements
        if HEALTH <= 0.5:
            done = True

        # -- Collisions

        # Player and Plastics Collision
        collects = pygame.sprite.spritecollide(player, plasticsGroup, True, pygame.sprite.collide_mask)
        for collect in collects:
            make_new_plastic(1)
            PLASTICS = PLASTICS + 1
            
        # Player and Grey Rocks Collision
        playerGreyRockCollision = pygame.sprite.spritecollide(player, greyRocksGroup, False, pygame.sprite.collide_mask)
        for everyGreyRockCollision in playerGreyRockCollision:
            damage("greyRocks")

        # Player and Black Rocks Collision
        playerBlackRockCollision = pygame.sprite.spritecollide(player, blackRocksGroup, False, pygame.sprite.collide_mask)
        for everyBlackRockCollision in playerBlackRockCollision:
            damage("blackRocks")

        # Player and JellyFish Collision 
        playerJellyCollision = pygame.sprite.spritecollide(player, jellyFishGroup, False, pygame.sprite.collide_mask)
        for jelly in playerJellyCollision:
            if jelly.getBubble():
                jelly.kill()
            else:
                jellyFishGroup.remove(jelly)
                damage("jelly")

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

        # Plastics and GreyRocks Collision
        plasticsRocksCollision = pygame.sprite.groupcollide(greyRocksGroup, plasticsGroup, False, False, pygame.sprite.collide_mask)
        if plasticsRocksCollision:
            plastic = list(plasticsRocksCollision.values())[0].pop()
            plastic.changeDirection()
        
        # Keep 6 JellyFish alive at all times
        if len(jellyFishGroup) <= 6:
            difference = 6 - len(jellyFishGroup)
            make_new_jelly(difference, JELLY_TYPE)

        # Keep 1 Plastic at all times
        if len(plasticsGroup) < 1:
            make_new_plastic(1)


        # - Depth increases as clock ticks
        DEPTH += DEPTHRATE
        
        # Change Jelly Type
        if (DEPTH > TUTORIAL_DEPTH):
            if ((int(DEPTH)-TUTORIAL_DEPTH)%JELLY_CHANGE_INTERVAL == 0) and incremented == False:
                if JELLY_TYPE < 5:
                    JELLY_TYPE += 1
                else:
                    JELLY_TYPE = 0
                incremented = True
        if incremented == True:
            if counter > 0:
                counter -= 1
            else:
                incremented = False
                counter = 50

        # - Health regenrates with time
        regenrateHealth()

        # -- flip display to reveal new position of objects
        pygame.display.flip()

game_intro()
game_loop()
retry = game_over()
while retry:
    game_loop()
    retry = game_over()