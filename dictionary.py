def read_dictionary(filename='wordle_dict.txt', word_length=5):
    with open(filename, 'r') as file:
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


def filter_dictionary(dictionary, score) -> bool:
    return {w for w in dictionary if filter_word(w, score)}







