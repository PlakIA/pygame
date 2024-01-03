import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, surface=pygame.Surface((64, 64)), tilename='tile'):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.tilename = tilename
        self.hitbox = self.rect.inflate(-10, -5)
