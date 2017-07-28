# -*- coding: utf-8 -*-

import codecs, sys
outf = codecs.getwriter('utf-8')(sys.stdout, errors='replace')
sys.stdout = outf

from sys import argv

script, user_name = argv
prompt = '> '

print u"Привет %s, Я - сценарий %r." % (user_name, script)
print u"Я хочу задать тебе несколько вопросов."
print u"Я тебе нравлюсь, %s?" % user_name
likes = raw_input(prompt).decode(sys.stdin.encoding or locale.getpreferredencoding(True))

print u"Где ты живешь, %s?" % user_name
lives = raw_input(prompt).decode(sys.stdin.encoding or locale.getpreferredencoding(True))

print u"На каком компьютере ты работаешь?"
computer = raw_input(prompt).decode(sys.stdin.encoding or locale.getpreferredencoding(True))

print u"""
Итак, ты ответил %s на вопрос, нравлюсь ли я тебе.
Ты живешь в %s. Я знаю, где это.
И у тебя есть компьютер %s. Прекрасно!
""" % (likes, lives, computer)
