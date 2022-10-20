# Глобальные переменные x и y
x = 0
y = 0

# Инициализация


def init(a, b):
   # Локальные переменные x и y, но можно сделать их глобальными:
    global x
    global y
    x = a
    y = b

# Решение задачи


def do_it():
    return x + y


# init(7, 8)

# x=0, y=0 если не использовать в init() global. Иначе x=7, y=8
# print(x)
# print(y)
