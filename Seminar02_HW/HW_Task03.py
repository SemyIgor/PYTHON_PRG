# Задайте список из n чисел последовательности  выведите на экран их сумму.

sequence = list()  # Создаём список
summ = 0
num_entered = int(input('Введите натуральное число: '))
for elem_index in range(1, num_entered + 1):
    elem_value = round((1 + 1 / (elem_index))**(elem_index), 4)
    sequence.append(elem_value)  # Добавляем элемент в последовательность
    summ += elem_value  # Добавляем элемент в сумму

print('Последовательность: {}'.format(sequence))
print('Сумма = {:.4f}'.format(summ))
