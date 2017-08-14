# -*- coding: utf-8 -*-

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song([u"Не могу я тебе в день рождения", u" Дорогие подарки дарить,", u" Но зато в эти ночи весенние"])

buills_on_parade = Song([u"Далеко-далеко на лугу пасётся кто?", u"Пейте, дети, молоко, будете здоровы!"])

happy_bday.sing_me_a_song()

buills_on_parade.sing_me_a_song()

