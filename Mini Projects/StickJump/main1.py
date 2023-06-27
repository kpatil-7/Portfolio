from frog import Frog
from bus import Bus
from log import Log
import pygame, sys

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

frog = Frog()
bus = Bus(Bus.STARTING_POSITION, 'Left')
log = Log(Log.STARTING_POSITION, 'Right')

while True:
    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                frog.move_up()
            if event.key == pygame.K_a:  # A
                frog.move_left()
            if event.key == pygame.K_s:  # S
                frog.move_down()
            if event.key == pygame.K_d:  # D
                frog.move_right()

    if frog.rect.colliderect(bus.rect):
        frog.reset_position()
    if frog.rect.colliderect(log.rect):
        frog.move_on_log(log)

    bus.move()
    log.move()

    SCREEN.blit(bus.image, bus.rect)
    SCREEN.blit(log.image, log.rect)
    SCREEN.blit(frog.image, frog.rect)

    pygame.display.flip()