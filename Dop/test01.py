# # ==============================
# def f(x):
#     return x**2

# g = f
# print(f(4))
# print(g(4))
# print(type(g))
# -------------------------------

# # ИСПОЛЬЗЗОВАНИЕ ВЫЗОВА ФУНКЦИИ ИЗ ФУНКЦИИ
# # ==============================
# def calc1(x):
#     return x + 10

# def calc2(x):
#     return x * 10

# def math(op, z):
#     return op(z)

# print(math(calc2, 5))  # 50
# print(math(calc1, 5))  # 15
# # -------------------------------

# # ==============================
# def sum(x, y):
#     return x + y
# # Можно записать так:
# # sum = lambda x, y: x+y
# но редактор превратил это в следующее:
# def sum(x, y): return x+y
# -------------------------------

# # СРАВНЕНИЕ ВЫЗОВА ОБЪЯВЛЕННОЙ ФУНКЦИИ И ЛЯМБДА-ФУНКЦИИ
# # ==============================
# def mul(x, y):  # Вызываемая функция
#     return x * y


# def calc(op, a, b):  # Вызывающая функция
#     return op(a, b)


# print(calc(mul, 7, 8))  # 56 (используем вызов объявленной функции)
# print(calc(lambda x, y: x+y, 7, 8))  # 15 (используем вызов лямбда-функции)
# # -------------------------------

# # =====================================================
# # Создаём список чётных элементов ряда от 0 до 20
# test_list = [i for i in range(0, 21) if i % 2 == 0]
# print(test_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Создаём список кортежей число - его квадрат для чётных элементов ряда от 0 до 20
# tup_list = [(i, i**2) for i in range(0, 21) if not i % 2]
# print(tup_list)
# # [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144), (14, 196), (16, 256), (18, 324), (20, 400)]

# # Создаём список квадратных корней для чётных элементов ряда от 0 до 20,
# # где корни вычисляются внешней функцией
# def f(x):
#     return round(x**0.5, 3)

# func_list = [f(i) for i in range(0, 21) if not i % 2]
# print(func_list)
# # [0.0, 1.414, 2.0, 2.449, 2.828, 3.162, 3.464, 3.742, 4.0, 4.243, 4.472]
# # -------------------------------------------------------------------

# ДЛЯ ЧЁТНЫХ ЭЛЕМЕНТОВ ПОЛУЧИТЬ СПИСОК КОРТЕЖЕЙ ЧИСЛО-ЕГО КВАДРАТ
# # =====================================================
# # ВАРИАНТ I
# # СЧИТЫВАЕМ ИЗ СТРОКИ, ФОРМИРУЕМ СПИСОК И ИЗ НЕГО ФОРМИРУЕМ СПИСОК КОРТЕЖЕЙ
# test_list = '1 2 3 5 8 15 23 38'
# # res_list = test_list.split()
# res_list = [(int(item), int(item)**2)
#             for item in test_list.split() if not int(item) % 2]
# print(res_list)

# # ВАРИАНТ II
# # СЧИТЫВАЕМ ИЗ ФАЙЛА И ПАРСИМ СТРОКУ
# # Считываем строку данных из файла (r убирает ложные escape - последовательности)
# path = r'J:\MY\_WEB\_GEEKBRAINS\_II_ВТОРАЯ ЧЕТВЕРТЬ\01-ЗНАКОМСТВО С ЯЗЫКОМ PYTHON\PYTHON_PRG\Dop\test01.txt'
# test_data = open(path, 'r', encoding='utf-8-sig')
# # Пробел в конец строки для нормального считывания последнего числа в след. блоке кода
# test_list = test_data.read() + ' '
# test_data.close()

# # Формируем список из считанной из файла строки чисел, разделённых пробелами
# num_bers = []
# while test_list != '':  # Пока не закончится строка
#     space_pos = test_list.index(' ')  # Позиция первого разделительного пробела
#     num_bers.append(int(test_list[:space_pos]))  # В список число в формате int
#     # отрезаем от строки число, которое занесли в список
#     test_list = test_list[space_pos + 1:]

