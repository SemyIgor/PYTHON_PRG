# 2 задача (2 вариант)
# находим максимальное число из пяти введённых созданием списка вводимых элементов
# и применением к списку функции max()
print('2 задача, 2 вариант')
sp = list()  # Создаём список неопределённого размера
print('Вводите числа:')
for i in range(5):
    x = int(input())
    sp.append(x)
print('Максимальное число равно {}'.format(max(sp)))
