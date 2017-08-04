# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats:
    print u"Слишком много кошек! Мир обречён!"

if people > cats:
    print u"Не так много кошек! Мир спасён!"

if people > dogs:
    print u"Мир сухой!"

dogs += 5

if people >= dogs:
    print u"Людей больше или столько же, сколько собак."

if people <= dogs:
    print u"Людей больше или столько же сколько собак."

if people == dogs:
    print u"Людей стлько же, сколько собак."
