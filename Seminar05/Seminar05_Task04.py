# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] , [1, 2, 3, 4, 6, 7], [1, 3, 4, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]
print(lst, '\n')
two_dig = []  # последовательность из 2 чисел
three_dig = []  # последовательность из 3 чисел
four_dig = []  # последовательность из 4 чисел
five_dig = []  # последовательность из 5 чисел
six_dig = []  # последовательность из 6 чисел
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            # Формируем последовательности из 2 чисел
            two_dig.append((lst[i], lst[j]))
            for k in range(j+1, len(lst)):
                if lst[j] < lst[k]:
                    three_dig.append((lst[i], lst[j], lst[k]))  # из 3 чисел
                    for l in range(k+1, len(lst)):
                        if lst[k] < lst[l]:
                            four_dig.append(
                                (lst[i], lst[j], lst[k], lst[l]))  # из 4 чисел
                            for m in range(l+1, len(lst)):
                                if lst[l] < lst[m]:
                                    five_dig.append(
                                        (lst[i], lst[j], lst[k], lst[l], lst[m]))  # из 5
                                    for n in range(m+1, len(lst)):
                                        if lst[m] < lst[n]:
                                            # формируем последовательность из 6 чисел
                                            six_dig.append(
                                                (lst[i], lst[j], lst[k], lst[l], lst[m], lst[n]))

# Пропускаем через множество, чтобы убрать возможные повторы
two = (list(set(two_dig)))
three = (list(set(three_dig)))
four = (list(set(four_dig)))
five = (list(set(five_dig)))
six = (list(set(six_dig)))

# объединяем последовательности в один список
six = six + five + four + three + two

# Распечатываем список всех возможных последовательностей
for item in six:
    print(list(item))
