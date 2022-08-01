import re


class Morph:

    def __init__(self, *args) -> None:
        self.word_forms = list(map(str.lower, args))

    def add_word(self, word: str) -> None:
        self.word_forms.append(word)

    def get_words(self) -> tuple:
        return tuple(self.word_forms)

    def __eq__(self, other: str) -> bool:
        return other.lower() in self.word_forms


def get_list_of_words(string: str) -> list:
    regex = r"\b\w+\b"
    return re.findall(regex, string)

words = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in words.splitlines()]

text = input()

text_list = list(map(str.lower, get_list_of_words(text)))

count = 0
for word in text_list:
    for w in dict_words:
        if word == w:
            count += 1
            break

print(count)
