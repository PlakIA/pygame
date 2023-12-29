import sys

import pygame

from level import Level
from level2 import Level2
import settings


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):

        while True:

            if settings.current_lvl != settings.old_current_lvl:
                if settings.current_lvl == 2:
                    self.level = Level2()
                settings.old_current_lvl = settings.current_lvl

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((255, 255, 255))
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
