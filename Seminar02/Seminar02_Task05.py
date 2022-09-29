﻿# Удалить вторую цифру трёхзначного числа.
# Делаем программу, которая работает с любым натуральным числом, имеющим вторую цифру

# ВАРИАНТ I
# Фиксированная разрядность вводимого числа с её проверкой
# n = None
# input_num_length = 3  # Устанавливаем разрядность исходного числа
# while n != input_num_length:  # Проверяем разрядность вводимого числа
#     print(f'Введите {input_num_length}-значное число: ')
#     str_num = input()
#     n = len(str_num)  # Определяем разрядность введённого числа
# num = int(str_num)  # Строку в число
# # Убираем вторую цифру введённого числа
# res = (num // (10 ** (n-1))) * (10 ** (n-2)) + (num % (10 ** (n-2)))
# print(res)

# ВАРИАНТ II
# Убирает вторую цифру любого натурального числа, у которого она есть

print('Введите число: ')
str_num = input()
n = len(str_num)  # Определяем разрядность введённого числа
num = int(str_num)  # Строку в число
# Убираем вторую цифру введённого числа
res = (num // (10 ** (n-1))) * (10 ** (n-2)) + (num % (10 ** (n-2)))
print(res)
