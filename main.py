import pygame
from random import *

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

# Sounds
pygame.mixer.init()
main_sound = pygame.mixer.Sound('sounds/main_FrozenJam_song.ogg')
main_sound.set_volume(0.1)
main_sound.play()
pew_sound = pygame.mixer.Sound('sounds/pew.wav')
main_sound.set_volume(0.1)


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
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        pew_sound.play()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
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

        if self.rect.right >= WIDTH + 30 or self.rect.left <= -30 or self.rect.bottom >= HEIGHT + 30:
            self.rect.centerx = randint(0, WIDTH)
            self.rect.top = -10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(lives_img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player_img = pygame.image.load('img/space_shooter_pic.png')
mob_images = [
    pygame.image.load('img/meteor_big_00.png'),
    pygame.image.load('img/meteor_medium_00.png'),
    pygame.image.load('img/meteor_small_00.png')
]
lives_img = pygame.image.load(
    'img/png-transparent-minecraft-video-game-health-game-result-thumbnail-removebg-preview.png')

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
hearts = []


def spawn_hearts():
    player_lives = player.lives
    pos_x = 10
    for j in range(player_lives):
        pos_x += 20
        heart = Heart(pos_x, 10)
        hearts.append(heart)
        if isinstance(heart, Heart):
            all_sprites.add(heart)


spawn_hearts()
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # player and meteorite collision
    hits = pygame.sprite.spritecollide(player, mobs, True)

    if hits:
        player.lives -= 1
        all_sprites.remove(hearts)
        hearts = []
        spawn_hearts()

    if player.lives == 0:
        running = False

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
