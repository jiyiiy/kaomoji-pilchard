# TODO: Go through, remove dupes and combine!!

SOURCE_MOZC = 0

from itertools import chain
from datatypes import default_list_dict
from parse_kaomoji_json import parse_kao_utf8, parse_anthy_kaomoji
from parse_mozc import get_kaomoji_data


def combine_kaomoji():
    datas = (
        parse_kao_utf8(),
        parse_anthy_kaomoji(),
        get_kaomoji_data()
    )

    map_kaomoji = default_list_dict()
    map_keys = default_list_dict()
    map_cats = default_list_dict()

    for k in set(chain.from_iterable([i.keys() for i in datas])):
        all_keys = set()
        all_cats = set()

        for i in datas:
            if not k in i:
                continue

            #print k, i[k]
            map_kaomoji[k].append(i[k])
            all_keys.update(i[k].keys)
            all_cats.update(i[k].cats)

            i[k].cats[:] = sorted(set(i[k].cats))
            i[k].keys[:] = sorted(set(i[k].keys))


        for key in all_keys:
            map_keys[key].append(k)

        for cat in all_cats:
            map_cats[cat].append(k)


    return map_kaomoji, map_keys, map_cats


def most_common_keys(d):
    s = []

    for k, v in d.items():
        s.append((k, len(v)))

    return sorted(s, key=lambda i: (-i[1], i[0]))

def print_most_common(d):
    l = most_common_keys(d)

    for k, amount in l:
        print k, amount


if __name__ == '__main__':
    map_kaomoji, map_keys, map_cats = combine_kaomoji()

    #from pprint import pprint
    #pprint(dict(map_kaomoji))
    #pprint(dict(map_keys))
    #pprint(dict(map_cats))

    #print_most_common(map_kaomoji)
    print_most_common(map_keys)
    print_most_common(map_cats)

