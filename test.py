import os
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text.txt')


def add_string_number(path_to_main_file):
    counter = 0  # Счетчик для нумерации
    path_to_file = os.path.dirname(path_to_main_file)

    with open(path_to_main_file, 'r', encoding='UTF-8') as f:  # Открываем указанный файл
        with open(os.path.join(path_to_file, 'temp_file.txt'), 'w', encoding='UTF-8') as temp_file:  # Создаем файл в
            # который будем вести запись
            for line in f:  # Перебираем все строки указанного файла
                counter += 1
                line = f'{counter} {line}'  # Создаем нужную нам строку
                temp_file.write(line)  # Построчно записываем во временный файл
    os.remove(path_to_main_file)  # Удаляем изначальный файл
    os.rename(os.path.join(path_to_file, 'temp_file.txt'), path_to_main_file)  # Переименовываем временный файл


add_string_number(path)
