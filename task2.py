import random

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def is_inside(a, b, x, y):
    is_inside = (a <= x and x <= b) and (0 <= y and y <= f(x))
    return (a <= x and x <= b) and (0 <= y and y <= f(x))

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_diff = 0

    # Опишемо область визначення для y
    y_min = a
    y_max = f(b)

    for _ in range(num_experiments):
        points = [(random.uniform(a, b), random.uniform(y_min, y_max)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)

        # В даному випадку b та y_max формують прямокутник, площу якого ми використовуємо, де b-a - одне ребро, а y_max - друге.
        diff = (M / N) * ((b-a) * y_max)

        # Додавання до середньої площі
        average_diff += diff

    # Обчислення середньої площі
    average_diff /= num_experiments
    return average_diff

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

# Кількість експериментів
num_experiments = 100

# Виконання симуляції
result = monte_carlo_simulation(a, b, num_experiments)

print(result)