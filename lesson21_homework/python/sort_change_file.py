import re

import write_read_file


def change_base(base_name, last_name):
    change_list = []
    file = write_read_file.write_read_base(base_name, 'r')
    for line in file:
        if line.find(last_name) == -1:
            change_list.append(line.strip())
    return change_list


def replace_base(base_name, last_name):
    change_list = []
    file = write_read_file.write_read_base(base_name, 'r')
    try:
        for line in file:
            if line.find(last_name) != -1:
                print(line.strip())
                pattern = input("Введите данные которые нужно заменить\n: ").title()
                line_change = input("Введите на что нужно поменять\n: ").title()
                new_line = line.strip().replace(pattern, line_change)
                change_list.append(new_line)
            else:
                change_list.append(line.strip())
        return change_list
    except ValueError:
        pass


def employee_search(base_name, last_name):
    change_list = []
    file = write_read_file.write_read_base(base_name, 'r')
    for line in file:
        if line.find(last_name) != -1:
            change_list.append(line.strip())
    return change_list
