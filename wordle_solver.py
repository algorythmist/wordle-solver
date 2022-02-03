import random
from collections import Counter


def random_word(dictionary: list):
    """
    Pick a random word from a dictionary
    :param dictionary: a list of wirds
    :return: one of the words
    """
    return dictionary[random.randrange(0, len(dictionary))]


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
    return [word for word in dictionary if all_letters_are_distinct(word) and has_vowels(word, 3)]


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
    return [w for w in dictionary if filter_word(w, score, guess)]


def is_solved(score: list) -> bool:
    return sum(score) == len(score)


def solve(secret_word, five_letter_words):
    guesses = []
    words_remaining = five_letter_words
    for i in range(6):
        if i == 0:
            guess = random_word(initial_guesses(words_remaining))
        else:
            guess = random_word(words_remaining)
        print('Guess: '+guess)
        guesses.append(guess)

        score = score_guess(secret_word, guess)
        print(f'Score = {score}')
        if is_solved(score):
            print("FOUND IT!")
            break
        words_remaining = filter_dictionary(words_remaining, score, guess)
    return guesses


def read_dictionary(filename='words_alpha.txt', word_length=5):
    with open(filename, 'r') as file:
        words = file.readlines()
    specific_words = [w.strip().upper() for w in words if len(w.strip()) == word_length]
    return specific_words




