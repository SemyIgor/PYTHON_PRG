# PYTHON
# Кроссплатформенность
# Подходит для:
#  - Веб-сервисов;
#  - ML (Meta Language), DataScience, Аналитики;
#  - Игр
#  - Написание софта
# Интерпретируемый
# Исполняемый файл запустится на компьютере только если в системе установлен интерпретатор Python


print("Hello, Мир !")
print("И Вам здравствуйте!")
# Python - язык с динамической типизацией

# ПРИСВАИВАНИЕ
text_var = None
print(text_var)
print(type(text_var))

text_var = 'Jane'  # Строка
print(text_var)
print(type(text_var))

# ВЫВОД ТИПА ДАННЫХ ПЕРЕМЕННОЙ:
a = 24  # int
print(a)
print(type(a))

# РАБОТА С КАВЫЧКАМИ
text_1 = "Так называемые 'партнёры'"
text_2 = 'Так называемые "партнёры"'
text_3 = 'Так называемые \'партнёры\''
print(text_1)  # Так называемые 'партнёры'
print(text_2)  # Так называемые "партнёры"
print(text_3)  # Так называемые 'партнёры'

# ФОРМАТИРОВАНИЕ СТРОК:
var1 = 5
var2 = 7
var3 = 14
print(var1, '-', var2, '-', var3)
print('{} - {} - {}'.format(var1, var2, var3))
print('{1} - {2} - {0}'.format(var1, var2, var3))
print(f'{var1} - {var2} - {var3}')

# ЛОГИЧЕСКИЕ ПЕРЕМЕННЫЕ:
t = True
f = False
print(t)  # True
print(f)  # False

# СПИСКИ (ниже по тексту будет подробнее)
list_one = ['1', '2', '3', '4', 'Hello']
print(list_one)

# ВВОД ЧИСЕЛ
a = int(input("Введите число а: "))
print(a)

a = float(input("Введите число а: "))
print(a)

a = input("Введите число x: ")  # 12
b = input("Введите число y: ")  # 80
print(a + b)  # 1280

# !!! Получение дробной части числа с плавающей точкой
print(2.56 % 1)

# ОКРУГЛЕНИЕ
a = 1.3
b = 3
c = a * b
print(c)  # 3.9000000000000004
print(round(c, 5))  # 3.9
print(round(a * b))  # 4

# ОПЕРАТОР in
message = 'Hello, World!'
print('Hello' in message)  # True
print('hello' in message)  # False

# ПОРАЗРЯДНЫЕ ОПЕРАЦИИ
number_one = 5  # Число в десятичной форме
number_two = 0b1011  # Число в двоичной форме

# Выводим десятичное число в двоичной форме
print('number_one = {:0b}'.format(number_one))  # 101

# Выводим двоичное число в десятичной форме
print('number_two = {}'.format(number_two))  # 11

print(16 << 1)  # 32
print(16 >> 1)  # 8
print(15 << 1)  # 30
print(15 >> 1)  # 7

# МНОЖЕСТВЕННОЕ СРАВНЕНИЕ
a = 1 < 5 < 3
print('a = {}'.format(a))  # False
a = 1 < 5 > 3
print('a = {}'.format(a))  # True

# ЛОГИКА В СПИСКАХ
f = [1, 2, 3, 4]
print(2 in f)  # True (В списке f есть 2)

# ПРОВЕРКА НА ЧЁТНОСТЬ
is_even = f[0] % 2 == 0  # False (1 - число нечётное)
# False (f[0] % 2 равно 1, то есть True, not True - это False)
is_even = not f[0] % 2

# КОНСТРУКЦИЯ if - else
username = input('Введите Ваше имя: ')
if (username == 'Маша'):
    print('Ура! Это же Маша!')
else:
    print(f'Здравствуй, {username}')

# КОНСТРУКЦИЯ if - elif - else
username = input('Введите Ваше имя: ')
if (username == 'Маша'):
    print('Ура! Это же Маша!')
elif (username == 'Маша'):
    print('Мы так ждали тебя, Марина !')
elif (username == 'Ильнар'):
    print('Ильнар - топ ! :-)')
else:
    print(f'Здравствуй, {username}')

# КОНСТРУКЦИЯ while
original = 235
print('Исходное число равно {}'.format(original))
inverted = 0
while (original != 0):
    inverted = inverted * 10 + original % 10
    original //= 10
    print(inverted)
print('Инвертированное число равно {}'.format(inverted))

# КОНСТРУКЦИЯ while - else
original = 235
print('Исходное число равно {}'.format(original))
inverted = 0
while (original != 0):
    inverted = inverted * 10 + original % 10
    original //= 10
    print(inverted)
else:
    print('Инвертированное число равно {}'.format(inverted))
print('Наконец-то конец !')

# ЦИКЛ for
for i in 1, 2, 3, 4, 5:  # Перебор списка
    print(i)

stranger_name = 'Владислав'  # Перебор строки
for i in stranger_name:
    print(i)

n = 3  # Перебор диапазона
for i in range(-n, (n + 1)):
    print(i)

for i in range(0, 10, 2):  # Перебор диапазона с шагом
    print(i)

# РАБОТА СО СТРОКАМИ

text = 'cъешь ещё этих мягких французских булок'

print(len(text))  # 39
print('ещё' in text)  # True
print(text.isdigit())  # False
print(text.islower())  # True
print(text.replace('ещё', 'ЕЩЁ'))  # cъешь ЕЩЁ этих мягких французских булок
print(text[10:14])  # этих
print(text[22:-14] + text[-11] + text[-4])  # фразу

# (Выборка с элемента [0] каждый 6-й элемент до конца):
print(text[::6])  # сеикакл

# ВВЕДЕНИЕ В СПИСКИ
numbers = [1, 2, 3, 4, 5]  # Самый простой способ создания списка
ran = range(1, 6)  # range - это отдельный тип
print(type(ran))  # <class 'range'>
numbers = list(ran)  # Приведение типа range к типу list
print(type(numbers))  # <class 'list'>

numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

for i in numbers:
    print(i**2)  # В цикле выводит в столбик квадраты переменной i (100, 4, 9, 16, 25),
print(numbers)  # но не изменяет сами элементы списка [10, 2, 3, 4, 5]

# СПИСКИ СТРОК
colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
print(colors * 2)  # ['red', 'green', 'blue', 'red', 'green', 'blue']

for e in colors:
    print(e)  # red green blue в цикле столбиком

for e in colors:
    print(e * 2)  # redred greengreen blueblue в цикле столбиком

colors.append('grey')  # Добавляем элемент в конец списка
print(colors)  # ['red', 'green', 'blue', 'grey']

print(colors == ['red', 'green', 'blue', 'grey'])  # True

colors.remove('red')  # Удаляет указанный элемент (альтернатива: del colors[0])
print(colors)  # ['green', 'blue', 'grey']

del colors[0]
print(colors)  # ['blue', 'grey']

del colors[-1]
print(colors)  # ['blue']

# ФУНКЦИИ


def function_name(x):
    # Line 1
    # Line 2
    x += 2
    # optional return x


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1
print(f(arg))  # Целое
print(type(f(arg)))  # <class 'str'>

arg = 2.3
print(f(arg))  # 23
print(type(f(arg)))  # <class 'int'>

arg = 2
print(f(arg))  # None
print(type(f(arg)))  # <class 'NoneType'>
