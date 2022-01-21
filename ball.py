import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.x_speed = 3
        self.y_speed = 5

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        #self.image = pygame.Surface((radius*2, radius*2))
        self.image = pygame.image.load("baseball.png")
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created. Just use the pygame.draw.circle method.
        # The surface will be self.image

        # Give the ball an initial speed. You will need a speed for the x direction and one for the y direction.


    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.windowHeight:
            self.y_speed = -self.y_speed

    def collide(self, p):
        if pygame.sprite.spritecollide(self, p, False):
            self.y_speed = -self.y_speed

    def collide_bricks(self, b):
        if pygame.sprite.spritecollide(self, b, True):
            self.y_speed = -self.y_speed