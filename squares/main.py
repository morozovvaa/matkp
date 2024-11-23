import pygame
import numpy as np
import sys
from graphics import Unit, Origin, ReferenceFrame, Drawer
from transform import translate, scale, rotate

# Константы
RES_X, RES_Y = 800, 600
SCALE = 0.9  # Коэффициент масштабирования
ANGLE = np.pi / 32  # Угол поворота (π/32)
ITERATIONS = 20  # Количество итераций трансформаций

# Начальные координаты квадрата
square = np.array([
    [2, -2, 1],
    [-2, -2, 1],
    [-2, 2, 1],
    [2, 2, 1]
])

# Единичный размер и начало координат
unit = Unit(100)  # Каждая единица равна 100 пикселям
origin = Origin(RES_X / 2, RES_Y / 2)
rf = ReferenceFrame(origin, unit, unit)

# Drawer для рисования
drawer = Drawer(RES_X, RES_Y, rf)
drawer.initialize("Square Transformation")

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    drawer.screen.fill((0, 0, 0))

    # Нарисовать оси
    # drawer.color = (255, 255, 255)
    # drawer.draw_axes(-5, 5, -5, 5)

    # Рисовать все итерации
    current_square = square.copy()
    for i in range(ITERATIONS + 1):
        # Преобразование: масштабирование и поворот относительно центра
        transform = (
            translate(-origin.x0 / unit.pixels, -origin.y0 / unit.pixels) @  # Сдвиг к центру
            scale(SCALE, SCALE) @  # Масштабирование
            rotate(ANGLE) @  # Поворот
            translate(origin.x0 / unit.pixels, origin.y0 / unit.pixels)  # Возврат к центру
        )

        # Цвет квадрата зависит от итерации
        drawer.color = (255 - i * 10, 0, i * 12)

        # Нарисовать квадрат
        drawer.draw_polygon(current_square)

        # Применить трансформацию для следующей итерации
        current_square = current_square @ transform.T

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Завершение Pygame
pygame.quit()
sys.exit()
