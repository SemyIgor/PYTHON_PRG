# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# ◦ k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def get_random_int(min, max):  # Генератор случайных целых чисел
    return random.randint(min, max)


minn = -100
maxx = 100

pow_of_poly = int(input('Введите степень многочлена: '))

tup_list = []  # Список кортежей в виде: (коэффициент, показатель степени x)

# Заполняем список кортежей, где коэффициент - случайное целое от -100 до 100
for i in range(0, pow_of_poly + 1):
    tup_list.append((get_random_int(minn, maxx), pow_of_poly - i))
print(tup_list)

# Создаём строку полинома для записи в файл
line_of_poly = ' = 0'  # Начинаем формировать строку полинома
for i in range(pow_of_poly, -1, -1):
    k, p = tup_list[i]  # Извлекаем очередной кортеж из списка в переменные
    # Минус если k<0, плюс если k>0, если самый первый k>0, то знак не ставим
    sign = '-' if k < 0 else '+' * (i != 0)  # знак коэффициента
   #  modul = abs(k)  # Модуль очередного коэффициента
    pow_r = 'x^' + str(p)  # Строка 'x в степени p'
    if pow_r == 'x^1':  # исключаем x в степени 1
        pow_r = 'x'
    elif pow_r == 'x^0':  # исключаем x в степени 0
        pow_r = ''
    # Формируем строку полинома
    line_of_poly = f'{sign} {abs(k)}{pow_r} ' + line_of_poly

# Записываем полином в файл
poly_file = open('S04_HW_Task04.txt', 'a')
poly_file.writelines(line_of_poly + '\n')
poly_file.close()

print(line_of_poly)
