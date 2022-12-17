import pygame
pygame.init()

display_width = 800
display_height = 600
FPS = 60


display=pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("doodlejump") # пишем заголовок вкладки
icon = pygame.display.set_icon(pygame.image.load('Лого_МФТИ.png')) # Загружаем иконку

from platform import *

Platform = Platforma()
clock = pygame.time.Clock()
Platform.generatePlatforms()
running = True
show = True
while show:
    display.fill((67, 134, 120))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если нажали на крестик - программа закрывается
            pygame.quit()
            quit()
    if player.playery - player.cameray > 700:
        player.cameray = 0
        Platform.score = 0
        Platform.springs = []
        Platform.platforms = [[400, 500, 0, 0]]
        Platform.generatePlatforms()
        player.playerx = 400
        player.playery = 400

    Platform.drawPlatforms()
    player.updatePlayer()
    Platform.updatePlatforms()
    Platform.screen.blit(Platform.font.render(str(Platform.score), -1, (0, 0, 0)), (25, 25))
    pygame.display.flip()


