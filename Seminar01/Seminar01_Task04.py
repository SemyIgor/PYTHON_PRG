# 4 задача
# Напечатать первую цифру после запятой во введённом вещественном числе

n = float(input('Введите число с плавающей точкой: '))
if not n % 1:  # Число не имеет дробной части
    print('Число не имеет дробной части')
else:
    # Остаток от деления на 10 отрицательного числа вычисляется по особым правилам
    # (остаток должен иметь тот же знак, что и делитель), исключаем возникающие при этом проблемы 
    # переводом введенного числа в положительное, использую abs()
    print('Первая цифра после запятой равна {}'.format((int(abs(n) * 10) % 10)))
