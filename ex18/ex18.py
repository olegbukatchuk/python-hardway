# -*- coding: utf-8 -*-

# Похоже на сценарий с argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ок, здесь вместо *args мы делаем следующее
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Пренимает только один аргумент
def print_one(arg1):
    print "arg1: %r" % arg1

# Не принимает аргументов
def print_none():
    print u"А я ничего не принимаю."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
