import pygame


class Bus(pygame.sprite.Sprite):
    # Define constant values
    LEFT_IMAGE = pygame.image.load('resources/bus_left.png')
    RIGHT_IMAGE = pygame.image.load('resources/bus_right.png')
    STARTING_POSITION = (300, 250)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2

    # Creates a Bus object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Bus.LEFT_IMAGE if direction == 'Left' else Bus.RIGHT_IMAGE
        
        # Bus Information
        self.rect = pygame.Rect((0, 0), Bus.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
         # Bus is going left
        if self.direction == 'Left':
            self.rect.centerx -= Bus.MOVE_DIST
            # Bus has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Bus.SCREEN_DIM[0] + Bus.SIZE[0] / 2
        # Bus is going right
        else:
            self.rect.centerx += Bus.MOVE_DIST
            # Bus has moved off the screen
            if self.rect.left >= Bus.SCREEN_DIM[0]:
                self.rect.centerx = -Bus.SIZE[0] / 2