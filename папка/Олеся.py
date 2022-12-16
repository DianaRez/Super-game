import pygame
pygame.init()
display_width=700
display_height=600
FPS=60
clock = pygame.time.Clock()
display=pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("doodlejump") # пишем заголовок вкладки
icon = pygame.image.load('Лого_МФТИ.png') # Загружаем иконку
pygame.display.set_icon(icon) # ставим иконку
jumper=pygame.image.load('василий.com.png')