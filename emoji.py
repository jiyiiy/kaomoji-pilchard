# -*- coding: utf-8 -*-
import cherrypy
import random

from data.parse_mozc import get_emoji_data
from data.combine_kaomoji import most_common_keys
from web_base import WebBase

map_emoji, map_emoji_cats, map_emoji_words = get_emoji_data()
mc_emoji_cats = most_common_keys(map_emoji_cats)
mc_emoji_words = most_common_keys(map_emoji_words)


class Emoji(WebBase):
    def __init__(self, parent):
        self.category = EmojiCategory()
        self.keyword = EmojiKeyword()


    @cherrypy.expose
    def index(self):
        return self._template('emoji.html', {
            'random_emoji': random.choice(map_emoji.keys()),

            'emoji_cats': self._add_random(mc_emoji_cats, map_emoji_cats),
            'emoji_words': self._add_random(mc_emoji_words, map_emoji_words)
        })


    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        map_emoji[name]

        return self._template('emoji/emoji_item.html', {
            'cur_emoji': name,
            'emoji': map_emoji[name]
        })


class EmojiCategory(object, WebBase):
    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        random.shuffle(map_emoji_cats[name])
        print map_emoji_cats[name]
        return self._template('emoji/keyword.html', {
            'trail_header': u'カテゴリー',
            'keyword': name,
            'emoji_list': map_emoji_cats[name]
        })


class EmojiKeyword(object, WebBase):
    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        random.shuffle(map_emoji_words[name])
        print map_emoji_words[name]
        return self._template('emoji/keyword.html', {
            'trail_header': u'キーワード',
            'keyword': name,
            'emoji_list': map_emoji_words[name]
        })
