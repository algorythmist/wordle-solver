import random
from collections import Counter


class Scorer:

    def __init__(self, secret: str):
        self.secret = secret

    def score(self, word: str):
        return score_guess(self.secret, word)


class WordleSolver:

    def __init__(self, scorer: Scorer):
        self.scorer = scorer

    def guess_next_word(self, words_remaining, trial):
        pass

    def solve(self, dictionary):
        guesses = []
        words_remaining = set(dictionary)
        for i in range(6):
            guess = self.guess_next_word(words_remaining, i)
            guesses.append(guess)
            score = self.scorer.score(guess)
            if is_solved(score):
                break
            words_remaining = filter_dictionary(words_remaining, score, guess)
        return guesses


class BruteForceSolver(WordleSolver):

    def __init__(self, scorer: Scorer):
        super(BruteForceSolver, self).__init__(scorer)

    def guess_next_word(self, words_remaining, trial):
        if trial == 0:
            return random_word(initial_guesses(words_remaining))
        return random_word(words_remaining)


def evaluate_guess(guess, dictionary):
    penalty = 0
    for word in dictionary:
        if word == guess:
            continue
        # TODO: resolve ties
        scorer = Scorer(word)
        score = scorer.score(guess)
        new_dict = filter_dictionary(dictionary, score, guess)
        penalty += len(new_dict)
    return float(penalty) / len(dictionary)


def find_best_word(dictionary, evaluate_fn):
    min_penalty = 1000000
    best_word = None
    for word in dictionary:
        penalty = evaluate_fn(word, dictionary)
        if penalty < min_penalty:
            min_penalty = penalty
            best_word = word
    return best_word


class OneStepLookaheadSolver(WordleSolver):

    def __init__(self, scorer: Scorer, evaluate_fn=evaluate_guess, threshold=200):
        super(OneStepLookaheadSolver, self).__init__(scorer)
        self.evaluate_fn = evaluate_fn
        self.threshold = threshold

    def guess_next_word(self, words_remaining, trial):
        if trial == 0:
            return random_word(initial_guesses(words_remaining))
        if len(words_remaining) < self.threshold:
            return find_best_word(words_remaining, self.evaluate_fn)
        return random_word(words_remaining)


def random_word(dictionary: list):
    """
    Pick a random word from a dictionary
    :param dictionary: a list of wirds
    :return: one of the words
    """
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


def score_guess(secret_word: str, guess: str) -> list:
    """
    Score a guess against the actual word
    The score codes mean
    -1: Letter is not in the word
    0: The letter is in the word but at a different place
    1: The letter is at the right place
    :param secret_word: The secret word
    :param guess: The guess
    :return: A list of score values - one for each letter
    """
    score = [-1 for _ in range(0, len(guess))]
    for i in range(0, len(guess)):
        if secret_word[i] == guess[i]:
            score[i] = 1
        elif guess[i] in secret_word:
            score[i] = 0
    return score


def filter_word(word: str, score: list, guess: str) -> bool:
    for i in range(0, len(score)):
        if score[i] == -1 and guess[i] in word:
            return False
        if score[i] == 0 and (not (guess[i] in word) or guess[i] == word[i]):
            return False
        if score[i] == 1 and not (guess[i] == word[i]):
            return False
    return True


def filter_dictionary(dictionary: list, score: list, guess: str) -> bool:
    return {w for w in dictionary if filter_word(w, score, guess)}


def is_solved(score: list) -> bool:
    return sum(score) == len(score)


def read_dictionary(filename='words_alpha.txt', word_length=5):
    with open(filename, 'r') as file:
        words = file.readlines()
    specific_words = [w.strip().upper() for w in words if len(w.strip()) == word_length]
    return specific_words


