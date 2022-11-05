# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# ◦ 45 -> 101101
# ◦ 3 -> 11
# ◦ 2 -> 10

# ВАРИАНТ II. Используем рекурсию (ДОРАБОТАТЬ!)
def dec_to_bin(n):
    str_bin = ''
    if n // 2 == 0:
        return str(n % 2) + str_bin
    else:
        str_bin = str(n % 2) + str_bin
        n = n // 2
    return dec_to_bin(n)


dec_num = int(input('Введите целое число в десятичном формате: '))
print(dec_num)

print(dec_to_bin(dec_num))
