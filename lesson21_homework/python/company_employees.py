import os
import re
import time
import write_read_file
import creat_base_employees
from lesson21_homework.python import sort_change_file


if not os.path.isdir(r'../txt'):
    os.mkdir(r'../txt')
def input_name_base():
    name = input("Введите имя базы данных\n: ")
    # base_list.append(name)
    return name



name_base = input_name_base()
new_base_list = creat_base_employees.creat_base_employees()
write_read_file.write_read_base(name_base, 'w', new_base_list)
write_read_file.output_base(name_base)

while (input_user := input('Выберите действие:\n'
                           '\t1 Добавить сотрудника\n'
                           '\t2 Изменить данные о сотруднике\n'
                           '\t3 Удалить данные из базы о  сотруднике\n'
                           '\t4 Поиск сотрудников\n'
                           '\t5 Вывод всех сотрудников\n'
                           '\t6 Вывод сотрудников из указанного файла\n'
                           '\t0 Для выхода из программы\n'
                           '\t: ')) != '0':
    match input_user:
        case '1':
            print('Введите данные сотрудника:')
            line = [f"{input('Введите фамилию: ').title()} "
                    f"{input('Введите имя: ').title()} "
                    f"{input('Введите возраст: ')} "
                    f"{input('Введите пол муж/жен: ').lower()} "]
            write_read_file.write_read_base(name_base, 'a', line)
            write_read_file.output_base(name_base)
        case '2':
            last_name = input("Введите фамилию сотрудника для изменения данных\n: ").title()
            new_list = sort_change_file.replace_base(name_base, last_name)
            write_read_file.write_read_base(name_base, 'w', new_list)
            write_read_file.output_base(name_base)
        case '3':
            last_name = input("Введите фамилию сотрудника для удаления из базы\n: ").title()
            new_list = sort_change_file.change_base(name_base, last_name)
            write_read_file.write_read_base(name_base, 'w', new_list)
            write_read_file.output_base(name_base)
        case '4':
            user_req = input("Введите фамилию сотрудника для поиска\n: ").title()
            new_list = sort_change_file.employee_search(name_base, user_req)
            if new_list:
                print(*new_list, sep='\n')
                save_change = input("Сохранить данные\n"
                                    "1 Да\n"
                                    "0 Нет\n: ")
                if save_change == '1':
                    name_base = input_name_base()
                    write_read_file.write_read_base(name_base, 'w', new_list)
                    write_read_file.output_base(name_base)

            else:
                print(f"Сотрудника с фамилией {user_req} в базе нет")
        case '5':
            base_list = os.listdir(r'../txt')
            for name in base_list:
                name_out = re.match(r'^[^\.]*', name)
                print(name_out[0])
                write_read_file.output_base(name)
        case '6':
            base_name = input("Введите название файла: ")
            write_read_file.output_base(base_name)
        case _:
            print("Данное действие не возможно")

for _ in range(3):
    print('Обновление и сохранение записей', end=' ')
    for i in range(5):
        print('.', end=' ')
        time.sleep(0.4)
    print(end='\r')
print()
print('Программа завершена')
