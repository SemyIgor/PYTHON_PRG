import user_interface as ui
import model as mod

global active_base
# active_base = []


def run():
    global active_base
    run_time = True
    while run_time == True:
        main_choice = mod.getting_main_choice()
        if main_choice == '1':
            # Выбор функции конвертирования базы
            # print(mod.getting_convertor_choice())
            convert_action = mod.getting_convertor_choice()
            if convert_action == '1':
                active_base = mod.get_txt_file()
            elif convert_action == '2':
                # active_base = mod.save_txt_file(active_base)
                mod.save_txt_file(active_base)
            elif convert_action == '3':
                active_base = mod.get_csv_file()
            elif convert_action == '4':
                # active_base = mod.save_csv_file(active_base)
                mod.save_csv_file(active_base)
            elif convert_action == '5':
                active_base = mod.get_json_file()
            elif convert_action == '6':
                # active_base = mod.save_json_file()
                mod.save_json_file(active_base)
            # return
        elif main_choice == '2':
            # Выбор действий по редактированию базы
            # print(mod.getting_base_option_choice())
            base_option_action = mod.getting_base_option_choice()
            if base_option_action == '1':
                base_option = mod.show_base(active_base)
            elif base_option_action == '2':
                base_option = mod.add_person(active_base)
            elif base_option_action == '3':
                base_option = mod.remove_person(active_base)
            elif base_option_action == '4':
                base_option = mod.edit_person_fields(active_base)
            elif base_option_action == '5':
                base_option = mod.edit_base_structure()
            elif base_option_action == '6':
                base_option = mod.save_base_changes()
            # return
        elif main_choice == '3':
            ui.print_base(active_base)
            # return
        elif main_choice == '0':
            break
