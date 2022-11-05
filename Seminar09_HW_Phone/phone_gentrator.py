from random import randint

for i in range(30):
    num = '+7'
    for j in range(10):
        if j == 0:
            num = num + '('
        if j == 3:
            num = num + ')'
        num += str(randint(0, 9))
    print(num)
