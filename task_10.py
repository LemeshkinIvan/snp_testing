import re

def count_words(string):
    try:
        # в регулярку запихнул то, что требуется очистить для теста и немного рандома
        array_after_re = re.split(r'[,?|!\s-]', string)
        words = []

        for el in array_after_re:
            # "удалит" за нас еще и пустые элементы
            words.append(el.lower())

        result = {}
        keys = set(words)

        for k in keys:
            if k.isalnum():
                result.update({k: words.count(k)})

        return result
    except:
        pass

# for test
print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))