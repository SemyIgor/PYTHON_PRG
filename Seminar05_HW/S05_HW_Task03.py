board = list(range(1, 10))  # Генерируем номера клеток поля


def draw_board(board):  # Рисуем игровое поле
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def take_input(player_token):  # Обрабатываем ход игрока
    valid = False
    while not valid:  # Пока не сделаем ход без ошибок
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:  # Если введено число от 1 до 9
            if (str(board[player_answer-1]) not in "XO"):  # Если выбранная клетка не занята
                # То заносим в клетку X или O
                board[player_answer-1] = player_token
                valid = True  # Признак завершения хода
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(board):  # Набор выигрышных вариантов
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        # Если по всем трём индексам из любого выигрышного кортежа
        # на игровом поле выпали одинаковые символы (X или O),
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]  # то возвращаем этот символ - он победил.
    return False  # Иначе победа пока не достигнута


def main(board):  # Главная функция
    counter = 0  # Счетчик ходов
    win = False  # Изначально победителей нет
    while not win:
        draw_board(board)
        if counter % 2 == 0:  # Если ход четный,
            take_input("X")  # то ход "крестиков"
        else:
            take_input("O")  # Иначе ход "ноликов"
        counter += 1
        if counter > 4:  # Если хотя бы один сделал 3 хода
            tmp = check_win(board)  # Проверяем на выигрыш
            if tmp:  # в tmp символ победителя (X или O)
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:  # Последний ход не может быть выигрышным
            print("Ничья!")
            break
    draw_board(board)  # Рисуем поле завершённой игры


main(board)  # Запуск игры
