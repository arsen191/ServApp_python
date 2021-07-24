"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать
строковые представление в формат Unicode и также проверить тип и содержимое переменных.
"""
word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'
print(f'{word1} = {type(word1)}, {word2} = {type(word2)}, {word3} = {type(word3)}')

word1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word2_unicode = '\u0441\u043E\u043A\u0435\u0442'
word3_unicode = '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440'
print(f'{word1_unicode} = {type(word1_unicode)}, {word2_unicode} = {type(word2_unicode)}, '
      f'{word3_unicode} = {type(word3_unicode)}')

