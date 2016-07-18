# -*- coding: utf-8 -*-
import random
import cherrypy

from data.combine_kaomoji import combine_kaomoji, most_common_keys
from data.parse_kaomoji_guess import parse_kaomoji_guess

from web_base import WebBase
from levenshtein import levenshtein


map_kaomoji, map_keywords, map_cats = combine_kaomoji()
mc_keywords = most_common_keys(map_keywords)
mc_cats = most_common_keys(map_cats)

kaomoji_guess_list = parse_kaomoji_guess()


class Kaomoji(object, WebBase):
    def __init__(self, parent):
        self.category = KaomojiCategory()
        self.keyword = KaomojiKeyword()

    @cherrypy.expose
    def index(self):
        return self._template('kaomoji.html', {
            'keywords': self._add_random(mc_keywords, map_keywords),
            'cats': self._add_random(mc_cats, map_cats),
            'random_kaomoji': random.choice(map_kaomoji.keys())
        })


    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        map_kaomoji[name]

        similar_kaomoji = sorted(
            (levenshtein(name, i), abs(len(i)-len(name)), i)
            for i in kaomoji_guess_list
        )[:100]
        similar_kaomoji = [i[-1] for i in similar_kaomoji]

        return self._template('kaomoji/kaomoji_item.html', {
            'cur_kaomoji': name,
            'kaomoji_list': map_kaomoji[name],
            'similar_kaomoji': similar_kaomoji
        })


class KaomojiCategory(object, WebBase):
    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        random.shuffle(map_cats[name])
        return self._template('kaomoji/keyword.html', {
            'trail_header': u'カテゴリー',
            'keyword': name,
            'kaomoji_list': [map_kaomoji[i] for i in map_cats[name]]
        })


class KaomojiKeyword(object, WebBase):
    @cherrypy.expose
    def default(self, name):
        name = name.decode('utf-8')
        random.shuffle(map_keywords[name])
        return self._template('kaomoji/keyword.html', {
            'trail_header': u'キーワード',
            'keyword': name,
            'kaomoji_list': [map_kaomoji[i] for i in map_keywords[name]]
        })

