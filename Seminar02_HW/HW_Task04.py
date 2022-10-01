# Задайте список из N элементов, заполненных числами из промежутка[-N, N]
# (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

# Открываем файл в двоичном формате, считываем две строки в переменные и закрываем файл
path = 'file.txt'
data = open(path, 'rb')
pos1 = data.readline()
pos2 = data.readline()
data.close()

# Обрезаем служебные символы перевода строки и возврата каретки (\r\n)
pos1 = int(pos1[0:-2])
pos2 = int(pos2[0:-2])

sequence = list()  # Создаём список
num_entered = int(input('Введите натуральное число: '))

# Генерируем последовательность из N чисел со случайными значениями в диапазоне [-N;N]
for i in range(num_entered):
    elem = num_entered - random.randint(0, 2 * num_entered)
    sequence.append(elem)
    # Печать элементов последовательности и их индексов
    print(f'i = {i}, elem = {elem}')

print(sequence)  # Печать всей последовательности
# Печать первого выбранного элемента
print(f'Position1 = {pos1}, Element1 = {sequence[pos1]}')
# Печать второго выбранного элемента
print(f'Position2 = {pos2}, Element2 = {sequence[pos2]}')
# Печать произведения выбранных элементов
print('Произведение = {}'.format(sequence[pos1] * sequence[pos2]))
