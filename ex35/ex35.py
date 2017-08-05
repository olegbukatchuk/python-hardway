# -*- coding: utf-8 -*-

import codecs, sys
outf = codecs.getwriter('utf-8') (sys.stdout, errors='replace')
sys.stdout = outf

from sys import exit

def gold_room():
    print u"Здесь полно золота. Сколько кг ты унесёшь?"

    next = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredenoding(True))

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead(u"Эй, ввести надо число!")

    if how_much < 50:
        print u"Шикарно! Ты не жадный, поэтому выигрываешь!"
        exit(0)
    else:
        dead(u"Ах ты жадина!")

def bear_room():
    print u"Здесь сидит медведь."
    print u"У мендведя бочка с медом."
    print u"Медведь закрыл собой дверь выхода."
    print u"Как переместить медведя? Отобрать мед или подразнить медведя?"
    bear_moved = False

    while True:
        next = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredenoding(True))

        if next == u"Отобрать мёд":
            dead(u"Медведь посмотрел на тебя и ударил лапой по лицу.")
        elif next == u"Подразнить медведя" and not bear_moved:
            print u"Медведь отошёл от двери. Вы можете войти в неё. Подразнить медведя или войти в дверь?"
            bear_moved = True
        elif next == u"Подразнить медведя" and bear_moved:
            dead(u"Медведь разозлился и откусил тебе ногу.")
        elif next == u"Войти в дверь" and bear_moved:
            gold_room()
        else:
            print u"Понятия не имею, что происходит."

def cthulhu_room():
    print u"Ha вас смотрит великий и ужасный Ктулху."
    print u"Он смотрит на тебя, и ты начинаешь сходить с ума."
    print u"Убежать или съесть свою голову?"

    next = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredenoding(True))

    if u"Убежать" in next:
        start()
    elif u"Съесть свою голову" in next:
        dead(u"Хм, а это даже и вкусно!")
    else:
        cthulhu_room()

def dead(why):
    print why, u"Великолепно!"
    exit(0)

def start():
    print u"Ты в темной комнате."
    print u"Отсюда ведут две двери, налево и направо."
    print u"Куда ты повернешь?"

    next = raw_input("> ").decode(sys.stdin.encoding or locale.getpreferredenoding(True))

    if next == u"Налево":
        bear_room()
    elif next == u"Направо":
        cthulhu_room()
    else:
        dead(u"Ты ходишь из комнаты в комнату, пока не умираешь с голоду.")

start()
