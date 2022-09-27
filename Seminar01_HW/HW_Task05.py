# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def string_del_spaces(str_line):  # Удаляем пробелы из введенной строки
    str_line = str_line.replace(' ', '')
    return str_line


def comma_index(str_line):  # Находим индекс запятой в строке
    comma_index = str_line.find(',')
    return comma_index


def get_x(str_line, comma_index):  # Получаем координату x
    x = float(str_line[:comma_index])
    return x


def get_y(str_line, comma_index):  # Получаем координату y
    y = float(str_line[comma_index + 1:])
    return y


a_coords = string_del_spaces(  # Получаем строку с координатами точки А и удаляем лишние пробелы
    input('Введите координаты точки А через запятую по форме Ax, Ay: '))

Ax = float(get_x(a_coords, comma_index(a_coords)))  # Координата x точки A
Ay = float(get_y(a_coords, comma_index(a_coords)))  # Координата y точки A

b_coords = string_del_spaces(  # Получаем строку с координатами точки B и удаляем лишние пробелы
    input('Введите координаты точки В через запятую по форме Bx, By: '))

Bx = float(get_x(b_coords, comma_index(b_coords)))  # Координата x точки B
By = float(get_y(b_coords, comma_index(b_coords)))  # Координата y точки B


length_AB = ((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5

print('\nAx = {}, \nBx = {}, \nAy = {}, \nBy = {}, \nДлина отрезка = {}'.format(
    Ax, Bx, Ay, By, round(length_AB, 2)))
