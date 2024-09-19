import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.image = pygame.transform.scale(player_img, (25, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 10
        if self.rect.left <= 0:
            self.rect.left = 10
        if self.rect.top <= 0:
            self.rect.top = 10
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - 10

        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, RED)
        all_sprites.add(bullet)
        bullets.add(bullet)
        pew_sound.play()
