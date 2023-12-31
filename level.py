import csv

import pygame

from Player import Player
from settings import *
from tile import Tile
from Enemy import Enemy


class Level:
    def __init__(self):
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        layouts = {'walls': import_csv_layout('data/levels/maps/1_walls.csv'),
                   'entity': import_csv_layout('data/levels/maps/1_entity.csv')}

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * 64
                        y = row_index * 64
                        if style == 'walls':
                            Tile((x, y), (self.obstacle_sprites))
                        if style == 'entity':
                            if col == '63':
                                Tile((x, y), (self.obstacle_sprites, self.visible_sprites),
                                     pygame.image.load('data/tiles/stanislavna.png'), tilename='transition')
                            if col == '31':
                                Tile((x, y), (self.visible_sprites, self.obstacle_sprites),
                                     pygame.image.load('data/tiles/tileset_50.png'), tilename='journal')
                            if col == '21':
                                Enemy((x, y), (self.visible_sprites), self.obstacle_sprites, self.player)
                            if col == '11':
                                self.dver = Tile((x, y), (self.visible_sprites, self.obstacle_sprites),
                                                 pygame.image.load('data/pictures/dver.png'), tilename='dver')
                            if col == '54':
                                self.player = Player((x, y), (self.visible_sprites), self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_c] and self.player.dver_flag:
            self.dver = Tile((pygame.math.Vector2(self.player.rect.center)[0] + 20,
                              pygame.math.Vector2(self.player.rect.center)[1] - 30),
                             (self.visible_sprites, self.obstacle_sprites),
                             pygame.image.load('data/pictures/dverbok.png'), tilename='dver')


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('data/levels/1.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


def import_csv_layout(path):
    terrain_map = list()
    with open(path, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            terrain_map.append(list(row))
        return terrain_map
