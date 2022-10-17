﻿# Задача №02 из Домашнего задания Семинара №03
# =============================
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#  [2, 3, 4, 5, 6] => [12, 15, 16];
#  [2, 3, 5, 6] => [12, 15]

lst = [int(i)
       for i in input('Введите последовательность через пробел:\n').split()]
# lst = [2, 3, 4, 5, 6]
# lst = [2, 3, 5, 6]

# Применяем zip() к списку и его развёрнутой копией, с помощью map() перемножаем элементы
# полученных кортежей, формируя удвоенный список произведений пар чисел.
res = list(map(lambda i: (i[0] * i[1]), zip(lst, reversed(lst))))

# С помощью метода List Comprehension избавляемся от дубляжа
result = [res[i] for i in range((len(res) // 2) + (len(res) % 2))]
print(result)
