directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')


def get_tuple(word):
    lower_cased = word.lower()

    if lower_cased in directions:
        return 'direction', lower_cased
    elif lower_cased in verbs:
        return 'verb', lower_cased
    elif lower_cased in stop_words:
        return 'stop', lower_cased
    elif lower_cased in nouns:
        return 'noun', lower_cased
    elif lower_cased.isdigit():
        return 'number', int(lower_cased)
    else:
        # in case of error, return word with original casing
        return 'error', word


def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]
