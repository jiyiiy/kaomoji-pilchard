# -*- coding: utf-8 -*-
from simplejson import load

from datatypes import (
    Kaomoji, SOURCE_KAO_UTF8, SOURCE_ANTHY_KAOMOJI
)


def parse_anthy_kaomoji():
    """
    "えがお": [
        "o(^-^)o",
    """
    map_kaomoji = {}


    with open('data/kaomoji_json/anthy_kaomoji.json', 'rb') as f:
        data = load(f, encoding='utf-8')

    for key, kaomojis in data.items():
        for kaomoji in kaomojis:
            if not kaomoji in map_kaomoji:
                map_kaomoji[kaomoji] = Kaomoji(
                    SOURCE_ANTHY_KAOMOJI,
                    kaomoji, [], []
                )

            km = map_kaomoji[kaomoji]
            km.keys.append(key)

    return map_kaomoji


def parse_kao_utf8():
    """
    [
      {
        "annotation": "あぁー",
        "face": "o┤*´Д`*├oｱｧｰ"
      },
    """
    map_kaomoji = {}


    with open('data/kaomoji_json/kao-utf8.json', 'rb') as f:
        data = load(f, encoding='utf-8')

    for km_dict in data:
        kaomoji = km_dict['face']
        key = km_dict['annotation']

        if not kaomoji in map_kaomoji:
            map_kaomoji[kaomoji] = Kaomoji(
                SOURCE_KAO_UTF8,
                kaomoji, [], []
            )

        km = map_kaomoji[kaomoji]
        km.keys.append(key)

    return map_kaomoji


if __name__ == '__main__':
    parse_anthy_kaomoji()
    parse_kao_utf8()


