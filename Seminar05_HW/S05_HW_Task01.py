# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Считываем строку данных из файла (r убирает ложные escape - последовательности)
path = r'Seminar05_HW\S05_HW_Task01.txt'
test_data = open(path, 'r', encoding='utf-8-sig')
# Пробел в конец строки для нормального считывания последнего слова в след. блоке кода
words_list = test_data.read() + ' '
test_data.close()

# Формируем список слов, разделённых пробелами, из строки, считанной из файла
words = []
print(f'\nИсходный текст:\n\n{words_list}')
# print(words_list)
while words_list != '':  # Пока не закончится строка
    # Позиция первого разделительного пробела
    space_pos = words_list.index(' ')
    if not 'абв' in words_list[:space_pos]:
        words.append(words_list[:space_pos])  # В список

    # отрезаем от строки слово, которое занесли в список
    words_list = words_list[space_pos + 1:]

# Делаем выборку из списка и формируем список согласно заданию
res_list = ' '.join(words)
print(f'\nБез слов, включающих "абв":\n\n{res_list}')
