# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print u"Копирование данных из файла %s в файл %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print u"Исходный файл имеет размер %d байт" % len(indata)

print u"Файл назначения существует? %r" % exists(to_file)
print u"Готов к работе, нажмите клавишу Enter для продолжения или CTRL+C для отмены."

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print u"Отлично, всё сделано..."
out_file.close()
in_file.close()
