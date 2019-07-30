spam = ['apples', 'bananas', 'tofu', 'cats']


def list_things(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])


print(list_things(spam))
