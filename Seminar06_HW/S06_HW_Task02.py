﻿# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные                                            # Выходные данные
# ОРРОРОРООРРРО                                             # 3
# ООООООРРРОРОРРРРРРР                                       # 7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР  # 31


# inp_str = 'ОРРОРОРООРРРО'
# inp_str = 'ООООООРРРОРОРРРРРРР'
inp_str = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'

count = 0
max_length = 0
for i in range(len(inp_str)):
    if inp_str[i] == 'Р':
        count += 1
        if count > max_length:
            max_length = count
      #   print(f'Р, c = {count}, max = {max_length}')
    else:
        count = 0
      #   print('О')
print(f'\nНаибольшее количество выпавших подряд Р равно: {max_length}')