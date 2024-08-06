import pygame

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



running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.update()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_speed_x = -2
            if event.key == pygame.K_RIGHT:
                rect_speed_x = 2
            if event.key == pygame.K_UP:
                rect_speed_y = -2
            if event.key == pygame.K_DOWN:
                rect_speed_y = 2
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                rect_speed_x = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                rect_speed_y = 0

    rect_coords[0] += rect_speed_x
    rect_coords[1] += rect_speed_y

    screen. fill(BLACK)
    pygame.draw.rect(screen, RED, rect_coords + rect_size, 0)
    pygame.draw.circle(screen, GREEN, (100, 100), 30, 0)
    pygame.display.update()
    time.sleep(0.04)

