from collections import defaultdict, namedtuple

default_list_dict = lambda: defaultdict(lambda: [])

Kaomoji = namedtuple('Kaomoji', ['source', 'kaomoji', 'cats', 'keys'])
Emoji = namedtuple('Emoji', ['emoji', 'cats', 'keys', 'engnames'])

SOURCE_MOZC = 0
SOURCE_ANTHY_KAOMOJI = 1
SOURCE_KAO_UTF8 = 2
