import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, lives_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(lives_img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y