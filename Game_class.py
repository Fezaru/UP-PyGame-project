import Menu_class
import pygame
SIZE = None  # возможно потом это будет в сериализованном файле


def init_walls(screen):
    x_length = SIZE[0]  # сколько клеток в ширину и высоту карта
    y_length = SIZE[1]
    wall1 = Wall((-50, -50), (x_length + 50, 50), screen)  # верхняя стенка
    wall1.draw()
    wall2 = Wall((-50, y_length), (x_length + 50, 50), screen)  # нижняя стенка
    wall2.draw()
    wall3 = Wall((-50, 0), (50, y_length), screen)    # левая стенка
    wall3.draw()
    wall4 = Wall((x_length, 0), (50, y_length), screen)
    wall4.draw()
    return wall1, wall2, wall3, wall4  # возвращает кортеж стенок (wall1, wall2, wall3, wall4)


class Player(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//spider.png')
        self.screen = screen  # передаю экран чтобы в функции draw на нем отображать

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Wall(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//fence.png')
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self, size):
        global SIZE
        SIZE = size
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        FPS = 60
        BACKGROUND = pygame.image.load('images for spidergame//images//gameBGfilled.png')

        pavuk = Player((0, 0), (50, 50), screen)
        walls = init_walls(screen)

        while True:
            screen.blit(BACKGROUND, (0, 0))
            
            if pavuk.rect.colliderect(walls[0]):
                pavuk.move(0, 50)
            if pavuk.rect.colliderect(walls[1]):
                pavuk.move(0, -50)
            if pavuk.rect.colliderect(walls[2]):
                pavuk.move(50, 0)
            if pavuk.rect.colliderect(walls[3]):
                pavuk.move(-50, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu_class.Menu()
                    pygame.display.quit()
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
