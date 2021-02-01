"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
преобразовать результаты из байтовового в строковый тип на кириллице."""
import subprocess

args = ['ping', '-c', '3', 'youtube.com']
subproc_ping_youtube = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping_youtube.stdout:
    line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'), end='')

args_ya = ['ping', '-c', '3', 'yandex.ru']
subproc_ping_ya = subprocess.Popen(args_ya, stdout=subprocess.PIPE)

for line in subproc_ping_ya.stdout:
    line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'), end='')