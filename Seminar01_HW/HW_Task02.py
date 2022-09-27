# Напишите программу
# для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True
print('x y z\t¬(X ⋁ Y ⋁ Z)\t¬X ⋀ ¬Y ⋀ ¬Z\tСравнение'.format())
for x in range(2):
    for y in range(2):
        for z in range(2):
            left_side = bool(not(x or y or z))
            right_side = bool(not x and not y and not z)
            check_one_line = 'Истинно' if left_side == right_side else 'Ложно'
            print('{} {} {}\t{}\t\t{}\t\t{}'.format(
                x, y, z, left_side, right_side, check_one_line))
            result = result and (left_side == right_side)
if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
