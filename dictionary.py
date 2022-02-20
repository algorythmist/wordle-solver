import string
from itertools import chain


def filter_word(word: str, score: dict) -> bool:
    for i, (letter, value) in enumerate(score):
        if value == -1 and letter in word:
            return False
        if value == 0 and (not (letter in word) or letter == word[i]):
            return False
        if value == 1 and not (letter == word[i]):
            return False
    return True


def filter_dictionary(dictionary: set, score: dict) -> bool:
    return {w for w in dictionary if filter_word(w, score)}


class Dictionary:

    def filter(self, score, word: str):
        pass


class SetDictionary(Dictionary):

    def __init__(self, words):
        self.words = set(words)

    def __len__(self):
        return len(self.words)

    def filter(self, score, word):
        return SetDictionary(filter_dictionary(self.words, score, word))


def matches_exact_letters(word, score):
    for i, (letter, value) in enumerate(score.items()):
        if value == 1 and word[i] != letter:
            return False
    return True

class MapDictionary(Dictionary):

    def __init__(self, words):
        self.words = {}
        self.size = len(words)
        for word in words:
            for letter in word:
                words_with_letter = self.words.get(letter, set())
                words_with_letter.add(word)
                self.words[letter] = words_with_letter

    def __len__(self):
        return self.size

    def filter(self, score):
        contains = [self.words[letter] for (letter, value) in score.items() if value >= 0]
        contains = set().union(*contains)
        print(contains)
        not_contains = [self.words[letter] for (letter, value) in score.items() if value < 0]
        not_contains = set(chain(*not_contains))
        print(not_contains)
        reduced_dictionary = contains.difference(not_contains)
        print(reduced_dictionary)
        exact_matches = [word for word in reduced_dictionary if matches_exact_letters(word, score)]
        return MapDictionary(exact_matches)







