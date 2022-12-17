import pygame
pygame.init()
#  некоторые параметры
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
while True:
    .screen.fill((255, 255, 255))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    if self.playery - self.cameray > 700:
        self.cameray = 0
        self.score = 0
        self.springs = []
        self.platforms = [[400, 500, 0, 0]]
        self.generatePlatforms()
        self.playerx = 400
        self.playery = 400
    self.drawGrid()
    self.drawPlatforms()
    self.updatePlayer()
    self.updatePlatforms()
    self.screen.blit(self.font.render(str(self.score), -1, (0, 0, 0)), (25, 25))
    pygame.display.flip()


