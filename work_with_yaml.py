"""Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными."""

import yaml

to_write_dict = {
    'lst': [1, 2, 3],
    'num': 5,
    'dictionary': {
        'euro': 'U+20AC'.encode('utf-8')
    }
}

with open('files_to_parse/file.yaml', 'w') as ya_file:
    yaml.dump(to_write_dict, ya_file, default_flow_style=False, allow_unicode=True)

with open('files_to_parse/file.yaml', 'r') as read_ya:
    data_from_yaml = yaml.load(read_ya, Loader=yaml.FullLoader)
print(data_from_yaml)
