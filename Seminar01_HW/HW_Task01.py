﻿# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
#     ◦ 6 -> да
#     ◦ 7 -> да
#     ◦ 1 -> нет

week_day_number = int(input('Введите порядковый номер дня недели: '))
while ((week_day_number < 1) or (week_day_number > 7)):
    print('С таким номером не бывает дней недели')
    print('Введите число от 1 до 7 включительно')
    week_day_number = int(input('Введите порядковый номер дня недели: '))
if 5 < week_day_number < 8:
    print('Да у нас тут выходной !')
elif week_day_number == 5:
    print('Сегодня пятница, а завтра - выходной !')
else:
    print('У-у, до выходных ещё работать и работать')
