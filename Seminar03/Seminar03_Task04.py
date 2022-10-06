﻿# Задайте список.
# Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# Входные данные     Выходные данные
# 12                 да
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка

# Функция: Есть ли в списке строк элемент, содержащий подстроку f_line
def if_inlist(f_line):
    for item in init_list:  # Перебираем элементы списка
        if f_line in item:  # Если втекущем элементе есть искомое
            return 'Да'  # Функция возвращает 'Да'
    return 'Нет'  # Если перебор ничего не нашел, то функция возвращает 'Нет'


# Список строк
init_list = \
    {
        'Строка1',
        'Строка2',
        'Строка3',
        'Строка45',
        'Стр12ка'
    }

print(if_inlist('12'))  # Вызываем функцию с искомой подстрокой ('12')
