# -*- coding: utf-8 -*-

x = u"Существует %d типов людей." % 10
binary = "Python"
do_not = u"нет"
y = u"Те, кто понимает %r, и те, кто - %s." % (binary, do_not)

print x
print y

print u"Я сказал: %s." % x
print u"А ещё я сказал: ' %s'." % y

hilarious = False
joke_evaluation = u"Разве это не смешно?! %r"

print joke_evaluation % hilarious

w = u"Это часть стороки слева..."
e = u" а это справа."

print w + e
