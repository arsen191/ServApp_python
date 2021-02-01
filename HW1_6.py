"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и
вывести его содержимое.
"""
lst_to_write = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as f_w:
    for el in lst_to_write:
        f_w.write(el + '\n')

f = open('test_file.txt')
print(f)    # кодировка по умолчанию utf-8
f.close()

with open('test_file.txt', 'r', encoding='utf-8') as f_r:
    for row in f_r:
        print(row, end='')
