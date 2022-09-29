# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# ВАРИАНТ 0
# Используем count()
#
# text_str.count(word_str)

# text_str = "Сколько мягких булочек"
# word_str = "ко"

# ВАРИАНТ I
# Используем .find()

text_str = input('Введите предложение:\n')
word_str = input('Введите слово: ')

word_str_len = len(word_str)  # Длина искомого слова
text_str_len = len(text_str)  # Длина основной строки

# Первоначальное значение index берётся в отрицательной нумерации -(text_str_len) для исключения
# возможности значения index = -1 на входе в цикл и мгновенного его прерывания.
# Дополнительное смещение на -(word_str_len) компенсирует первое приращение +(word_str_len) в цикле
index = -(text_str_len + word_str_len)  # Указатель но начало области проверки
count_er = -1  # Счётчик количества вхождений искомого слова
while index != -1:  # До тех пор, пока поиск не завершится впустую
    # Переносим начало области проверки
    index = text_str.find(word_str, index + word_str_len)
    count_er += 1
print('Слово "{}" повторяется в строке "{}" {} раз{}'.format(
    word_str, text_str, count_er, "а"*int(1 < count_er < 5)))  # Дописываем "а" к слову раз


# ВАРИАНТ II (От преподавателя)
# Используем срезы строки
#
# text_str = input('Введите предложение:\n')
# word_str = input('Введите слово: ')
#
# count_er = 0
# i = 0
# while i < len(text_str):
#     if text_str[i:i+len(word_str)] == word_str:
#         count_er += 1
#         i += len(word_str)
#     else:
#         i += 1
# print('count_er = {}'.format(count_er))
