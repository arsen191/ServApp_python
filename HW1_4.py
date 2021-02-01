"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""
word1 = 'разработка'
word2 = 'администрирование'
word3 = 'protocol'
word4 = 'standard'

word1_encoded = word1.encode('utf-8')
word2_encoded = word2.encode('utf-8')
word3_encoded = word3.encode('utf-8')
word4_encoded = word4.encode('utf-8')
print(word1_encoded, '\n', word2_encoded, '\n', word3_encoded, '\n', word4_encoded)
print('*******************************************')

word1 = word1_encoded.decode('utf-8')
word2 = word2_encoded.decode('utf-8')
word3 = word3_encoded.decode('utf-8')
word4 = word4_encoded.decode('utf-8')
print(word1, '\n', word2, '\n', word3, '\n', word4)
