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
    global SCORE, DEPTH, PLASTICS, JELLY_KILLED, JELLYID, HEALTH, RED, GREEN
    
    # Kill all sprites
    for each in all_sprites_list.sprites():
        each.kill()
    # Reset all global variables
    SCORE = INITIAL_SCORE
    DEPTH = INITIAL_DEPTH
    PLASTICS = INITIAL_PLASTICS
    JELLYID = INITIAL_JELLYID
    JELLY_KILLED = INITIAL_JELLY_KILLED
    HEALTH = INITIAL_HEALTH
    RED = INITIAL_RED
    GREEN = INITIAL_GREEN
    JELLY_TYPE = INITIAL_JELLY_TYPE

def readScore():
    localLeaderboard = []
    with open('leaderboard.txt') as json_file:
        scores = json.load(json_file)
        for s in scores['newScores']:
            temp = (s['name'], s['score'])
            localLeaderboard.append(temp)
        return localLeaderboard

def pullScore(scoreEnd):
    scores = readScore()
    if scoreEnd == "high":
        score = str(scores[0][1])
        scoreText = titleFont.render("Highest Score", True, WHITE)
        screen.blit(scoreText, [100,150])
        scoreNumber = titleFont.render(score,True,WHITE)
        screen.blit(scoreNumber, [700,150])
    elif scoreEnd == "low":
        # score = str(scores[4][1])
        score = scores[4][1]
        return score

def pushScore(username, userscore):
    # Get original scores from file
    currentScores = readScore()
    # print(currentScores)

    # Create new structure
    leaderboard = {}
    leaderboard['newScores'] = []
    i = 0
    newname = username
    newscore = userscore

    # Append to new list until position found
    for score in currentScores:
        if userscore < score[1]:
            leaderboard['newScores'].append({'name': score[0],'score': score[1]})
            i += 1
    # Add updated list to new structure
    while i <= 4:
        leaderboard['newScores'].append({'name': newname,'score': newscore})
        newname = currentScores[i][0]
        newscore = currentScores[i][1]
        i += 1
    # print(leaderboard)

    with open('leaderboard.txt', 'w') as outfile:
        json.dump(leaderboard, outfile)

def displayTop5Scores(display):
    scores = readScore()
    if display == "leaderboard":
        x = 300
        y = 300
        yStep = 100
    elif display == "game_over":
        x = 300
        y = 300
        yStep = 50
    for score in scores:
        scoreText = pygame.font.SysFont('calibri', 32, True, False).render(score[0] + "             " + str(score[1]), True, WHITE)
        screen.blit(scoreText, [x,y])
        y += yStep

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
        titleText = titleFont.render("Scuba Scroller", True, WHITE)
        screen.blit(titleText, [170,400])

        # Play Button
        leaderboardButton = button(275, 600, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        leaderboardText = pygame.font.SysFont('bubblegums', 24, True, False).render("Leaderboard", True, WHITE)
        screen.blit(leaderboardText, [278, 610])
        if leaderboardButton:
            leaderboard()

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
                        if len(name) < 3:
                            name += event.unicode

        # Background
        screen.blit(backround, (0,0))

        # Update Leaderboard
        if updateLeaderboard == True:
            # Draw textbox on screen for name
            pygame.draw.rect(screen, WHITE, (450, 450, 100, 50))
            nameText = pygame.font.SysFont(None, 20, True, False).render(name, True, BLACK)
            screen.blit(nameText, [475, 475])

        # Title
        titleText = titleFont.render("GAME OVER", True, WHITE)
        screen.blit(titleText, [225, 75])

        # Main Score
        scoreText = pygame.font.SysFont('bubblegums', 20, True, False).render(str("{:06d}".format(int(SCORE))), True, WHITE)
        screen.blit(scoreText, [305,170])

        # Depth Reached
        depthText = pygame.font.SysFont('bubblegums', 20, True, False).render("You reached " + '%0.0f'%DEPTH + "m",True, WHITE)
        screen.blit(depthText, [305,470])

        # Plastics Collected
        plasticText = pygame.font.SysFont('bubblegums', 20, True, False).render("You cleaned up " + str(PLASTICS) + ' bottles',True, WHITE)
        screen.blit(plasticText, [230,505])

        # Jelly Popped
        jellyText = pygame.font.SysFont('bubblegums', 20, True, False).render("You killed " + str(JELLY_KILLED) + ' JellyFish',True, WHITE)
        screen.blit(jellyText, [230,605])
        
        # High Scores
        displayTop5Scores("game_over")

        # Retry Button
        retryButton = button(275, 800, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        retryText = pygame.font.SysFont('bubblegums', 24, True, False).render("Retry", True, WHITE)
        screen.blit(retryText, [278, 810])
        if retryButton:
            retry = True
            game_over = False

        # Quit Button
        quitButton = button(535, 800, 100, 50, DARKRED, BRIGHTRED)
        quitText = pygame.font.SysFont('bubblegums', 25, True, False).render("Quit", True, WHITE)
        screen.blit(quitText, [540, 810])
        if quitButton:
            game_over = False
            pygame.quit()

        pygame.display.flip()
    cleanSlate()
    return retry
def game_loop():
    # - Global Variables
    global SCORE, DEPTH, PLASTICS, HEALTH, RED, GREEN, JELLY_TYPE, JELLY_KILLED
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
        depthText = agentOrange.render('%0.0f'%DEPTH + 'm', True, GREY)
        screen.blit(depthText, (375, 200))
        font = pygame.font.SysFont('calibri', 32, True, False)
        screen.blit(bottle, [40, 50])
        plasticsText = font.render('x' + str(PLASTICS), True, WHITE)
        screen.blit(plasticsText, [70, 70])
        
        # - Health Bar
        healthBarColour = (int(RED), int(GREEN), 0)
        pygame.draw.rect(screen, healthBarColour, [290, 40, HEALTH, 20])
        healthBarText = pygame.font.SysFont('calibri', 26, True, False).render(str(int(100*HEALTH/INITIAL_HEALTH)) + "%", True, WHITE)
        screen.blit(healthBarText, [435,42])

        # Score
        scoreText = agentOrange.render(str("{:06d}".format(int(SCORE))), True, WHITE)
        screen.blit(scoreText, [730, 50])

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
        titleText = titleFont.render("Leaderboard", True, WHITE)
        screen.blit(titleText, [200,75])

        # Back Button
        backButton = button(400, 800, 100, 50, DARKGOGREEN, BRIGHTGOGREEN)
        backText = pygame.font.SysFont('bubblegums', 24, True, False).render("Back", True, WHITE)
        screen.blit(backText, [403, 810])
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
