a = 2
res = '+' * (a != 2)
print(res)

# sp = ['rr', 'tt', 'tt', 'tt', 'tt']
# d = {}
# # заполнение словаря
# for i in sp:
#     d[i] = d.get(i, 0) + 1
#     print(list(d.keys()))
#     print(list(d.values()))
#     print(d.items())
# # перебор словаря
# for key, val in d.items():
#     print(key, val)
# # сортировка словаря по значениям (по убыванию)
# print(dict(sorted(d.items(), key=lambda x: -x[1])))

# Множества
# test_list = [1, 2, 3, 4, 2, 3, 4]
# print(test_list)  # [1, 2, 3, 4, 2, 3, 4]
# test_set = set(test_list)
# print(test_set)  # {1, 2, 3, 4}
# test_list = list(test_set)
# print(test_list)  # [1, 2, 3, 4]


# from Lecture02 import new_string
# import Lecture02

# print(Lecture02.new_string('Вау '))
# a = (3, 4)  # Кортеж
# print('a = {}'.format(a))
# print(f'type = {type(a)}')  # tuple
# print(f'a[0] = {a[0]}')
# print(f'a[-1] = {a[-1]}')
# # a[0] = 12  # Не работает, в отличие от списка, потому что кортеж - список неизменяемый

# t = (['red', 'green', 'blue'])  # Преобразуем список в кортеж
# rd, gn, bl = t  # Распаковываем кортеж в переменные
# print('r:{} g:{} b:{}'.format(rd, gn, bl))  # r:red g:green b:blue

# # Слэш позволяет осуществить перенос строки в коде, не прерывая его
# dictionary =\
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←

# for k in dictionary.keys():
#     print(k)  # Распечатывает все ключи словаря

# for k in dictionary.values():
#     print(k)  # Распечатывает все значения словаря

# # Кортежи
# tuple_list = ()
# list_beg = 1
# list_end = 6
# for i in range(list_beg, list_end):
#     tuple_list = tuple_list + (i, i**2)
# print(tuple_list)

# for i in range(0, len(tuple_list)):
#     if i % 2:
#         tuple_list = tuple_list + tuple_list[i:i+1]
# print(tuple_list)

# # Срез кортежа
# tuple_list = tuple_list[(list_end - list_beg) * 2:]
# print(tuple_list)

# СПИСОК кортежей
# tuple_listx = []
# for i in range(1, 6):
#     tuple_listx.append((i, i**2))
# print(f'tuple_listx = {tuple_listx}')
# print(tuple_listx[4])
# # (5, 25)
# # Обращение к элементу кортежа в списке кортежей
# print(tuple_listx)
# print(tuple_listx[3][1])  # Кортеж с индексом 3 (4, 16), элемент 1 (16)
# 16

# Словари
# from os import DirEntry


# dictionary =\
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→',
#         'солнышко': '☀',
#         'облако': '☁',
#         'зонтик': '☂'
#     }
# dictionary['PgUp'] = '☢'

# print(dictionary)
# for k in dictionary:
#     print(f'{k} = {dictionary[k]}')
