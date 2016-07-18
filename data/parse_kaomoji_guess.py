from codecs import open


def parse_kaomoji_guess():
    kaomoji = set()

    for line in open('data/kaomoji_guess/kaomozi.txt', 'rb', 'utf-8'):
        line = line.strip()
        if line:
            kaomoji.add(line)

    return sorted(kaomoji)

