def calc(text, log):
    try:
        return eval(text)
    except SyntaxError:
        log.error(f'Синтаксическая ошибка {text}')
        return 'Ошибка ввода'


def convertor(gr, log):
    try:
        return str(round(float(gr) / 1000, 3)) + 'кг'
    except ValueError:
        log.error(f'Ошибка конвертации {gr}')
        return 'Не бывает столько граммов'
