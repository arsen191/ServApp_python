"""Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""
import json


def write_order_to_json(item, quantity, price, buyer, data):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "data": data
    }
    with open('files_to_parse/orders.json', 'r') as r_json:
        tmp = json.load(r_json)
        lst_a = tmp['orders']
        lst_a.append(dict_to_json)
        tmp['orders'] = lst_a

    with open('files_to_parse/orders.json', 'w') as w_json:
        json.dump(tmp, w_json, sort_keys=True, indent=4)


write_order_to_json('Pillow', 2, 3000, 'Buyer#1', '2020-12-12 21:00')
write_order_to_json('Bed', 1, 12000, 'Buyer#1', '2020-12-12 21:00')
