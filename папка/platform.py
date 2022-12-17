import pygame



if type_player == 'Girl':
    player = Girl()
else:
    player = Boy()


class Bakalavr:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.green = pygame.draw.rect([400,500,40,40] )



