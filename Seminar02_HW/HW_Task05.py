﻿# Реализуйте алгоритм перемешивания списка.

import random

# Исходный список
agenda = ['фурыч', 'глюк', 'нинзя', 'свинт', 'гичата', 'сюкр']
# Новый список с пустыми ('') элементами
shuffled = [''] * len(agenda)

print('\nИсходный список')
print(agenda)

# Генерируем случайным образом индекс нового списка, по которому будем заносить первый элемент исходного списка
j = random.randint(0, len(agenda) - 1)
for item in agenda:  # По порядку пробегаем все элементы исходного списка, находя случайным образом для них место в новом списке
    while shuffled[j] != '':  # Пока не найдём свободное место в новом списке
        # Генерируем индекс для нового списка и в цикле проверяем, свободно ли место по этому индексу
        j = random.randint(0, len(agenda) - 1)
    # Заносим очередной элемент исходного списка в найденное место нового списка
    shuffled[j] = item

print('Перемешанный список')
print(shuffled)
