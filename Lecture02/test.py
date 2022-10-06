# from Lecture02 import new_string
# import Lecture02

# print(Lecture02.new_string('Вау '))
a = (3, 4)  # Кортеж
print('a = {}'.format(a))
print(f'type = {type(a)}')  # tuple
print(f'a[0] = {a[0]}')
print(f'a[-1] = {a[-1]}')
# a[0] = 12  # Не работает, в отличие от списка, потому что кортеж - список неизменяемый

t = (['red', 'green', 'blue'])  # Преобразуем список в кортеж
rd, gn, bl = t  # Распаковываем кортеж в переменные
print('r:{} g:{} b:{}'.format(rd, gn, bl))  # r:red g:green b:blue

# Слэш позволяет осуществить перенос строки в коде, не прерывая его
dictionary =\
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])  # ←

for k in dictionary.keys():
    print(k)  # Распечатывает все ключи словаря

for k in dictionary.values():
    print(k)  # Распечатывает все значения словаря
