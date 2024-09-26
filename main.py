import pygame
from classes.Heart import Heart
from classes.Mob import Mob
from classes.Player import Player

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

player_img = pygame.image.load('img/space_shooter_pic.png')
mob_images = [
    pygame.image.load('img/meteor_big_00.png'),
    pygame.image.load('img/meteor_medium_00.png'),
    pygame.image.load('img/meteor_small_00.png')
]
lives_img = pygame.image.load(
    'img/png-transparent-minecraft-video-game-health-game-result-thumbnail-removebg-preview.png')

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(WIDTH, HEIGHT, player_img, all_sprites, bullets, pew_sound)
all_sprites.add(player)
mobs = pygame.sprite.Group()

for i in range(8):
    m = Mob(mob_images, WIDTH, HEIGHT)
    all_sprites.add(m)
    mobs.add(m)

running = True
hearts = []


def spawn_hearts():
    player_lives = player.lives
    pos_x = 10
    for j in range(player_lives):
        pos_x += 20
        heart = Heart(pos_x, 10, lives_img)
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
        m = Mob(mob_images, WIDTH, HEIGHT)
        all_sprites.add(m)
        mobs.add(m)

    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
