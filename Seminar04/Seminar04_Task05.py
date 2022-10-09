# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#
# Пример:
# Входные данные:       Выходные данные:
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye               Bye

def key_and_val(dict, word):  # Функция поиска в словаре пары заданному слову
    for k, v in dict.items():  # Перебираем пары "ключ - значение словаря"
        if k == word:  # Если это слово является ключом
            return f'Заданному слову {k} соответствует слово {v}'
        if v == word:  # Если это слово является значением
            return f'Заданному слову {v} соответствует слово {k}'
    return 'К заданному слову пара не найдена'


diction =\
    {
        'Hello': 'Hi',
        'Bye': 'Goodbye',
        'List': 'Array'
    }

word_to_find = 'Goodbye'
# word_to_find = 'Array'
# word_to_find = 'Hello'

print(key_and_val(diction, word_to_find))  # Печатаем результат поиска слова
