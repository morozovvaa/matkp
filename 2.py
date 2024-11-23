import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Графические примитивы")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
black = (0, 0, 0)

# Настройка шрифта
font = pygame.font.Font(None, 36)

# Основной цикл
running = True
while running:
    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(white)

    # Рисование окружности
    pygame.draw.circle(screen, red, (width // 2, height // 2), 100, 5)  # Красная окружность с толщиной 5 пикселей

    # Рисование линии
    pygame.draw.line(screen, blue, (100, 50), (700, 50), 8)  # Синяя линия толщиной 8 пикселей

    # Рисование прямоугольника
    pygame.draw.rect(screen, green, (150, 400, 200, 100))  # Зеленый прямоугольник

    # Рисование многоугольника
    pygame.draw.polygon(screen, yellow, [(400, 300), (500, 200), (600, 300), (550, 400), (450, 400)])  # Желтый многоугольник

    # Добавление текста
    text = font.render("text", True, purple)
    screen.blit(text, (width // 2 - text.get_width() // 2, height - 100))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
sys.exit()
