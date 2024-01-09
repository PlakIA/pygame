from level import *

import settings
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles, player, au=False):
        super().__init__(groups)

        self.image = pygame.image.load('data/pictures/pstay.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites = obstacles
        self.hitbox = self.rect.inflate(-20, -10)
        self.player = player

        self.speed = 1
        self.direction = pygame.math.Vector2()

        self.level2_unlock = False

        self.frame_index = 0
        self.animation_speed = 0.04 * self.speed
        if au:
            self.down_frames = [pygame.image.load('data/pictures/awalk1.png'), pygame.image.load('data/pictures/astay.png'),
                                pygame.image.load('data/pictures/awalk.png'), pygame.image.load('data/pictures/astay.png')]
            self.up_frames = [pygame.image.load('data/pictures/ast.png'), pygame.image.load('data/pictures/astw.png'),
                              pygame.image.load('data/pictures/ast.png'), pygame.image.load('data/pictures/astw1.png')]
            self.right_frames = [pygame.image.load('data/pictures/aits.png'), pygame.image.load('data/pictures/aitw.png'),
                                 pygame.image.load('data/pictures/aitw1.png'), pygame.image.load('data/pictures/aitw.png')]
            self.left_frames = [pygame.image.load('data/pictures/ailw.png'), pygame.image.load('data/pictures/ails.png'),
                                pygame.image.load('data/pictures/ailw1.png'), pygame.image.load('data/pictures/ails.png')]
        else:
            self.down_frames = [pygame.image.load('data/pictures/walk1.png'),
                                pygame.image.load('data/pictures/pstay.png'),
                                pygame.image.load('data/pictures/walk.png'),
                                pygame.image.load('data/pictures/pstay.png')]
            self.up_frames = [pygame.image.load('data/pictures/st.png'), pygame.image.load('data/pictures/astw.png'),
                              pygame.image.load('data/pictures/st.png'), pygame.image.load('data/pictures/astw1.png')]
            self.right_frames = [pygame.image.load('data/pictures/aits.png'),
                                 pygame.image.load('data/pictures/aitw.png'),
                                 pygame.image.load('data/pictures/aitw1.png'),
                                 pygame.image.load('data/pictures/aitw.png')]
            self.left_frames = [pygame.image.load('data/pictures/ailw.png'),
                                pygame.image.load('data/pictures/ails.png'),
                                pygame.image.load('data/pictures/ailw1.png'),
                                pygame.image.load('data/pictures/ails.png')]

        self.radius = 400
    def df(self):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(self.player.rect.center)
        dic = (player_vec - enemy_vec).magnitude()
        if 50 < dic <= self.radius:
            self.direction = (player_vec - enemy_vec).normalize()
        else:
            self.direction = pygame.math.Vector2()


                ###dx, dy = self.direction.x - player.direction.x, self.rect.y - player.rect.y
                #print(dx)
                #dist = math.hypot(dx, dy) + 1
                #dx, dy = dx / dist, dy / dist  # Normalize.
                # Move along this normalized vector towards the player at current speed.
                #self.rect.x += dx * self.speed
                #self.rect.y += dy * self.speed
                # Find direction vector (dx, dy) between enemy and player.
                #dirvect = pygame.math.Vector2(self.rect.x - player.rect.x,
                                              #self.rect.y - player.rect.y)
                #dirvect.normalize()
                # Move along this normalized vector towards the player at current speed.
                #dirvect.scale_to_length(self.speed)
                #self.rect.move_ip(dirvect)

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

    def update(self):
        self.input()
        self.df()
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision('x')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('y')
        self.rect.center = self.hitbox.center

    def input(self):
        self.enemy_vec = pygame.math.Vector2(self.rect.center)
        self.player_vec = pygame.math.Vector2(self.player.rect.center)
        if (self.player_vec[0] < self.enemy_vec[0] and
                abs(self.player_vec[0] - self.enemy_vec[0]) > abs(self.player_vec[1] - self.enemy_vec[1])):
            self.animate(self.left_frames)
        elif (self.player_vec[0] > self.enemy_vec[0] and
              abs(self.player_vec[0] - self.enemy_vec[0]) > abs(self.player_vec[1] - self.enemy_vec[1])):
            self.animate(self.right_frames)
        if (self.player_vec[1] < self.enemy_vec[1] and
              abs(self.player_vec[0] - self.enemy_vec[0]) < abs(self.player_vec[1] - self.enemy_vec[1])):
            self.animate(self.up_frames)
        elif (self.player_vec[1] > self.enemy_vec[1] and
              abs(self.player_vec[0] - self.enemy_vec[0]) < abs(self.player_vec[1] - self.enemy_vec[1])):
            self.animate(self.down_frames)

