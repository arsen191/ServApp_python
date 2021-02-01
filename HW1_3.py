"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""
w1 = b'attribute'
#w2 = b'класс'   # SyntaxError: bytes can only contain ASCII literal characters.
#w3 = b'функция' # SyntaxError: bytes can only contain ASCII literal characters.
w4 = b'type'

print(w1, w4)