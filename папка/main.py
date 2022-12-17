import pygame
pygame.init()
#  некоторые параметры
display_width=800
display_height=600
FPS=60
clock = pygame.time.Clock()

display=pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("doodlejump") # пишем заголовок вкладки
icon = pygame.display.set_icon(pygame.image.load('Лого_МФТИ.png')) # Загружаем иконку

from platform import *

