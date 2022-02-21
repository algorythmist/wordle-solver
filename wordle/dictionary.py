import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, '../data')


def read_dictionary(filename: str='wordle_dict.txt', word_length: int=5) -> list:
    """
    Read a list of words from a file.
    :param filename: the name of the file
    :param word_length: keep only words of this length
    :return: the list of words of the specified length, in uppercase
    """
    with open(os.path.join(DATA_DIR, filename), 'r') as file:
        words = file.readlines()
    specific_words = [w.strip().upper() for w in words if len(w.strip()) == word_length]
    return specific_words


def filter_word(word: str, score: dict) -> bool:
    for i, (letter, value) in enumerate(score):
        if value == -1 and letter in word:
            return False
        if value == 0 and (letter not in word or letter == word[i]):
            return False
        if value == 1 and not (letter == word[i]):
            return False
    return True


def filter_dictionary(dictionary, score) -> set:
    """
    Filter the dictionary of allowed words based on the score
    :param dictionary: the current dictionary
    :param score: the wordle score
    :return: the subset of the dictionary that is consistent with the score
    """
    return {w for w in dictionary if filter_word(w, score)}







