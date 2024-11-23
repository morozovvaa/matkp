import numpy as np
import pygame

# Исходная матрица треугольника
L = np.array([[5, 1],
              [5, 2],
              [3, 2]])

# Матрица масщтабирования
T = np.array([[2, 0],
              [0, 2]])

# Умножение для масштабирования
L_scaled = L * 80

# Преобразование треугольника
L_transformed = np.dot(L_scaled, T)

# Смещение треугольника в видимую область (например, на 300 пикселей вправо и вниз)
offset = np.array([-50, 200])
L_scaled_offset = L_scaled + offset
L_transformed_offset = L_transformed + offset

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Вращение треугольника")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(white)

    # Рисуем оси
    pygame.draw.line(screen, (0, 0, 0), (width // 2, 0), (width // 2, height), 2)  # вертикальная ось
    pygame.draw.line(screen, (0, 0, 0), (0, height // 2), (width, height // 2), 2)  # горизонтальная ось

    # Функция для отрисовки треугольника
    def draw_triangle(points, color):
        pygame.draw.polygon(screen, color,
                            [(int(points[i, 0]), int(height - points[i, 1])) for i in range(3)], 2)

    # Рисуем исходный треугольник
    draw_triangle(L_scaled_offset, red)

    # Рисуем преобразованный треугольник
    draw_triangle(L_transformed_offset, blue)

    # Обновление экрана
    pygame.display.flip()

# Закрытие Pygame
pygame.quit()