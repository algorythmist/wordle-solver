import random
from collections import Counter
from dictionary import read_dictionary, filter_dictionary
from wordle_scorer import Scorer


class WordleSolver:

    def __init__(self, scorer: Scorer):
        self.scorer = scorer

    def guess_next_word(self, words_remaining, trial):
        pass

    def solve(self, dictionary):
        guesses = []
        words_remaining = dictionary
        for i in range(6):
            guess = self.guess_next_word(words_remaining, i)
            guesses.append(guess)
            score = self.scorer.score(guess)
            #TODO print(guess, score)
            if self.scorer.is_solved(guess):
                break
            words_remaining = filter_dictionary(words_remaining, score)
        return guesses


class BruteForceSolver(WordleSolver):

    def __init__(self, scorer: Scorer, opener='SLATE'):
        super(BruteForceSolver, self).__init__(scorer)
        self.opener = opener

    def guess_next_word(self, words_remaining, trial):
        if trial == 0:
            return self.opener
        return random_word(words_remaining)


def random_word(dictionary):
    """
    Pick a random word from a dictionary
    :param dictionary: a list of wirds
    :return: one of the words
    """
    # TODO: Sampling from a set is deprecated. Find new way
    return random.sample(dictionary, 1)[0]


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


def evaluate_solver(dictionary_filename,
                    trials,
                    solver_factory):
    five_letter_words = read_dictionary(dictionary_filename)
    successes = 0
    total_score = 0
    for i in range(trials):
        secret_word = random_word(five_letter_words)
        scorer = Scorer(secret_word)
        solver = solver_factory(scorer)
        guesses = solver.solve(five_letter_words)

        guess = guesses[-1]
        if guess == secret_word:
            successes += 1
            total_score += len(guesses)

    success_rate = float(successes) / trials
    average_score = float(total_score) / successes
    return success_rate, average_score

