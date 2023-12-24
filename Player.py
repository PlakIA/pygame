import pygame
from pygame.locals import *


down = [pygame.image.load('pictures\walk.png'), pygame.image.load('pictures\pstay.png'),
        pygame.image.load('pictures\walk1.png'), pygame.image.load('pictures\pstay.png')]
d = 0
up = [pygame.image.load('pictures\st.png'), pygame.image.load('pictures\stw.png'),
      pygame.image.load('pictures\st.png'), pygame.image.load('pictures\stw1.png')]
u = 0
rt = [pygame.image.load('pictures\its.png'), pygame.image.load('pictures\itw.png'),
      pygame.image.load('pictures\itw1.png'), pygame.image.load('pictures\itw.png')]
r = 0
tl = [pygame.image.load('pictures\ilw.png'), pygame.image.load('pictures\ils.png'),
      pygame.image.load('pictures\ilw1.png'), pygame.image.load('pictures\ils.png')]
t = 0
left = False
right = False
ups = False
dw = False


class Player:
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    image = pygame.image.load('pictures\pstay.png')
    x, y = 0, 0
    px = 10
    while True:
        screen.fill((255, 255, 255))
        pygame.time.delay(40)
        for event in pygame.event.get():
            if pygame.key.get_pressed()[K_LEFT]:
                left = True
            if pygame.key.get_pressed()[K_RIGHT]:
                right = True
            if pygame.key.get_pressed()[K_DOWN]:
                dw = True
            if pygame.key.get_pressed()[K_UP]:
                ups = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_DOWN:
                    dw = False
                if event.key == pygame.K_UP:
                    ups = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if left:
            x -= px
            image = tl[t % 4]
            t += 1
        if right:
            x += px
            image = rt[r % 4]
            r += 1
        if ups:
            y -= px
            image = up[u % 4]
            u += 1
        if dw:
            y += px
            image = down[d % 4]
            d += 1
        screen.blit(image, (x, y))
        pygame.display.update()
