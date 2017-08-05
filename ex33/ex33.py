# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
    print u"Вверху значение i равно %d" % i
    numbers.append(i)

    i += 1
    print u"Текущие значения: ", numbers
    print u"Внизу значение i равно %d" % i

print u"Значения: "

for num in numbers:
    print num
    
