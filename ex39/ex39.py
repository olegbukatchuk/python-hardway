# -*- coding: utf-8 -*-

# Схема связей аббревиатур с названиями связей
countries = {
    u'Россия': 'RU',
    u'Германия': 'DE',
    u'Узбекистан': 'UZ',
    u'Зимбабве': 'ZW',
    u'Турция': 'TR'
}

# Создание базового набора стран и некоторых городов в них
cities = {
    'UZ': u'Газли',
    'TR': u'Сарыгерме',
    'DE': u'Мюнхен'
}

# Добавление некоторых городов
cities['ZW'] = u'Гверу'
cities['RU'] = u'Москва'

# Вывод некоторых городов
print '- ' * 10
print u"В стране ZW усть город: ", cities['ZW']
print u"В стране RU есть город: ", cities['RU']

# Вывод некоторых стран
print '- ' * 10
print u"Аббревиатура Турции: ", countries[u'Турция']
print u"Аббревиатура Германии: ", countries[u'Германия']

# Выполняется с учётом страны и словаря городов
print '- ' * 10
print u"В Турции есть город: ", cities[countries[u'Турция']]
print u"В Германии есть город: ", cities[countries[u'Германия']]

# Вывод аббревиатур всех стран
print '- ' * 10
for country, abbrev in countries.items():
    print u"%s имеет аббревиатуру %s" % (country, abbrev)

# Вывод всех городов в странах
print '- ' * 10
for abbrev, city in cities.items():
    print u"В стране %s есть город %s" % (abbrev, city)

# А теперь сразу оба типа данных
print '- ' * 10
for country, abbrev in countries.items():
    print u"В стране %s используется аббревиатура %s и есть город %s" % (country, abbrev, cities[abbrev])

print '- ' * 10
# Безопасное получение аббревиатуры страны, которая не представлена
country = countries.get(u'США', None)

if not country:
    print u"Прошу прощения, США не обнаружено."

# Получение города со значением по умолчанию
city = cities.get('US', u'не существует')
print u"В стране 'US' есть город: %s" % city
