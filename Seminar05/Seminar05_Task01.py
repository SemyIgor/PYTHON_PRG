# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
#
# Входные данные        # Выходные данные
# 1 2 3 5 6 7 8         # 4

# Поиск недостающего числа в ряду
def missed_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:  # если нет, то
            return lst[i] - 1  # приводим к требуемому


path = 'Seminar05\S05_Task01.txt'
dta = open(path, 'r', encoding='utf-8-sig')
lst_str = dta.read()
dta.close()

lst_num = list(map(int, lst_str.split()))  # список в целые
print(missed_num(lst_num))
