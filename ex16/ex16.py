# -*- coding: utf-8 -*-

import codecs, sys
outf = codecs.getwriter('utf-8')(sys.stdout, errors='replace')
sys.stdout = outf

from sys import argv

script, filename = argv

#print u"Я собираюсь стереть файл %r." % filename
#print u"Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C)."
#print u"Если хотите стереть файл, нажмите клавишу Enter."

#raw_input("?")

print u"Открытие файла..."
target = open(filename, 'w')

print u"Очистка файла. До свидания!"
target.truncate()

print u"Теперь я запрашиваю у вас три строки."

line1 = raw_input(u"строка 1: ")
line2 = raw_input(u"строка 2: ")
line3 = raw_input(u"строка 3: ")

print u"Это я запишу в файл."

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print u"И наконец я закрою файл."
target.close()
