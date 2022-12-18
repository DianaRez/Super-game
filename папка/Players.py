import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.playerx = 400
        self.playery = 400
        self.cameray = 0
        self.jump = 0
        self.gravity = 0
        self.xmovement = 0

    def updatePlayer(self):
#если нет сигнала прыгать, падает вниз под действием гравитации
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1

#управление кнопками

        key = pygame.key.get_pressed()

        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1

        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1

        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
# если игрок ушёл за правую сторону экрана, он вернётся по левую и наоборот
        if self.playerx > 850:
            self.playerx = -50

        elif self.playerx < -50:
            self.playerx = 850

        self.playerx += self.xmovement

#если игрок находится выше чем половина экрана, то фон сдвигается на 10
        if self.playery - self.cameray <= 300:
            self.cameray -= 10

# делаем два игрока
class Boy(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("boy.png"), (100, 100))

class Girl(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("girl.png"), (100, 100))


