import random
from collections import Counter

from wordle.dictionary import filter_dictionary
from wordle.wordle_scorer import Scorer


class WordleSolver:

    def __init__(self, scorer: Scorer):
        self.scorer = scorer

    def guess_next_word(self, words_remaining, trial):
        """
        Generate a guess given the current dictionary
        :param words_remaining: the current dictionary of valid words
        :param trial: the trial number
        :return: a word from the current dictionary
        """
        pass


def play_wordle(dictionary, secret, solver: WordleSolver):
    scorer = Scorer(secret)
    guesses = []
    words_remaining = dictionary
    for i in range(6):
        guess = solver.guess_next_word(words_remaining, i)
        guesses.append(guess)
        score = scorer.score(guess)
        if secret == guess:
            break
        words_remaining = filter_dictionary(words_remaining, score)
    return guesses


class NaiveSolver(WordleSolver):

    def __init__(self, scorer: Scorer, opener='SLATE'):
        super(NaiveSolver, self).__init__(scorer)
        self.opener = opener

    def guess_next_word(self, words_remaining, trial):
        if trial == 0:
            return self.opener
        return random_word(words_remaining)


def random_word(dictionary):
    """
    Pick a random word from a dictionary
    :param dictionary: a list of words
    :return: one of the words
    """
    return random.choice(tuple(dictionary))


def all_letters_are_distinct(word: str) -> bool:
    return len(Counter(word).values()) == len(word)


def is_vowel(char) -> bool:
    return char in 'AEIOUY'


def has_vowels(word: str, number_of_vowels: int) -> bool:
    return sum([is_vowel(char) for char in word]) == number_of_vowels


def initial_guesses(dictionary):
    """
    Pick words that have all distinct letters and 3 vowels
    :param dictionary:
    :return:
    """
    return {word for word in dictionary if all_letters_are_distinct(word) and has_vowels(word, 3)}
