# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re


def str_to_num_list(s):  # Функция выбора чисел из строки
    nums = re.findall(r'\d+', s)
    nums = [int(i) for i in nums]
    return nums


def poly_sum(a, b):  # Складываем индексы двух полиномов
    l, s = ((a, b), (b, a))[len(a) < len(b)]  # l - long list, s - short list
    # Складываем списки
    sum_list = ([l[i] + s[i] if abs(i) < len(s)+1 else l[i] +
                 0 for i in range(-1, -len(l)-1, -1)])
    sum_list.reverse()  # "Разворачиваем" результат
    return sum_list


def poly_tup(nums):  # Из индексов кортежи
    print(len(nums))
    poly_form = []
    for i in range(-len(nums), -1, 2):
        poly_form.append((nums[i], nums[i+1]))
    return poly_form


def del_garb(num_list):  # Удаляем лишние числа
    lim = len(num_list) // 2
    for i in range(1, lim):
        del num_list[i]
    del num_list[-1]


# Из первого файла считали первый полином
first_fil = open('S04_HW_Task05-1.txt', 'r', encoding='utf-8-sig')
first_poly_str = first_fil.readlines()[0]  # Сразу в строку
first_fil.close()

# Из второго файла считали второй полином
second_fil = open('S04_HW_Task05-2.txt', 'r', encoding='utf-8-sig')
second_poly_str = second_fil.readlines()[0]  # Сразу в строку
second_fil.close()

# Получаем список коэффициентов первого полинома
first_num_list = str_to_num_list(first_poly_str)
print(first_num_list)

# Получаем список коэффициентов второго полинома
second_num_list = str_to_num_list(second_poly_str)
print(second_num_list)

# Складываем полиномы, получая список коэффициентов третьего полинома
third_num_list = poly_sum(first_num_list, second_num_list)
print(third_num_list)

# Удаляем показатели степени и ноль правой части полинома
del_garb(third_num_list)
print(third_num_list)

# Создаём список кортежей индексов полинома
tup_list = []
pow_of_poly = len(third_num_list) - 1

for i in range(0, len(third_num_list)):
    tup_list.append((third_num_list[i], pow_of_poly - i))


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
poly_file = open('S04_HW_Task05-3.txt', 'a')
poly_file.writelines(line_of_poly + '\n')
poly_file.close()
