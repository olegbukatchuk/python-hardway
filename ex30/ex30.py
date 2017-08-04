# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15

if cars > people:
    print u"Поедем на машине."
elif cars < people:
    print u"Не поедем на машине."
else:
    print u"Мы не можем выбрать."

if buses > cars:
    print u"Слишком много автобусов."
elif buses < cars:
    print u"Может, поехать на автобусе?"
else:
    print u"Мы до сих пор не можем выбрать."

if people > buses:
    print u"Хорошо, давайте поедем на автобусе."
else:
    print u"Прекрасно, давайте останемся дома."
