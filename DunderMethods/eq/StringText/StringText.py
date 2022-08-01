import re
from pprint import pprint


class StringText:

    def __init__(self, lst_words: list) -> None:
        self.lst_words = lst_words
        self.len = len(self)

    def __len__(self) -> int:
        return len(self.lst_words)

    def __ge__(self, other) -> bool:
        return len(self) >= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    @staticmethod
    def get_list_of_words(string: str) -> list:
        regex = r"\b\w+\b"
        return re.findall(regex, string)


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_text = [StringText(StringText.get_list_of_words(line)) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [" ".join(str_text.lst_words) for str_text in lst_text_sorted]
pprint(lst_text_sorted)