# # Делаем выборку из списка и формируем список кортежей согласно заданию
# res_list = [(item, item**2) for item in num_bers if not item % 2]
# print(res_list)

# # ВАРИАНТ III
# # ИСПОЛЬЗУЕМ ФУНКЦИИ, ВОЗВРАЩАЮЩИЕ LIST Comprehension, С ИСПОЛЬЗОВАНИЕМ lambda функций
# # Применяет функцию f к каждому элементу списка col
# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):  # Выбирает из списка col значения, которые соответствуют условию из функции f
#     return [x for x in col if f(x)]


# test_list = '1 2 3 5 8 15 23 38'.split()  # Получаем список строк из строки
# res = select(int, test_list)  # Преобразуем элементы списка в числа (int)
# res = where(lambda x: not x % 2, res)  # Выбираем чётные числа
# # Применяем функцию lambda, которая возвращает кортеж, к каждому элементу списка res
# res = select(lambda x: (x, x**2), res)
# print(res)
# # -----------------------------------------------------------

# Функция MAP()
# map(f(x), list) - применяет функцию f(x) к каждому элементу списка list и образует объект
# типа map в памяти, из которого, применив к нему преобразование list, можно получить итоговый список

# # Пример использования функции map
# lst = [x for x in range(1, 11)]  # Создаём список чисел
# lst = map(lambda x: x + 10, lst)
# print(lst)  # <map object at 0x0000029E70446F50> - ссылка на объект map
# print(list(lst))  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# # 1. Вводим строку чисел через пробел.
# # 2. Преобразуем ее в список строк чисел.
# # 3. Применяем к каждому элементу списка функцию int и сохраняем результат в объект map
# lst = map(int, input('Вводите числа через пробел:\n').split())
# # 4. Преобразуем объект map в список и распечатываем его.
# print(list(lst))

# # Объект map можно распечатать, не преобразовывая его в список (list)
# lst = map(int, '1 2 3 4'.split())
# for e in lst:
#     e = e**2
#     print(e)  # Выдаст в столбик 1 4 9 16
# # НО ! После испльзования объекта map, он в памяти не сохраняется (повторно использовать невозможно)
# print(list(lst))  # Выдаст []
# # Поэтому результат функции map, если требуется, сохраняют в список list(map(...))

# Функция FILTER()
# filter(f(x), list) - перебирает итерируемый объект (list) и возвращает другой итерируемый объект (filter),
# состоящий из элементов, удовлетворяющих условию функции f(x). Как и map, используется один раз.

# num_str = [i for i in range(11)]
# even = filter(lambda x: not x % 2, num_str)
# print(list(even))

# # Функция ZIP()
# # Функция zip() применяется к набору (напр. списку) итерируемых объектов и возвращает итератор с кортежами из элементов входных данных.
# # Количество элементов в результате равно минимальному количеству элементов входного набора.
# lst1 = [1, 2, 3]
# lst2 = ['о', 'д', 'т']
# lst3 = ['f', 's', 't']
# print(lst1, lst2, lst3)
# tst = zip(lst1, lst2, lst3)
# print(tst)  # <zip object at 0x0000022D21F2FE40>
# print(list(tst))  # [1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't']
# print(list(tst))  # [] Повторное использование объекта zip невозможно

# # Длина результирующего итератора при использовании zip() равна длине наименьшего в наборе итерируемого объекта:
# usrs = ['us1', 'us2', 'us3', 'us4', 'us5']
# ids = [7, 3, 19, 5, 15]
# print(list(zip(usrs, ids)))
# # Результат: [('us1', 7), ('us2', 3), ('us3', 19), ('us4', 5), ('us5', 15)]
# salary = [111, 333, 222]  # наименьший, сократил количество кортежей до 3
# print(list(zip(usrs, ids, salary)))
# # Результат: [('us1', 7, 111), ('us2', 3, 333), ('us3', 19, 222)]

# Функция enumerate
# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных.
# Также, как в map, filter, zip результат невозможно использовать повторно
print(list(enumerate(['Киев', 'Львов', 'Ивано-Франковск', 'Винница'])))
# Результат: [(0, 'Киев'), (1, 'Львов'), (2, 'Ивано-Франковск'), (3, 'Винница')]
