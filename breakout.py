import pygame, sys
import brick
import paddle
import random
import ball
from pygame.locals import *

# Constants that will be used in the program
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
BRICK_SEP = 4  # The space between each brick
BRICK_Y_OFFSET = 70
BRICK_WIDTH = int((APPLICATION_WIDTH - (BRICKS_PER_ROW * BRICK_SEP)) / BRICKS_PER_ROW)
BRICK_HEIGHT = 8
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
RADIUS_OF_BALL = 10
NUM_TURNS = 3
time = pygame.time.Clock()
# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((255, 255, 255))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)
x_pos = BRICK_SEP
y_pos = BRICK_Y_OFFSET
bricks = pygame.sprite.Group()
black_paddle = pygame.sprite.Group()
for z in [RED, ORANGE, YELLOW, GREEN, CYAN]:
    for y in range(2):
        for x in range(BRICKS_PER_ROW):
           b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, z)
           bricks.add(b)
           b.rect.x = x_pos
           b.rect.y = y_pos
           mainsurface.blit(b.image, b.rect)
           x_pos = x_pos + BRICK_WIDTH + BRICK_SEP
        y_pos = y_pos + BRICK_HEIGHT + 4
        x_pos = BRICK_SEP
p = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, BLACK)
black_paddle.add(p)
p.rect.y = y_pos + 400 - PADDLE_Y_OFFSET
p.rect.x = x_pos + APPLICATION_WIDTH/2 - 35
mainsurface.blit(p.image, p.rect)
red_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
red_ball.rect.y = APPLICATION_HEIGHT/2
red_ball.rect.x = APPLICATION_WIDTH/2
while True:
    mainsurface.fill(WHITE)
    for x in bricks:
        mainsurface.blit(x.image, x.rect)
    p.move()
    mainsurface.blit(p.image, p.rect)
    red_ball.move()
    mainsurface.blit(red_ball.image, red_ball.rect)
    red_ball.collide(black_paddle)
    red_ball.collide(bricks)
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()
    time.tick(60)
