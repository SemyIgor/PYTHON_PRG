import user_interface as ui


def todo_choice():  # Организуем получение выбора от пользователя
    todo = ui.todo_choice_input()
    while todo != '1' and todo != '2' and todo != '3' and todo != '4':
        print('Повторите выбор')
        todo = ui.todo_choice_input()
    return todo


def frmat_choice():  # Организуем получение выбора от пользователя
    frmat = ui.choose_export_format()
    while frmat != '1' and frmat != '2' and frmat != '3':
        print('Повторите выбор')
        frmat = ui.choose_export_format()
    return frmat
