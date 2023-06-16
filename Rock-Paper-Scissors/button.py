# This class control the button behavior

import pygame

class Button:
    def __init__(self, position, size, image):
        self.image = pygame.transform.scale(image, size)
        self.size = size
        self.position = position
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0], position[1])

    def collide(self, x, y):
        return self.rect.collidepoint(x, y)

    def change_image(self, new_image):
        self.image = pygame.transform.scale(new_image, self.size)