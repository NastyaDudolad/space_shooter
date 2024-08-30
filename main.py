import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, WIDTH)
        self.rect.top = -10
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 7)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right >= WIDTH + 30 or self.rect.left <= -30 or self.rect.bottom >= HEIGHT + 30:
            self.rect.centerx = random.randint(0, WIDTH)
            self.rect.top = -10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect.bottom = y
        self.rect.centerx = -10
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


player_img = pygame.image.load('img/space_shooter_pic.png')
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
