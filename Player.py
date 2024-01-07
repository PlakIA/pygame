import pygame

from level import *

import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load('data/pictures/pstay.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites = obstacles
        self.hitbox = self.rect.inflate(-20, -10)

        self.speed = 5
        self.direction = pygame.math.Vector2()

        self.level2_unlock = False

        self.frame_index = 0
        self.animation_speed = 0.04 * self.speed
        self.down_frames = [pygame.image.load('data/pictures/walk.png'), pygame.image.load('data/pictures/pstay.png'),
                            pygame.image.load('data/pictures/walk1.png'), pygame.image.load('data/pictures/pstay.png')]
        self.up_frames = [pygame.image.load('data/pictures/st.png'), pygame.image.load('data/pictures/stw.png'),
                          pygame.image.load('data/pictures/st.png'), pygame.image.load('data/pictures/stw1.png')]
        self.right_frames = [pygame.image.load('data/pictures/its.png'), pygame.image.load('data/pictures/itw.png'),
                             pygame.image.load('data/pictures/itw1.png'), pygame.image.load('data/pictures/itw.png')]
        self.left_frames = [pygame.image.load('data/pictures/ilw.png'), pygame.image.load('data/pictures/ils.png'),
                            pygame.image.load('data/pictures/ilw1.png'), pygame.image.load('data/pictures/ils.png')]

    def animate(self, framelist):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(framelist):
            self.frame_index = 0

        self.image = framelist[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.rect.center)

    def collision(self, direction):
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'y':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x += -1
            self.animate(self.left_frames)
        elif keys[pygame.K_RIGHT]:
            self.direction.x += 1
            self.animate(self.right_frames)
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y += -1
            self.animate(self.up_frames)
        elif keys[pygame.K_DOWN]:
            self.direction.y += 1
            self.animate(self.down_frames)
        else:
            self.direction.y = 0

    def event_processing(self):
        keys = pygame.key.get_pressed()

        for tile in self.obstacle_sprites:
            if tile.rect.colliderect(self.rect):
                if tile.tilename == 'journal':
                    if keys[pygame.K_RETURN]:
                        print('EVENT')
                        self.level2_unlock = True
                    if keys[pygame.K_BACKSPACE]:
                        print('ALT EVENT')

                if tile.tilename == 'transition':
                    if self.level2_unlock:
                        settings.current_lvl = 2

                if tile.tilename == 'vape':
                    tile.kill()
                    self.speed /= 4
                    self.animation_speed = 0.04 * self.speed
                if tile.tilename == 'dver':
                    tile.kill()

    def update(self):

        self.input()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision('x')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('y')
        self.rect.center = self.hitbox.center

        self.event_processing()
