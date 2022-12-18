import pygame
pygame.init()
#  некоторые параметры
display_width = 800
display_height = 600
FPS = 60
clock = pygame.time.Clock()

display = pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("SuperPhystech") # пишем заголовок вкладки
icon = pygame.display.set_icon(pygame.image.load('Лого_МФТИ.png')) # Загружаем иконку

# Переменные
girl = pygame.image.load('girl.png')
Girl1 = pygame.transform.scale(girl, (girl.get_width() // 2,girl.get_height() // 2))
boy = pygame.image.load('boy.png')
Boy1 = pygame.transform.scale(boy, (boy.get_width() // 2, boy.get_height() // 2))
menu1_back = pygame.image.load('космос.jpg')
menu2_back = pygame.image.load('василий.com.png')
display.blit(menu1_back, (-400,0))
display.blit(menu2_back, (0, 0))
# button_sound = pygame.mixer.Sound('кнопка.wav')
button_sound = pygame.mixer.Sound('клик.wav')
# создадим кнопку play
class Button:
    def __init__(self, width, height):
        self.width = width # ширина кнопки
        self.height = height # длина
        self.active_color = (124,24,233) # цвет ненажатой кнопки
        self.inactive_color = (255, 255, 255) # цвет нажатой
    def draw (self, x, y, message, action = None, font_size = 30): #принимает размеры кнопки (x и y), надпись и  её размер, звук нажатия
        mouse = pygame.mouse.get_pos() # положение курсора мыши, которая несёт значения x и y
        click = pygame.mouse.get_pressed() # click[0] - левая кнопка мыши, click[1] - правая кнопка мыши
        if x < mouse [0] < x + self.width and y < mouse [1] < y + self.height: # если курсор мыши попал на кнопку
            # меняем ей цвет
            pygame.draw.rect(display, self.active_color,(x, y, self.width, self.height))
            if click[0] == 1: # польхзователь нажал на левую кнопку мыши
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)# задержка, чтобы звук не звучал несколько раз
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    if action == func1:
                        func1()
                    if action == func2:
                        func2()
                    action()


        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height)) # когда курсор вне кнопки, она начального цвета

        print_text(message = message,x = x + 13, y = y + 10, font_size = font_size) # печатаем текст на кнопке

# создадим функцию, печатующую текст : func (текст, координата x, y, цвет шрифта, его тип, его размер)
def print_text(message, x, y, font_color = (56, 56, 56), font_type = 'шрифт.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size) #создаёт новый объект Font из файла
    text = font_type.render(message, True, font_color) #Вторым аргументом указывается сглаживание, третьим – цвет текста
    display.blit (text, (x,y)) # выводим на экран в месте с координатами x и y


from StartGame import *
from platforma import *

def func1():
    player.h()
    StartGame()
def func2():
    player.g()
    StartGame()

def choose_your_fighter():
    show_game = True
    hero1_button = Button (120,70)
    hero2_button = Button (150, 70)
    while show_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # если нажали на крестик - программа закрывается
                pygame.quit()
                quit()
        display.fill((176, 224, 230))
        display.blit(Girl1, (100,130))
        display.blit(Boy1, (450,130))
        hero1_button.draw(100, 450, "Ботан", func1)  # рисуем кнопку старта
        hero2_button.draw(500, 450, 'раздолб', func2)
        pygame.display.update()  # обновляем дисплей
        clock.tick(60)  # создаём задержку


def show_menu():

    start_button = Button (210,65)
    quit_button = Button (90, 65)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # если нажали на крестик - программа закрывается
                pygame.quit()
                quit()

        start_button.draw(300, 200, 'Start game', choose_your_fighter)# рисуем кнопку старта
        quit_button.draw(360, 360, 'Quit', quit)
        pygame.display.update() #обновляем дисплей
        clock.tick(60) # создаём задержку

show_menu()
pygame.quit()
quit()