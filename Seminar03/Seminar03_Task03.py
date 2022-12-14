# Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime

from datetime import datetime

# ВАРИАНТ I
print('\nВАРИАНТ I')

time_r = datetime.now()  # Время в формате год-месяц-день час:мин:сек.мс
time_t = datetime.timestamp(time_r)  # Время в формате сек.мс
rand = time_t % 1  # Получаем случайное вещественное число в диапазоне [0;1)
# Получаем случайное целое число в диапазоне от 0 до 99
print(round(rand * 100))


# ВАРИАНТ II
print('ВАРИАНТ II')
# Определяем функцию, которая получает текущее время в миллисекундах
# и делим его на аргумент функции (100), получая случайное число в диапазоне от 0 до 99


def num_random(n):
    number = datetime.now().microsecond
    return number % n


print(num_random(100))
