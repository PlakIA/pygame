import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load('pictures/pstay.png')
        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 2

        self.frame_index = 0
        self.animation_speed = 0.04 * self.speed
        self.down_frames = [pygame.image.load('pictures\walk.png'), pygame.image.load('pictures\pstay.png'),
                            pygame.image.load('pictures\walk1.png'), pygame.image.load('pictures\pstay.png')]
        self.up_frames = [pygame.image.load('pictures\st.png'), pygame.image.load('pictures\stw.png'),
                          pygame.image.load('pictures\st.png'), pygame.image.load('pictures\stw1.png')]
        self.right_frames = [pygame.image.load('pictures\its.png'), pygame.image.load('pictures\itw.png'),
                             pygame.image.load('pictures\itw1.png'), pygame.image.load('pictures\itw.png')]
        self.left_frames = [pygame.image.load('pictures\ilw.png'), pygame.image.load('pictures\ils.png'),
                            pygame.image.load('pictures\ilw1.png'), pygame.image.load('pictures\ils.png')]

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
