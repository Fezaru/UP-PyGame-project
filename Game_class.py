import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


class Player(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, color, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//spider.png')
        self.screen = screen

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self, size):
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        FPS = 60
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BACKGROUND = pygame.image.load('images for spidergame//images//gameBG.png') # тут будет другой бг

        pavuk = Player((0, 0), (50, 50), WHITE, screen)

        while True:
            screen.blit(BACKGROUND, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        pavuk.move(0, -50)
                    elif event.key == pygame.K_s:
                        pavuk.move(0, 50)
                    elif event.key == pygame.K_a:
                        pavuk.move(-50, 0)
                    elif event.key == pygame.K_d:
                        pavuk.move(50, 0)

            pavuk.draw()
            clock.tick(FPS)
            pygame.display.update()  # Or pygame.display.flip()