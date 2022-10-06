# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#         ◦ [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def num_random(min, max):  # Генератор случайных чисел
    return round(random.uniform(min, max), 2)


real_list = list()  # Объявляем список вещественных чисел

real_length = 10  # Длина списка вещественных чисел

rand_min = 10  # Минимум случайного числа
rand_max = 100  # Максимум случайного числа

# Заполняем список случайных чисел, генерируя их в функции num_random
for i in range(real_length):
    real_list.append(num_random(rand_min, rand_max))

# real_list = [1.1, 1.2, 3.1, 5, 10.01]  # Список из примера в условии

print(real_list)  # Печать списка вещественных чисел

# Поиск минимального и максимального значений дробных частей списка
min = round(real_list[0] % 1, 2)  # Начальное мин. значение дробной части
max = round(real_list[0] % 1, 2)  # Начальное макс. значение дробной части

for item in real_list:
    if round(item % 1, 2) != 0:  # Исключаем числа без дробной части
        if item % 1 < min:
            min = round(item % 1, 2)
        if item % 1 > max:
            max = round(item % 1, 2)
print(min)
print(max)
print(round(max - min, 2))
