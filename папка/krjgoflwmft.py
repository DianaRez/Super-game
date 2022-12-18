import random
from platform import *

def StartGame():
    # player = Girl()
    

    Platform = Platforma()
    clock = pygame.time.Clock()
    Platform.generatePlatforms()
    display_width = 800
    display_height = 600
    score_last = 0
    background = (67, 134, 120)
    display = pygame.display.set_mode((display_width, display_height))  # создаём дисплей игры
    show = True
    while show:
        display.fill(background)
        Platform.screen.blit(player.image, (player.playerx, player.playery - player.cameray))
        clock.tick(60)
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
            score_last = 0
    
        Platform.drawPlatforms()
        player.updatePlayer()
        Platform.updatePlatforms()
        Platform.screen.blit(Platform.font.render(str(Platform.score), -1, (0, 0, 0)), (25, 25))
        if Platform.score - score_last > 1000:
            score_last = Platform.score
            background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        pygame.display.flip()


# StartGame()