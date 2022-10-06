﻿# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 3, 5, 9, 3]
lst = [int(i) for i in input('Введите числа через пробел: \n').split()]
summ = 0  # Задаём начальное значение суммы
for i in range(0, len(lst)):  # Перебираем элементы списка по индексу
    if i % 2:  # Если индекс нечётный,
        summ += lst[i]  # то добавляем элемент в сумму
print('Сумма элементов списка с нечётным индексом = {}'.format(summ))