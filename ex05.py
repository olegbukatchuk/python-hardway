# -*- coding: utf-8 -*-

name = u'Олег Букатчук'
age = 33 # Это правда!
height = 183 # см
weight = 83 # кг
eyes = u'Карие'
teeth = u'Белые'
hair = u'Чёрные'

print u"Давайте поговорим о человеке по имени %s." % name
print u"Его рост составляет %d см." % height
print u"Он весит %d кг." % weight
print u"На самом деле это не так много."
print u"У него %s глаза и %s волосы." % (eyes, hair)

# Эта строка кода довольно сложна
print u"Если я сложу %d, %d и %d, то получу %d." % (age, height, weight, age + height + weight)
