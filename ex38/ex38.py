# -*- coding: utf-8 -*-

ten_things = u"Apples Oranges Crows Telephone Light Sugar"

print u"Погодите, тут меньше 10 объектов. Давайте исправим это."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff)!= 10:
    next_one = more_stuff.pop()
    print u"Добавляем: ", next_one
    stuff.append(next_one)
    print u"Теперь у нас %d объектов." % len(stuff)

print u"Итак: ", stuff

print u"Давайте кое-что сделаем с нашими объектами."

print stuff[1]
print stuff[- 1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
