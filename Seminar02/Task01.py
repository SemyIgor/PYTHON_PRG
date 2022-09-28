# Даны три целых числа.
# Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = int(input('Введите a = '))
b = int(input('Введите b = '))
c = int(input('Введите c = '))

count = 1
if a == b and a == c and b == c:
    print(3)
elif a == b and a != c:
    print(2)
elif b == c and b != a:
    print(2)
elif a == c and a != b:
    print(2)
else:
    print(0)
