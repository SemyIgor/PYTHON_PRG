# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def code_txt(t_str):  # Функция кодировки
    code_list = ''  # Накопитель кода
    s = 0  # Указатель позиции в тексте
    while s < len(t_str):
        script = t_str[s]  # Обрабатываемый символ
        repeat = 0  # Количество повторений символа
        while (s + repeat) < len(t_str) and t_str[s + repeat] == script:
            repeat += 1
        code_list += (str(repeat) + script)  # Добавляем закодированный блок
        s += repeat  # Перемещаем указатель по тексту
    return code_list


def dcode_txt(c_txt):  # Функция дешифровки
    d_txt = ''  # Количество группы символов
    res_txt = ''  # Дешифрованная строка
    for i in c_txt:  # Каждый элемент строки
        if i.isdigit():  # Формируем кол-во повторений, если цифра
            d_txt += i  # Количество повторений очередного символа
        else:
            res_txt = res_txt + i * int(d_txt)  # Формируем итоговую строку
            d_txt = ''  # Обнуляем количество повторений
    return res_txt

# tst_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# tst_str = input('Введите текст для кодировки:\n')


# Считываем из файла текст для кодировки
to_code = open('Seminar05_HW\S05_HW_Task04-1.txt', 'r', encoding='utf-8-sig')
tst_str = to_code.read()
to_code.close()

print(f'Текст для кодировки:\n{tst_str}')
code_text = code_txt(tst_str)
print(f'Текст после кодировки:\n{code_text}')

# Записываем в файл зашифрованный текст
to_dcode = open('Seminar05_HW\S05_HW_Task04-2.txt', 'w', encoding='utf-8-sig')
tst_str = to_dcode.write(code_text)
to_dcode.close()

dec_text = dcode_txt(code_text)
print(f'Текст после дешифровки:\n{dec_text}')
