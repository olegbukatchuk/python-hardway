# -*- coding: utf-8 -*-

print u"Ты находишься в темной комнате с двумя дверями. Ты войдёшь в дверь №1 или №2?"

door = raw_input("> ")

if door == "1":
    print u"В этой комнате гигантский медведь поедает чизкейк. Твои действия?"
    print u"1. Отберешь чизкейк."
    print u"2. Крикнешь медведю в ухо."

    bear = raw_input("> ")

    if bear == "1":
        print u"Медведь укусил тебя за голову. Отличная работа!"
    elif bear == "2":
        print u"Медведь укусил тебя за ногу. Отличная работа!"
    else:
        print u"Прекрасно, это действие %s было единственным верным. Медведь убежал прочь." % bear

elif door == "2":
    print u"Ты смотришь в бесконечную пропасть глаз Ктулху. Твои действия?"
    print u"l. Рассказать Ктулху про чернички."
    print u"2. Потрепать желтые заклепки на куртке."
    print u"3. С помощью револьвера насвистеть мелодии."

    insanity = raw_input("> ")

    if insanity =="1" or insanity == "2":
        print u"Твое тело спасено благодаря тому, что Ктулху превратился в желе. Отличная работа!"
    else:
        print u"Безумие охватило тебя, и ты упал в бассейн с грязью. Отличная работа!"

else:
    print u"Безумие охватило тебя, и ты выстрелил себе в ухо. Отличная работа!"
