# Игра \Тир\
import pygame
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

target_icon = pygame.image.load("img/")
target_WIDTH = 50
target_HEIGHT = 50

running = True

while running:
    pass
pygame.quit()