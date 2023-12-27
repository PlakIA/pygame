import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacles):
        super().__init__(groups)

        self.image = pygame.image.load('data/pictures/pstay.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites = obstacles

        self.speed = 3

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

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.animate(self.up_frames)

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.animate(self.down_frames)

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.animate(self.right_frames)

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.animate(self.left_frames)

        for tile in self.obstacle_sprites:
            if tile.tilename == 'journal':
                if tile.rect.colliderect(self.rect):
                    if keys[pygame.K_RETURN]:
                        print('EVENT')
                    if keys[pygame.K_BACKSPACE]:
                        print('ALT EVENT')

