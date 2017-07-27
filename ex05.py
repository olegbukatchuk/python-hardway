# -*- coding: utf-8 -*-

my_name = u'Олег Букатчук'
my_age = 33 # Это правда!
my_height = 183 # см
my_weight = 83 # кг
my_eyes = u'Карие'
my_teeth = u'Белые'
my_hair = u'Чёрные'

print u"Давайте поговорим о человеке по имени %s." % my_name
print u"Его рост составляет %d см." % my_height
print u"Он весит %d кг." % my_weight
print u"На самом деле это не так много."
print u"У него %s глаза и %s волосы." % (my_eyes, my_hair)

# Эта строка кода довольно сложна
print u"Если я сложу %d, %d и %d, то получу %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
