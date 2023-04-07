from prettytable import PrettyTable


def output_base(base_name):
    my_table = PrettyTable()
    my_table.field_names = ["Фамилия Имя", "Возраст", "Пол"]
    try:
        with open(fr'../txt/{base_name}', 'r', encoding='utf-8') as fr:
            for i in fr:
                row = i.strip().split()
                full_name = " ".join(row[:2])
                my_table.add_row([full_name, row[2], row[3]])
            print(my_table)
    except FileNotFoundError:
        print(f"Базы c именем '{base_name}' нет")


def write_read_base(base_name, key, employees=[]):
    with open(f'../txt/{base_name}', key, encoding='utf-8') as fw:
        if key == 'r':
            f = fw.readlines()
            return f
        for i in employees:
            print(i, file=fw)
