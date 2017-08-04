# -*- coding: utf-8 -*-

print u"Давайте попрактикуемся!"
print u'Вы должны знать об управляющих последовательностях с символом \\, которые \n управляют переносом строк и \t отступами.'

poem = u"""
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать,
Хочу всегда
я быть с тобой рядом
\n\t\tИ никогда не отпускать!
"""

print "-----------------------"
print poem
print "-----------------------"

five = 10 - 2 + 3 - 6
print u"Здесь долдна быть пятерка: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print u"Начиная с: %d" % start_point
print u"У нас есть %d бобов, %d банок и %d ящиков." % (beans, jars, crates)


start_point = start_point / 10

print u"Такде можно поступить следующим образом:"
print u"У нас есть %d бобов, %d банок и %d ящиков." % secret_formula(start_point)
