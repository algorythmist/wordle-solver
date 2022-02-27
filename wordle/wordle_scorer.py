import pickle


def score_guess(secret: str, guess: str):
    score = [(letter, -1) for letter in guess]
    for i, letter in enumerate(guess):
        if secret[i] == guess[i]:
            score[i] = (letter, 1)
        elif guess[i] in secret:
            score[i] = (letter, 0)
    return score


def score_secret(dictionary, secret):
    """
    Create a score for this secret and every word on the dictionary
    """
    return {guess: score_guess(secret, guess) for guess in dictionary}


def score_all(dictionary, filename):
    """
    Create a score lookup for all secret/guess scores and store in a file
    """
    lookup = {secret: score_secret(dictionary, secret) for secret in dictionary}
    pickle.dump(lookup, open(filename, "wb"))
    return lookup


class Scorer:

    def score(self, secret: str, guess: str):
        """
        Score a guess against the actual word
        The score codes mean
        -1: Letter is not in the word
        0: The letter is in the word but at a different place
        1: The letter is at the right place
        :param guess: The guess
        :return: A list of pairs of letters to score values
        """
        return score_guess(secret, guess)

    def is_solved(self, word):
        return self.secret == word


class MemoryScorer:

    def __init__(self, filename: str):
        self.lookup = pickle.load(open(filename, 'rb'))

    def score(self, secret: str, guess: str):
        return self.lookup[secret][guess]

    def is_solved(self, word):
        return self.secret == word
