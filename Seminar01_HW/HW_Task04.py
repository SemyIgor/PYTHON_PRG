# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти(x и y).

ch = input('Введите номер четверти координатной плоскости: ')

if ch == '1':
    print('Четверть I, x > 0, y > 0')
elif ch == '2':
    print('Четверть II, x < 0, y > 0')
elif ch == '3':
    print('Четверть III, x < 0, y < 0')
elif ch == '4':
    print('Четверть IV, x > 0, y < 0')
else:
    print('Четверти с номером {} не существует'.format(ch))
