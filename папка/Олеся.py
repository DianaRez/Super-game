import pygame
pygame.init()

display_width=800
display_height=600
FPS=60

clock = pygame.time.Clock()

display=pygame.display.set_mode((display_width, display_height)) # создаём дисплей игры
pygame.display.set_caption("doodlejump") # пишем заголовок вкладки
icon = pygame.display.set_icon(pygame.image.load('Лого_МФТИ.png')) # Загружаем иконку
display.fill([105, 196, 205])
menu1_back = pygame.image.load('космос.jpg')
display.blit(menu1_back, (-400, 0))
pygame.display.update()
# Переменные
jumper=pygame.image.load('василий.com.png')
button_sound = pygame.mixer.Sound('кнопка.wav')

# создадим кнопку play
class Button:
    def __init__(self, width, height):
        self.width = width # ширина кнопки
        self.height = height # длина
        self.active_color = (124,24,233) # цвет ненажатой кнопки
        self.inactive_color = (255, 255, 255) # цвет нажатой
    def draw (self, x, y, message, action = None, font_size = 30): #принимает размеры кнопки (x и y), надпись и  её размер
        mouse = pygame.mouse.get_pos() # положение курсора мыши, которая несёт значения x и y
        click = pygame.mouse.get_pressed() # click[0] - левая кнопка мыши, click[1] - правая кнопка мыши
        if x < mouse [0] < x + self.width and y < mouse [1] < y + self.height: # если курсор мыши попал на кнопку
            # меняем ей цвет
            pygame.draw.rect(display, self.active_color,(x, y, self.width, self.height))
            if click[0] == 1: # польхзователь нажал на левую кнопку мыши
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)# задержка, чтобы звук не звучал несколько раз
                if action is not None: # если клавиша нажата
                    start_game ()

        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height)) # когда курсор вне кнопки, она начального цвета

        print_text(message = message,x = x + 13, y = y + 10, font_size = font_size) # печатаем текст на кнопке


def print_text(message, x, y, font_color = (56, 56, 56), font_type = 'шрифт.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit (text, (x,y))
def start_game():
    display.blit(menu1_back, (-4000, 0))
    display.fill ([105,196,205])
    menu_back = pygame.image.load('солнце.png')
    display.blit(menu_back, (500, 20))
    pygame.display.update()

def show_menu():
    menu_back = pygame.image.load('василий.com.png') # загружаем фон
    start_button = Button (210,70)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # если нажали на крестик - программа закрывается
                pygame.quit()
                quit()
        display.blit(menu_back, (0, 0)) # отображаем фон на дисплее
        start_button.draw(300, 200, 'Start game', start_game) # рисуем кнопку старта
        pygame.display.update() #обновляем дисплей
        clock.tick(60) # создаём задержку

# def run_game():
#     game = True
#     button = Button(125, 50) # Создаём экземляр класса с такими размерами
#     while game:
#         button.draw(300, 250, "играть")
#         pygame.display.flip()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
# run_game()
show_menu()

