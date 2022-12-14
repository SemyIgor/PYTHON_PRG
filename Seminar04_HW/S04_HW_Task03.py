# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

init_list = [15, 28, 35, 28, 44, 15, 51]

# Для списка строк тоже работает
# init_list = ['разработчик', 'программист', 'тестировщик',
#              'программист', 'продакт', 'проджект', 'тестировщик']

# УДАЛЯЕТ ПОВТОРЫ
print('\nИсходный список:')
print(init_list)

# Преобразуем список в множество. Множество состоит из неповторяющихся элементов
init_set = set(init_list)
# Сортируем множество по алфавиту и распечатываем
print('\nУбраны повторы:')
print(sorted(init_set))

# ОСТАВЛЯЕТ ЭЛЕМЕНТЫ, КОТОРЫЕ НЕ ИМЕЮТ КОПИЙ
res_list = [item for item in init_list if init_list.count(item) == 1]

print('\nТолько уникальные элементы:')
print(res_list)
