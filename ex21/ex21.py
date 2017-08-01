# -*- coding: utf-8 -*-

def add(a, b):
    print u"СЛОЖЕНИЕ %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print u"ВЫЧИТАНИЕ %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print u"УМНОЖЕНИЕ %d * %d" % (a, b)
    return a * b 

def divide(a, b):
    print u"ДЕЛЕНИЕ %d / %d" % (a, b)
    return a / b

print u"Давайте выполним несколько вычислений с помощью функций!"

age = add(30, 7)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(220, 2)

print u"Возраст: %d, Рост: %d, Вес: %d, IQ: %d" % (age, height, weight, iq)

# Головоломка
print u"Это головоломка."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print u"Получается: ", what, u"Вы можете это вычислить вручную?"
