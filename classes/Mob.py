import pygame
from random import *


class Mob(pygame.sprite.Sprite):
    def __init__(self, mob_images, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        pygame.sprite.Sprite.__init__(self)
        size = randint(20, 50)
        self.image = pygame.transform.scale(choice(mob_images), (size, size))
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, WIDTH)
        self.rect.top = -10
        self.speedx = randint(-3, 3)
        self.speedy = randint(1, 7)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right >= self.width + 30 or self.rect.left <= -30 or self.rect.bottom >= self.height + 30:
            self.rect.centerx = randint(0, self.width)
            self.rect.top = -10
