# -*- coding: utf-8 -*-

def cheese_and_crackers(cheeese_count, boxes_of_crackers):
    print u"У нас есть %d бутылок лимонада!" % cheeese_count
    print u"У нас есть %d коробок чипсов!" % boxes_of_crackers
    print u"Этого достаточно для вечеринки!"
    print u"Поехали!\n"

print u"ИЛИ, мы можем использовать переменные из нашего сценария:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print u"Мы даже можем выполнять вичисления внутри функции:"
cheese_and_crackers(10 + 20, 5 + 6)

print u"И объединять переменные с вычислениями:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
