﻿# 5 задача
# Проверить, делится ли введённое число на 10 или 15 и при этом не делится на 30.

n = int(input('\nВведите число: '))
if (n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('Число делится на 10 или 15 и не делится на 30')
else:
    print('Число не соответствует условию')