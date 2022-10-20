import model_sub as model  # Здесь меняем название модуля
import view

func_name = 'Разность x - y'


def button_click():
    #  model.init(get_value())
    value_a = view.get_value()  # Получаем первое слагаемое
    value_b = view.get_value()  # Получаем второе слагаемое
    model.init(value_a, value_b)
    res = model.do_it()
    view.view_data(res, func_name)
