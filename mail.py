# Игра \Тир\
import pygame
import random
# образуем тело цикла всей игры
pygame.init()

# организация поля игры с использованием pygame.disply /размер/имя/иконка/
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

# создаю переменую. которая подгружает иконку игры
icon = pygame.image.load("img/tir.prn")
pygame.display.set_icon(icon)

target_icon = pygame.image.load("img/target.png")
target_WIDTH = 50
target_HEIGHT = 50

target_x = random.randint(0, SCREEN_WIDTH - target_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - target_HEIGHT)

color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))


running = True

while running:

    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

pygame.quit()