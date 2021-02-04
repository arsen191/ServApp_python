"""Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
 из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
- Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
- Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
- Проверить работу программы через вызов функции write_to_csv()."""
import re
import os
import csv

res_list = [['Название ОС', 'Код продукта', 'Изготовитель системы', 'Тип системы']]


def get_data():
    directory = 'files_to_parse/'
    for file in os.listdir(directory):
        tmp_list = []
        if file.endswith(".txt"):
            with open(f'{directory}{file}', 'r', encoding='cp1251') as f:
                for row in f:
                    for i in range(0, len(res_list[0])):
                        if re.match(res_list[0][i], row):
                            temp = re.split(r':\s+', row)
                            tmp_list.append(temp[1])
        if file == 'info_1.txt':
            res_list.append(tmp_list)
        elif file == 'info_2.txt':
            res_list.append(tmp_list)
        elif file == 'info_3.txt':
            res_list.append(tmp_list)
    return res_list


def write_to_csv():
    with open('files_to_parse/complete_file_HW1.csv', 'w') as w_csv:
        w_csv_writer = csv.writer(w_csv)
        for row in get_data():
            w_csv_writer.writerow(row)


write_to_csv()
