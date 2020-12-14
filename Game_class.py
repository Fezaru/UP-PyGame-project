import Menu_class
import pygame
import random
import tkinter.messagebox

bonus = None
SIZE = None  # возможно потом это будет в сериализованном файле


def init_fences(screen):
    global SIZE
    n = SIZE[0] // 50
    lines = []
    fences = []
    with open('Map1', 'r') as f:
        for i in range(n):
            lines.append(f.readline().strip('\n'))
    coords = [[] for i in range(n)]
    for i in range(n):
        coords[i] = lines[i].split()
    for i in range(n):
        for j in range(len(coords[i])):
            if coords[j][i] == '1':
                fences.append(Wall((i * 50, j * 50), (50, 50), screen))
            if coords[j][i] == '2':
                exit = Exit((i * 50, j * 50), (50, 50), screen)
    return fences, exit


def init_walls(screen):
    x_length = SIZE[0]  # сколько клеток в ширину и высоту карта
    y_length = SIZE[1]
    wall1 = Wall((-50, -50), (x_length + 50, 50), screen)  # верхняя стенка
    wall1.draw()
    wall2 = Wall((-50, y_length), (x_length + 50, 50), screen)  # нижняя стенка
    wall2.draw()
    wall3 = Wall((-50, 0), (50, y_length), screen)  # левая стенка
    wall3.draw()
    wall4 = Wall((x_length, 0), (50, y_length), screen)
    wall4.draw()
    return wall1, wall2, wall3, wall4  # возвращает кортеж стенок (wall1, wall2, wall3, wall4)


class Exit(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//stone.png')
        self.screen = screen  # передаю экран чтобы в функции draw на нем отображать

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def win(self):
        tkinter.messagebox.showinfo('Победа!', 'Вы выиграли')
        Menu_class.Menu()
        pygame.quit()


class Player(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//spider.png')
        self.screen = screen  # передаю экран чтобы в функции draw на нем отображать
        self.__bonuses = 0

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def addBonus(self):
        self.__bonuses += 1

    def remove_bonus(self):
        self.__bonuses -= 1

    def getBonuses(self):
        return self.__bonuses


class Bot(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//bot.png')
        self.screen = screen  # передаю экран чтобы в функции draw на нем отображать

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def follow(self, pavuk: Player):
        x, y = pavuk.rect.x, pavuk.rect.y

        if self.rect.x < x:
            if self.rect.y < y:
                self.move(50, 50)
            elif self.rect.y > y:
                self.move(50, -50)
            else:
                self.move(50, 0)
        elif self.rect.x > x:
            if self.rect.y < y:
                self.move(-50, 50)
            elif self.rect.y > y:
                self.move(-50, -50)
            else:
                self.move(-50, 0)
        else:
            if self.rect.y < y:
                self.move(0, 50)
            elif self.rect.y > y:
                self.move(0, -50)


class Wall(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//fence.png')
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bonus(pygame.sprite.Sprite):
    def __init__(self, xy0: tuple, sizes: tuple, screen):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(xy0, sizes)  # First tuple is position, second is size.
        self.image = pygame.image.load('images for spidergame//images//barrel.png')
        self.screen = screen  # передаю экран чтобы в функции draw на нем отображать

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self, size):
        global bonus
        global SIZE
        SIZE = size
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        FPS = 60
        BACKGROUND = pygame.image.load('images for spidergame//images//gameBGfilled.png')

        pavuk = Player((150, 150), (50, 50), screen)
        bot = Bot((0, 250), (50, 50), screen)
        walls = init_walls(screen)
        fences, escape = init_fences(screen)

        # bonus = Bonus((50, 50), screen)
        bonusStep = 0
        start_ticks = pygame.time.get_ticks()
        timer = 1
        while True:
            screen.blit(BACKGROUND, (0, 0))

            seconds = (pygame.time.get_ticks() - start_ticks) / 1000

            pavukpos = pavuk.rect.copy()

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
                    collision = 0
                    if event.key == pygame.K_w:
                        temp = pavuk.rect.copy()
                        temp.move_ip(0, -50)
                        for fence in fences:
                            if temp.colliderect(fence) == 1:
                                if pavuk.getBonuses() > 0:
                                    fences.remove(fence)
                                    pavuk.remove_bonus()
                                else:
                                    collision = 1
                        if collision != 1:
                            pavuk.move(0, -50)
                    elif event.key == pygame.K_s:
                        temp = pavuk.rect.copy()
                        temp.move_ip(0, 50)
                        for fence in fences:
                            if temp.colliderect(fence) == 1:
                                if pavuk.getBonuses() > 0:
                                    fences.remove(fence)
                                    pavuk.remove_bonus()
                                else:
                                    collision = 1
                        if collision != 1:
                            pavuk.move(0, 50)
                    elif event.key == pygame.K_a:
                        temp = pavuk.rect.copy()
                        temp.move_ip(-50, 0)
                        for fence in fences:
                            if temp.colliderect(fence) == 1:
                                if pavuk.getBonuses() > 0:
                                    fences.remove(fence)
                                    pavuk.remove_bonus()
                                else:
                                    collision = 1
                        if collision != 1:
                            pavuk.move(-50, 0)
                    elif event.key == pygame.K_d:
                        temp = pavuk.rect.copy()
                        temp.move_ip(50, 0)
                        for fence in fences:
                            if temp.colliderect(fence) == 1:
                                if pavuk.getBonuses() > 0:
                                    fences.remove(fence)
                                    pavuk.remove_bonus()
                                else:
                                    collision = 1
                        if collision != 1:
                            pavuk.move(50, 0)

            if seconds >= timer:
                bot.follow(pavuk)
                start_ticks = pygame.time.get_ticks()

            if pavuk.rect.colliderect(escape.rect):
                pygame.display.update()
                escape.win()
            if bonus is not None:
                bonus.draw()
                if pavuk.rect.colliderect(bonus.rect):  # кушает бонус
                    pavuk.addBonus()
                    print(pavuk.getBonuses())
                    bonus = None
            else:
                if pavuk.rect.colliderect(pavukpos) != 1:
                    bonusStep += 1
                if bonusStep == 4:
                    bonusStep = 0
                    isBonusSpawnOkay = False
                    while not isBonusSpawnOkay:
                        bonusX = random.randint(0, (SIZE[0] // 50) - 1) * 50  # спавн бонуса
                        bonusY = random.randint(0, (SIZE[1] // 50) - 1) * 50
                        isInFence = False
                        for fence in fences:
                            if fence.rect.topleft == (bonusX, bonusY):
                                isInFence = True
                        if not isInFence:
                            isBonusSpawnOkay = True
                    bonus = Bonus((bonusX, bonusY), (50, 50), screen)

            for fence in fences:
                fence.draw()
            pavuk.draw()
            bot.draw()
            escape.draw()
            clock.tick(FPS)
            pygame.display.update()  # Or pygame.display.flip()
