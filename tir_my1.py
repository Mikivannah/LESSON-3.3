import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Happy Shooting Game")

icon = pygame.image.load("img/tir.png")
pygame.display.set_icon(icon)

target_icon = pygame.image.load("img/target.png")
target_WIDTH = 50
target_HEIGHT = 50

target_x = random.randint(0, SCREEN_WIDTH - target_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - target_HEIGHT)

color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

running = True
hits = 0
misses = 0
clicks = 0

clock = pygame.time.Clock()

speed = 1  # Speed of target movement

pygame.mixer.music.load('music/happy_song.mp3')  # Load a cheerful melody
pygame.mixer.music.play(-1)  # Play the melody in a loop

while running:
    clock.tick(60)

    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_WIDTH and target_y < mouse_y < target_y + target_HEIGHT:
                hits += 1
                if hits == 30:
                    speed += 1
                    hits = 0
                target_x = random.randint(0, SCREEN_WIDTH - target_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - target_HEIGHT)
            else:
                misses += 1

    target_x += random.randint(-2, 2)  # Move the target randomly
    if target_x > SCREEN_WIDTH:
        target_x = 0

    screen.blit(target_icon, (target_x, target_y))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Выстрел: {clicks}, Точность: {hits}, Пропуск: {misses}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.mixer.music.stop()  # Stop playing the music
pygame.quit()