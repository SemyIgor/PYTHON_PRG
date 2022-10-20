import model
import view
from statistics import mode


def run(log):
    log.info('Показываю меню')
    option = view.show_menu()
    log.warn('Меню показано')
    if option == '1':
        log.info('Выбран калькулятор')
        res = view.show_calc_enter()
        res = model.calc(res, log)
        view.show_calc_res(res)
    if option == '2':
        log.info('Выбран конвертор')
        g_res = view.show_converter_enter()
        kg_res = model.convertor(g_res, log)
        view.show_conv_res(g_res, kg_res)
