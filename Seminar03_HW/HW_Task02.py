# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#  [2, 3, 4, 5, 6] => [12, 15, 16];
#  [2, 3, 5, 6] => [12, 15]

lst = [int(i)
       for i in input('Введите последовательность через пробел:\n').split()]
# lst = [2, 3, 4, 5, 6]
# lst = [2, 3, 5, 6]

lst_mul = list()  # Создаём список произведений пар чисел
for i in range(0, (len(lst) // 2) + (len(lst) % 2)):  # Перебор до середины списка
    lst_mul.append(lst[i] * lst[-(i+1)])  # Заносим произведение в список
print(
    f'{lst_mul} - последовательность произведений пар чисел списка')
