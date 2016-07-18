# -*- coding: utf-8 -*-
import codecs

from datatypes import default_list_dict, Kaomoji, Emoji, SOURCE_MOZC


def iter_tsv(path, width):
    with codecs.open(path, 'rb', 'utf-8') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('# ') or not line:
                continue

            # Make sure data is of a constant width
            yield_me = line.split('\t')
            if len(yield_me) < width:
                yield_me += (None,)*(width-len(yield_me))
            yield yield_me


cat_map = {
    'SMILE': u'笑い',
    'SWEAT': u'汗',
    'SURPRISE': u'感嘆',
    'SADNESS': u'悲しみ',
    'DISPLEASURE': u'不満',

    'OTHER': u'その他',
    'NATURE': u'自然界',
    'ACTIVITY': u'活動',
    'FACE': u'顔',
    'CITY': u'都市',
    'FOOD': u'食べ物'
}


def get_kaomoji_data():
    """
    Get the categorized kaomoji data from mozc
    """
    map_kaomoji = {}

    for kaomoji, cat, keys in iter_tsv('data/mozc/categorized.tsv', 3):
        if not kaomoji in map_kaomoji:
            map_kaomoji[kaomoji] = Kaomoji(
                SOURCE_MOZC,
                kaomoji,
                [],
                keys.split()
            )

        km = map_kaomoji[kaomoji]
        km.cats.extend(cat_map[i_cat] for i_cat in cat.split())
        km.keys.extend(keys.split())

    return map_kaomoji


def get_emoji_data():
    map_emoji = {}
    map_cats = default_list_dict()
    map_words = default_list_dict()

    for (
        _, char, _, _, _, _, yomi,
        keys_uni, key_ja, key_docomo, key_softbank, key_kddi,
        cat_mozc
    ) in iter_tsv('data/mozc/emoji_data.tsv', 13):
        print char, yomi, keys_uni, key_ja, key_docomo, key_softbank, key_kddi, cat_mozc
        if not char:
            continue

        # Format for category is (english category)-(mozc ID)
        # The mozc ID probably isn't useful outside mozc
        assert not ' ' in cat_mozc
        cat = cat_map[cat_mozc.split('-')[0]]

        add_me = Emoji(
            char,
            [cat],
            # NOTE: key_uni is in English, the others are in Japanese
            [i.strip() for i in {key_ja, key_docomo, key_softbank} if i.strip()],
            keys_uni
        )

        assert not char in map_emoji
        map_emoji[char] = add_me
        if cat.strip():
            map_cats[cat].append(add_me)

        for name in add_me.keys:
            for word in name.split():
                if not word.strip():
                    continue
                map_words[word.strip()].append(add_me)

    return map_emoji, map_cats, map_words


if __name__ == '__main__':
    get_kaomoji_data()
    get_emoji_data()

