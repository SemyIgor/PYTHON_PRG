def show_menu():
    print('1 - калькулятор')
    print('2 - корвертор')
    return input('Введите цифру: ')


def show_calc_enter():
    return input('Введите выражение: ')


def show_converter_enter():
    return input('Введите вес в граммах: ')


def show_calc_res(res):
    print(f'Результат калькуляции = {res}')


def show_conv_res(kg, res):
    print('{} г = {}'.format(kg, res))
