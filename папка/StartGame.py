import random
from platforma import *

import pygame.font


def StartGame():
    # player = Girl()
    # а вот и музыка
    pygame.mixer.music.load('delta.wav')
    pygame.mixer.music.play(-1)

    Platform = Platforma()
    clock = pygame.time.Clock()
    Platform.generatePlatforms()
    display_width = 800
    display_height = 600
    score_last = 0
    background = (0, 255, 255)
    num = 1
    display = pygame.display.set_mode((display_width, display_height))  # создаём дисплей игры
    from Start import print_text
    show = True
    while show:
        display.fill(background)
        Platform.screen.blit(player.image, (player.playerx, player.playery - player.cameray))
        clock.tick(60)
        if num < 5:
            print_text('{} курс'.format(num), 250, 200, '#FF1493', 'шрифт.ttf', 100)
        else:
            print_text('Поздравляем, ', 100, 200, '#FF1493', 'шрифт.ttf', 50)
            print_text('вы окончили физтех!', 80, 300, '#FF1493', 'шрифт.ttf', 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # если нажали на крестик - программа закрывается
                pygame.quit()
                quit()
        if player.playery - player.cameray > 700:
            player.cameray = 0
            Platform.score = 0
            num = 1
            Platform.springs = []
            Platform.platforms = [[400, 500, 0, 0]]
            Platform.generatePlatforms()
            player.playerx = 400
            player.playery = 400
            score_last = 0
    
        Platform.drawPlatforms()
        player.updatePlayer()
        Platform.updatePlatforms()
        Platform.screen.blit(Platform.font.render(str(Platform.score), -1, (0, 0, 0)), (25, 25))
        if Platform.score - score_last > 5000:
            score_last = Platform.score
            background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            if num < 5:
                num += 1
        pygame.display.flip()


# StartGame()