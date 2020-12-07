import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


class Game:
    def __init__(self, size):
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        FPS = 60
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        pavuk = pygame.Rect((0, 0), (50, 50))  # First tuple is position, second is size.
        image = pygame.Surface((50, 50))  # The tuple represent size.
        image.fill(WHITE)  # We fill our surface with a nice white color (by default black).

        while True:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        pavuk.move_ip(0, -50)
                    elif event.key == pygame.K_s:
                        pavuk.move_ip(0, 50)
                    elif event.key == pygame.K_a:
                        pavuk.move_ip(-50, 0)
                    elif event.key == pygame.K_d:
                        pavuk.move_ip(50, 0)

            screen.fill(BLACK)
            screen.blit(image, pavuk)
            pygame.display.update()  # Or pygame.display.flip()