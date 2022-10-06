# Данные, функции и модули в Python
# КАК РАБОТАТЬ С ФАЙЛАМИ
# 1. Связать файловую переменную с файлом, определив модификатор работы:
#    - a - открытие для добавления данных (если файл не существует, то будет создан)
#    - r - открытие для чтения данных (если файл не существует, то будет ошибка)
#    - w - открытие для записи данных (поверх существующих, если файл не существует, то создаётся)
#    - w+ - открытие для записи с возможностью чтения (если файла не будет, то он создаётся)
#    - r+ - открытие для чтения с возможностью записи (если файла не будет, то будет ошибка)

# Первый вариант записи в файл


colors = ['red', ' ', 'green', ' ', 'blue']
data = open('Lecture02.txt', 'w')
data.writelines(colors)  # разделителей не будет
for i in range(5):
    data.write(f'\n{str(i)}')
data.close()

# Второй вариант записи в файл, не требуется close()
# (соединение с файлом завершается автоматически после выполнения блока with)
with open('Lecture02.txt', 'a') as col_data:
    col_data.write('\nFirst Line Added\n')
    col_data.write('Second Line Added\n')

# Чтение из файла и вывод на печать
summ = 0
path = 'Lecture02.txt'
data = open(path, 'r')
for li_ne in data:
    print(li_ne)
    try:
        summ += int(li_ne)
    except ValueError:
        summ = summ
    #  if li_ne.isdigit():
    #      summ += int(li_ne)
data.close()
print(summ)


def new_string(symbol, count=3):
    return(symbol * count)


a = (3, 4)  # Кортеж
print('a = {}'.format(a))
print(f'type = {type(a)}')  # tuple
print(f'a[0] = {a[0]}')
print(f'a[-1] = {a[-1]}')
# a[0] = 12  # Не работает, в отличие от списка, потому что кортеж - список неизменяемый

t = (['red', 'green', 'blue'])  # Преобразуем список в кортеж
rd, gn, bl = t  # Распаковываем кортеж в переменные
print('r:{} g:{} b:{}'.format(rd, gn, bl))  # r:red g:green b:blue

# СЛОВАРИ

# Типы ключей могут различаться
dictionary = {}
dictionary =\
    {
        'up': '↑',
        2: '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['up'])  # ↑
print(dictionary[2])  # ←

print('\n')
for k in dictionary.keys():
    print(k)  # Распечатываем ключи словаря

print('\n')
for k in dictionary:
    print(k)  # Распечатываем ключи словаря

print('\n')
for k in dictionary.values():
    print(k)  # Распечатываем элементы словаря

print('\n')
for v in dictionary:
    print(dictionary[v])  # Распечатываем элементы словаря

del dictionary['right']  # Удаляем элемент по ключу 'right'
print(dictionary)

dictionary['right'] = '→'  # Добавляем элемент по ключу 'right'
print(dictionary)

print('\n')
for item in dictionary:
    # Печатаем ключ и значение элемента:
    print('{}: {}'.format(item, dictionary[item]))

# МНОЖЕСТВА

print('\n')
colors = {'red', 'green', 'blue'}
print(type(colors))  # <class 'set'>
print(colors)  # {'blue', 'green', 'red'}

colors.add('red')  # Такой элемент есть, поэтому ничего не изменится
print(colors)  # {'blue', 'green', 'red'}

colors.add('grey')  # Добавляем элемент
print(colors)  # {'blue', 'green', 'red', 'grey'}

colors.remove('red')  # Удаляем элемент
print(colors)  # {'blue', 'green', 'grey'}

# colors.remove('red')  # KeyError: 'red' Удаление несуществующего элемента
# Удаляет элемент, если он есть, не выводит ошибку, если его нет
colors.discard('red')

colors.clear()  # {}
print(colors)  # set()

# К множествам можно применять объединение, пересечение и пр. по теории множеств
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1,2,3,5,8,13,21}
i = a.intersection(b)  # i = {2, 5, 8}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}

q = a\
    .union(b)\
    .difference(a.intersection(b))  # {1,21,3,13}

print(q)

# НЕИЗМЕНЯЕМЫЕ МНОЖЕСТВА

# Никакие действия с добавлением или удалением элементов не действуют на s
s = frozenset(a)

# СПИСКИ

list1 = [1, 2, 3, 4, 5]
list2 = list1  # Так делать не надо, так как это не копия списка, а ещё одна ссылка на тот же список

print('\n ')
print(list1)  # Печатаем список [1, 2, 3, 4, 5]
lst = list1.pop()  # Извлекли в переменную последний элемент списка (5)
print(lst)  # Печатаем извлечённый элемент (5)
print(list1)  # Печатаем остаток списка [1, 2, 3, 4]

# По этой ссылке (list2) тоже удалён последний элемент [1, 2, 3, 4]
print(list2)
lst_2 = list1.pop(2)  # Извлекли в переменную элемент списка с индексом 2
print(lst_2)  # Печатаем удалённый элемент с индексом [2] (3)
print(list1)  # Печатаем остаток списка [1, 2, 4]

print(list1.insert(2, 3))  # None (Вставляем после 2 элемента элемент (3)
print(list1)  # Печатаем список [1, 2, 3, 4]

list1.append(5)  # Добавляем элемент (5) в конец списка
print(list2)  # [1, 2, 3, 4, 5]


exit()  # Выходит из программы не выполняя возможный последующий код
