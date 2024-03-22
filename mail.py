# Игра \Тир\
import pygame
# образуем тело цикла всей игры
pygame.init()

# организация поля игры с использованием pygame.disply константы высоты и ширины
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# создою названия окна программы
pygame.display.set_caption("Игра Тир")

# создаю переменую. которая подгружает иконку игры
icon = pygame.image.load("")


running = True

while running:
    pass
pygame.quit()