import pygame
pygame.init()

display_width=800
display_height=600
FPS=60

clock = pygame.time.Clock()

display=pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("doodlejump") # пишем заголовок вкладки
icon = pygame.display.set_icon(pygame.image.load('Лого_МФТИ.png')) # Загружаем иконку
# Переменные
jumper=pygame.image.load('василий.com.png')
button_sound = pygame.mixer.Sound('кнопка.wav')

# создадим кнопку play
class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (124,24,233)
        self.active_color = (255, 255, 255)
    def draw (self, x, y, message, action = None):
        mouse = pygame.mouse.get_pos() # положение курсора мыши, которая несёт значения x и y
        click = pygame.mouse.get_pressed() # click[0] - левая кнопка мыши, click[1] - правая кнопка мыши
        if x < mouse [0] < x + self.width: # если курсор мыши попал на кнопку
            if y < mouse [1] < y + self.height:
                # т.е., если курсор мыши попал на кнопку, меняем ей цвет
                pygame.draw.rect(display, self.inactive_color,(x, y, self.width, self.height))

                if click[0] == 1: # польхзователь нажал на левую кнопку мыши
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300) # задержка, чтобы звук не звучал несколько раз
                    if action is not None: # если клавиша нажата
                        action ()
        else:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))

        print_text(message,x + 10, y + 7)


def print_text(message, x, y, font_color = (56, 56, 56), font_type = 'шрифт.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit (text, (x,y))


def run_game():
    game = True
    button = Button(125, 50)
    while game:
        button.draw(300, 250, "играть")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

run_game()
pygame.display.flip()


# while True:
#     button.draw(300, 250, "играть")
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit() # завершает работу модуля Pygame
#             quit() # выходим из цикла
#     clock.tick(FPS)
