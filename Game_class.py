import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


class Game():
    def __init__(self):
        screen = pygame.display.set_mode((720, 480))
        clock = pygame.time.Clock()
        FPS = 60