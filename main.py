import pygame
import random
import time
import json
from math import *
from assets import *
from global_vars import *
from rocks import *
from player import *
from plastics import *
from bubble import *
from helpers import *
from jelly import *

# -- Initialise Pygame
pygame.init()
clock = pygame.time.Clock()

def createJelly(number, type):
    for i in range(number):
        JB = Jelly(type)
        all_sprites_list.add(JB)
        jellyFishGroup.add(JB)

def createPlastic(number):
    plasticChoices = [bottle, bag]
    plasticType = random.choice(plasticChoices)
    for i in range(number):
        P = Plastic(plasticType)
        all_sprites_list.add(P)
        plasticsGroup.add(P)

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

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Background
        screen.blit(backround, (0,0))
        
        # Title
        addText("Scuba", "bubblegums", 55, ["center", 320])
        addText("Scroller", "bubblegums", 55, ["center", 400])

        # Leaderboard Button
        leaderboardButton = addButton(315, 590, 273, 50, DARKGOGREEN, BRIGHTGOGREEN)
        addText("Leaderboard", "bubblegums", 24, [318, 600])
        if leaderboardButton:
            leaderboard()

        # Play Button
        playButton = addButton(270, 500, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        addText("Play", "bubblegums", 24, [273, 510])
        if playButton:
            intro = False

        # Quit Button
        quitButton = addButton(530, 500, 100, 50, DARKRED, BRIGHTRED)
        addText("Quit", "bubblegums", 25, [535, 510])
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
        addText("Paused", "bubblegums", 45, [325, 400])

        # Resume Button
        resumeButton = addButton(275, 500, 160, 50, DARKGOGREEN, BRIGHTGOGREEN)
        addText("Resume", "bubblegums", 24, [278, 510])
        if resumeButton:
            pause = False

        # Quit Button
        quitButton = addButton(535, 500, 100, 50, DARKRED, BRIGHTRED)
        addText("Quit", "bubblegums", 25, [540, 510])
        if quitButton:
            pause = False
            pygame.quit()

        pygame.display.flip()        
def game_over():
    # Global Variables
    global DEPTH, PLASTICS, JELLYID, HEALTH, RED, GREEN
    # Flags
    game_over = True
    retry = False
    updateLeaderboard = False
    
    # Highscore variables
    myScore = int(SCORE)
    lowestScore = pullScore("low")
    
    # Condition to update highscores
    if myScore >= lowestScore:
        updateLeaderboard = True
        name = ''
    
    # Main Loop
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Event for updating highscore
            if updateLeaderboard == True:
                if event.type == pygame.KEYDOWN:
                    # Return key finalises name and resets name variable to empty
                    if event.key == pygame.K_RETURN:
                        # Update leaderboard.txt
                        pushScore(name, myScore)
                        name = ''
                        updateLeaderboard = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        # Limits name to hold 3 characters
                        if len(name) < 4:
                            name += event.unicode

        # Background
        screen.blit(backround, (0,0))

        # Update Leaderboard
        if updateLeaderboard == True:
            # Draw textbox on screen for name
            pygame.draw.rect(screen, BLACK, (405, 725, 110, 50))
            pygame.draw.rect(screen, WHITE, (410, 730, 100, 40))
            addText(name, "calibri", 40, [422, 740], BLACK)

        # Title
        addText("GAME OVER", "bubblegums", 50, ["center", 75])

        # Main Score
        scoreText = str("{:06d}".format(int(SCORE)))
        addText(scoreText, "bubblegums", 30, ["center", 170])

        # Depth Reached

        depthText = "You reached " + '%0.0f'%DEPTH + "m"
        addText(depthText, "calibri", 28, ["center", 590])

        # Plastics Collected
        plasticText = "You cleaned up " + str(PLASTICS) + " bottles"
        addText(plasticText, "calibri", 28, ["center", 630])

        # Jelly Popped
        jellyText = "You popped " + str(JELLY_KILLED) + " JellyFish"
        addText(jellyText, "calibri", 28, ["center", 670])
        
        # High Scores
        displayTop5Scores("game_over")

        # Retry Button
        retryButton = addButton(272, 800, 125, 50, DARKGOGREEN, BRIGHTGOGREEN)
        addText("Retry", "bubblegums", 24, [275, 810])
        if retryButton:
            retry = True
            game_over = False

        # Quit Button
        quitButton = addButton(535, 800, 100, 50, DARKRED, BRIGHTRED)
        addText("Quit", "bubblegums", 25, [540, 810])
        if quitButton:
            game_over = False
            pygame.quit()

        pygame.display.flip()
    cleanSlate()
    return retry
def game_loop():
    # - Global Variables
    global SCORE, DEPTH, PLASTICS, HEALTH, RED, GREEN, JELLY_TYPE, JELLY_KILLED
    clock.tick(FPS)                                                     
    done = False
    player = Player()                                       # Player Object
    all_sprites_list.add(player)
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
        
        # Ongoing Depth
        depthText = '%0.0f'%DEPTH + 'm'
        addText(depthText, "agentOrange", 55, ["center", 200], GREY)
        
        # Plastic Bottle Counter
        screen.blit(bottle, [40, 50])
        plasticsText = 'x' + str(PLASTICS)
        addText(plasticsText, "calibri", 32, [70, 70])
        
        # Health Bar
        healthBarColour = (int(RED), int(GREEN), 0)
        pygame.draw.rect(screen, healthBarColour, [280, 40, HEALTH, 25])
        healthBarText = str(int(100*HEALTH/INITIAL_HEALTH)) + "%"
        addText(healthBarText, "calibri", 26, ["center", 42])

        # Score
        scoreText = str("{:06d}".format(int(SCORE)))
        addText(scoreText, "agentOrange", 26, [700, 50])

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
                        bubble = Bubble(x, y, 2, 0)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootRight()
                elif event.key == pygame.K_LEFT:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, -2, 0)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootLeft()
                elif event.key == pygame.K_UP:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, 0, -2)
                        BubbleGroup.add(bubble)
                        all_sprites_list.add(bubble)
                    player.shootTop()
                elif event.key == pygame.K_DOWN:
                    if len(BubbleGroup) < BUBBLE_LIMIT:
                        [x, y] = player.getPos()
                        bubble = Bubble(x, y, 0, 2)
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
                JELLY_KILLED += 1
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
        
        # Keep 9 JellyFish alive at all times
        if len(jellyFishGroup) <= 9:
            difference = 9 - len(jellyFishGroup)
            createJelly(difference, JELLY_TYPE)

        # Keep 1 Plastic at all times
        if len(plasticsGroup) < 1:
            createPlastic(1)


        # - Depth increases as clock ticks
        DEPTH += DEPTHRATE
        
        # Change Jelly Type
        if (DEPTH > TUTORIAL_DEPTH):
            if ((int(DEPTH)-TUTORIAL_DEPTH)%JELLY_CHANGE_INTERVAL == 0) and incremented == False:
                if JELLY_TYPE < 4:
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

        # Update score
        SCORE = DEPTH + JELLY_KILLED*100 + PLASTICS*200

        # -- flip display to reveal new position of objects
        pygame.display.flip()
def leaderboard():
    leaderboard = True
    while leaderboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Background
        screen.blit(backround, (0,0))
        
        # Title
        addText("Leaderboard", "bubblegums", 55, ["center", 75])

        # Back Button
        backButton = addButton(400, 800, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        addText("Back", "bubblegums", 24, [403, 810])
        if backButton:
            leaderboard = False

        # Display high scores on the screen
        pullScore("high")

        # Display top 5 scores on the screen
        displayTop5Scores("leaderboard")

        pygame.display.flip()

game_intro()
game_loop()
retry = game_over()
while retry:
    game_loop()
    retry = game_over()
