# 2 задача (1 вариант)
# находим максимальное число из пяти введённых последовательным сравнением
print('2 задача, 1 вариант')
m = int(input('Вводите числа: \n'))  # Вводим первое число
for i in range(4):
    x = int(input())  # Вводим остальные числа
    if x > m:
        m = x
print('Максимальное число = {}'.format(m))
