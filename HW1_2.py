"""Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""
word1 = b'class'
word2 = b'function'
word3 = b'method'
print(f'word1 = {type(word1)} - {word1} - {len(word1)}')
print(f'word2 = {type(word2)} - {word2} - {len(word2)}')
print(f'word3 = {type(word3)} - {word3} - {len(word3)}')