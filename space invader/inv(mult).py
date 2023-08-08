import pygame
# import pygame.locals import *
import random
import sys
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((700, 550))
background = pygame.image.load('ye.png')
pygame.display.set_caption("Spaceship battle")
icon = pygame.image.load('space.png')
pygame.display.set_icon(icon)
plimg = pygame.image.load('space-invaders.png')
plX = 350
plY = 440
plX_change = 0

pl1img = pygame.image.load('player.png')
pl1X = 180
pl1Y = 440
pl1X_change = 0


enimg = []
enX = []
enY = []
enX_change = []
enY_change = []
num_of_enemies = 7

# enemy
for i in range(num_of_enemies):
    enimg.append(pygame.image.load('enemy80.png'))
    enX.append(random.randint(0,630))
    enY.append(random.randint(50,150))
    enX_change.append(0.6)
    enY_change.append(0.06)
# bullet
bulimg = pygame.image.load('bullets.png')
bulX = 0
bulY = 440
bulX_change = 0
bulY_change = 6
# can't see bullet - ready function
bul_state = "ready"
#another bullet
bul1img = pygame.image.load('bullet.png')
bul1X = 0
bul1Y = 440
bul1X_change = 0
bul1Y_change = 6

bul1_state = "ready"

score1_val = 0
score_val = 0
font = pygame.font.Font('homework.otf',48)

testX1 = 10
testY1 = 10

testX = 440
testY = 10

def show_score1(x,y):
    score1 = font.render("Score(pl-1) : " + str(score1_val),True, (255, 215, 0))
    screen.blit(score1, (x, y))
def show_score(x,y):
    score = font.render("Score(pl-2) : " + str(score_val),True, (255, 165, 0))
    
    screen.blit(score, (x, y))
# player
def pl(x, y):
    screen.blit(plimg, (x, y))

def pl1(x, y):
    screen.blit(pl1img, (x, y))

def en(x, y, i):
    screen.blit(enimg[i], (x, y))

def fire_bul(x, y):
    global bul_state
    bul_state = "fire"
    screen.blit(bulimg,(x+16,y+10))    

def fire_bul1(x, y):
    global bul1_state
    bul1_state = "fire"
    screen.blit(bul1img,(x+16,y+10))

def iscoll1(enX,enY,bul1X,bul1Y):
    distance = math.sqrt((math.pow(enX-bul1X,2)) + (math.pow(enY-bul1Y,2)))
    if distance < 27:
        return True
    else:
        return False    

def iscoll(enX,enY,bulX,bulY):
    distance = math.sqrt((math.pow(enX-bulX,2)) + (math.pow(enY-bulY,2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    # plX += 0.1
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #or event.key == ord('a'):
                plX_change = -1.5

            if event.key == pygame.K_RIGHT:# or event.key == ord('d'):
                plX_change = 1.5
            if event.key == ord('a'):
                pl1X_change = -1.5
            if event.key == ord('d'):
                pl1X_change = +1.5
            if event.key == pygame.K_SPACE:
                if bul_state is 'ready':
                    bul_sound = mixer.Sound('laser.wav')
                    bul_sound.play()

                    bulX = plX 
                    fire_bul(bulX,bulY)   
            if event.key == ord('z'):
                if bul1_state is 'ready':
                    bul_sound = mixer.Sound('laser.wav')
                    bul_sound.play()
                    bul1X = pl1X 
                    fire_bul1(bul1X,bul1Y)







            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if event.button == 1:
                    # fire_bul(plX,bulY)    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #or event.key == ord('a') or event.key == ord('d'):
                plX_change = 0
            if event.key == ord('a') or event.key == ord('d'):
                pl1X_change = 0  
    plX  += plX_change
    if plX <= 340:
        plX = 340
    elif plX >= 636:
        plX = 636    

#another player boundary
    pl1X  += pl1X_change
    if pl1X <= 0:
        pl1X = 0
    elif pl1X >= 280:
        pl1X = 280

    for i in range(num_of_enemies):
        enX[i]  += enX_change[i]
        if enX[i] <= 0:
            enX_change[i] = 0.8
        elif enX[i] >= 616:
            enX_change[i] = -0.8
        enY[i] += enY_change[i]
        if enY[i] >=375:
            running = False
            print("bole to game over")

        collision = iscoll(enX[i],enY[i],bulX,bulY)
        if collision:
            expl_sound = mixer.Sound('explosion.wav')
            expl_sound.play()
            bulY = 440 
            bul_state = "ready"
            score_val += 1
            if score_val >= 120:
                print("player 2 WON, CONGRATS")
                running = False
            enX[i] = random.randint(0,630)
            enY[i] = random.randint(0,120)  
        en(enX[i], enY[i], i)

        collision1 = iscoll1(enX[i],enY[i],bul1X,bul1Y)
        if collision1:
            expl_sound = mixer.Sound('explosion.wav')
            expl_sound.play()
            bul1Y = 440 
            bul1_state = "ready"
            score1_val += 1
            if score1_val >= 120:
                print("player 1 WON, CONGRATS")
                running = False
            enX[i] = random.randint(0,630)
            enY[i] = random.randint(0,120)  
        en(enX[i], enY[i], i)
    #bul moment
    if bulY <=0:
        bulY = 440
        bul_state = "ready"
    if bul_state is "fire":
        fire_bul(bulX,bulY)
        bulY -= bulY_change
#another player firing
    if bul1Y <=0:
        bul1Y = 440
        bul1_state = "ready"
    if bul1_state is "fire":
        fire_bul1(bul1X,bul1Y)
        bul1Y -= bul1Y_change
    #collision
    
        

    pl(plX, plY)
    pl1(pl1X, pl1Y)
    show_score(testX, testY)
    show_score1(testX1,testY1)
    pygame.display.update()
