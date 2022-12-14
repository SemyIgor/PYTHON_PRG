# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель(НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные           # Выходные данные
# 36                       # 6
# 12
# 144
# 18

from math import gcd


nums = []  # Список для вводимых чисел
in_num = '0'  # Непустая строка
print('\nВведите число:')
while in_num != '':  # Продолжать, пока не введена пустая строка
    in_num = input()  # Вводим очередное число
    if in_num != '' and in_num.isdigit():  # Если не пустая строка и число,
        nums.append(int(in_num))  # то добавляем число в список

nod = nums[0]
for num in nums:
    nod = gcd(nod, num)
print(f'NOD = {nod}')
