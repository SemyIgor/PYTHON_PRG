# Определите среднее значение всех элементов последовательности,
# завершающейся числом 0.

# Создаём список и наполняем его числами
numbers = list()
summ = 0
entr_num = '1'  # Любое число для первой проверки входа в цикл
print('Введите число и нажмите ENTER. Введите 0 для завершения: ')
while entr_num.isdigit():
    entr_num = input()
    if entr_num == '0':
        break
    if entr_num.isdigit():
        elem = int(entr_num)
        summ += elem
        numbers.append(elem)
if len(numbers) != 0:
    print(
        f'Среднее арифметическое элементов последовательности {numbers} \nравно {summ / len(numbers)}')
else:
    print('Вы не ввели никаких чисел !')
