import pygame
import json
from math import *
import random
from assets import *
from global_vars import *
from jelly import *
from plastics import *

def addText(text, font, size, location, color=WHITE):
    # Render correct font from file
    if font == "bubblegums":
        fontToUse = pygame.font.Font("assets/fonts/BUBBLEGUMS.TTF", size)
        fontToUse.set_bold(True)
    elif font == "agentOrange":
        fontToUse = pygame.font.Font("assets/fonts/AGENTORANGE.TTF", size)
        fontToUse.set_bold(True)
    elif font == "calibri":
        fontToUse = pygame.font.SysFont('calibri', size, True, False)
    # Create text surface
    textToAdd = fontToUse.render(text, True, color)
    # Find position on screen
    if location[0] == "center":
        x = WIDTH/2 - textToAdd.get_width()/2
        y = location[1]
    else:
        x = location[0]
        y = location[1]
    # Blit on screen
    screen.blit(textToAdd, (x,y))

def addButton(x, y, width, height, inactivecolour, activecolour):
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

def cleanSlate():
    global SCORE, DEPTH, PLASTICS, JELLY_KILLED, JELLYID, HEALTH, RED, GREEN, JELLY_TYPE
    
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
        scoreText = "Highest Score " + score
        addText(scoreText, "bubblegums", 27, [225, 170])
    elif scoreEnd == "low":
        score = scores[4][1]
        return score

def pushScore(username, userscore):
    # Get original scores from file
    currentScores = readScore()
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
    # Output to file
    with open('leaderboard.txt', 'w') as outfile:
        json.dump(leaderboard, outfile)

def displayTop5Scores(display):
    scores = readScore()
    if display == "leaderboard":
        x = 350
        y = 300
        yStep = 100
    elif display == "game_over":
        x = 340
        y = 270
        yStep = 60
    for score in scores:
        scoreText = score[0] + "             " + str(score[1])
        addText(scoreText, "calibri", 32, [x,y])
        y += yStep