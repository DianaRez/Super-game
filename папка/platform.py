import pygame
import random


from Players import*
type_player = 'Boy'

if type_player == 'Girl':
    player = Girl()
else:
    player = Boy()


class Platforma:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

        pygame.font.init()
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 25)
        self.green = pygame.image.load("халява.png").convert_alpha()
        self.blue = pygame.image.load("матан.png").convert_alpha()
        self.red = pygame.image.load("химия.png").convert_alpha()
        self.red_1 = pygame.image.load("химия_разорванная.png").convert_alpha()

        self.spring = pygame.image.load("spring.png").convert_alpha()

        self.platforms = [[400, 500, 0, 0]]
        self.springs = []

    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], 70 - 10, 10)  # 70-10 это ширина минус 10, 10 это высота
            gamer = pygame.Rect(player.playerx, player.playery, player.image.get_width() - 10,
                                player.image.get_height())  # узнать размеры картинок игроков
            if rect.colliderect(gamer) and player.gravity and player.playery < (
                    p[1] - player.cameray):  # проверяем пересечение игрока и платформы

                if p[2] != 2:  # если не красная
                    player.jump = 15
                    player.gravity = 0
                else:  # если все таки красная
                    p[-1] = 1  # ломаемся

            if p[2] == 1:  # если синяя
                if p[-1] == 1:
                    p[0] += 5  # движемся вправо
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[-1] = 1

    def drawPlatforms(self):
        for p in self.platforms:
            check = self.platforms[1][1] - player.cameray
            if check > 600:
                platform = random.randint(0, 1000)
                if platform < 800:
                    platform = 0 # зеленая
                elif platform < 900:
                    platform = 1 # синяя
                else:
                    platform = 2 # красная

                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, platform, 0])
                coords = self.platforms[-1] #верхняя платформа
                check = random.randint(0, 1000)
                if check > 900 and platform == 0:
                    self.springs.append([coords[0], coords[1] - 25]) #добавляем пружинку на верхнюю платформу
                self.platforms.pop(0) #удаляем нижнюю платформу
                self.score += 100

            if p[2] == 0:
                self.screen.blit(self.green, (p[0], p[1] - player.cameray))
            elif p[2] == 1:
                 self.screen.blit(self.blue, (p[0], p[1] - player.cameray))
            elif p[2] == 2:
                 if not p[3]:
                     self.screen.blit(self.red, (p[0], p[1] - player.cameray)) #целая
                 else:
                     self.screen.blit(self.red_1, (p[0], p[1] - player.cameray)) # ломается

        for spring in self.springs:
            self.screen.blit(self.spring, (spring[0], spring[1] - player.cameray))

            if pygame.Rect(spring[0], spring[1], self.spring.get_width(), self.spring.get_height()).colliderect(
                    pygame.Rect(player.playerx, player.playery, player.image.get_width(),
                                player.image.get_height())):
                player.jump = 50
                player.cameray -= 50

    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            if platform < 800:
                platform = 0
            elif platform < 900:
                platform = 1
            else:
                platform = 2
            self.platforms.append([x, on, platform, 0])
            on -= 50
