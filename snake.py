

from random import randint
from time import sleep
import pygame
pygame.init()
WIDTH,HEIGHT = 600,600

# Snake info
snakes = [[0,1],[0,2],[0,3],[0,4]]

direction = "right"
apple = [randint(0,29),randint(0,29)]
point = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ran san moi')
running = True
clock = pygame.time.Clock()
pausing = False
font = pygame.font.SysFont('sans',20)
big_font = pygame.font.SysFont('sans',40)

GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

while running:

    screen.fill(GREEN)
    #pygame.draw.rect(screen,RED,(0,0,50,50))
    snake_tail_x = snakes[0][0]
    snake_tail_y = snakes[0][1]
    #draw glid
    """for i in range (30):
        pygame.draw.line(screen,WHITE,(0,20*i),(600,20*i))
        pygame.draw.line(screen,WHITE,(20*i,0),(20*i,600))"""
    #draw snake
    for snake in snakes:
        pygame.draw.rect(screen,RED,((snake[0]*20),(snake[1]*20),20,20))

    #draw apple
        pygame.draw.rect(screen,YELLOW,(apple[0]*20,apple[1]*20,20,20))

    #Point
    score = font.render("SCORE = " + str(point),True,BLACK)
    screen.blit(score,(0,0))

    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0,[snake_tail_x,snake_tail_y])
        for snake in snakes:
            while(apple[0] == snake[0] and apple[1] == snake[1]):
                apple = [randint(0,29),randint(0,29)]
                point+=1
    #game over
    if snakes[-1][0] < 0 :
        snakes[-1][0] = 29
    if snakes[-1][0] > 29 :
        snakes[-1][0] = 0
    if snakes[-1][1] < 0 :
        snakes[-1][1] = 29
    if snakes[-1][1] >29  :
        snakes[-1][1] = 0

    
   

    #snake move
    
    if pausing == False:
        if direction == "right":
                snakes.append([snakes[-1][0]+1,snakes[-1][1]])
                snakes.pop(0)
                sleep(0.05)
        if direction == "left":
                snakes.append([snakes[-1][0]-1,snakes[-1][1]])
                snakes.pop(0)
                sleep(0.05)
        if direction == "up":
                snakes.append([snakes[-1][0],snakes[-1][1]-1])
                snakes.pop(0)
                sleep(0.05)
        if direction == "down":
                snakes.append([snakes[-1][0],snakes[-1][1]+1])
                snakes.pop(0)
                sleep(0.05)
    
    for i in range (len(snakes) -1):
        if snakes[-1][0] == snakes[i][0]and snakes[-1][1] == snakes[i][1]:
            pausing = True
     #drawing game over
    if pausing == True:
        gameover = big_font.render("GAME OVER! SCORE = " + str(point),True,BLACK)
        retry = font.render ("Press Space to try again",True,BLACK)
        pygame.draw.rect(screen,WHITE,(100,200,400,200))
        screen.blit(gameover,(100,250))
        screen.blit(retry,(250,300))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != "down":
                    direction = "up"
            if event.key == pygame.K_DOWN:
                if direction != "up":
                    direction = "down"
            if event.key == pygame.K_LEFT:
                if direction != "right":
                    direction = "left"

            if event.key == pygame.K_RIGHT:
                if direction != "left":
                    direction = "right"
            if event.key == pygame.K_SPACE:
                pausing = False
                snakes = [[0,1],[0,2],[0,3],[0,4]]
                apple = [randint(0,29),randint(0,29)]
                direction= "right"
                point = 0

    pygame.display.flip()
pygame.quit()

