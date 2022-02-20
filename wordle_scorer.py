class Scorer:

    def __init__(self, secret: str):
        self.secret = secret

    def score(self, guess: str):
        """
        Score a guess against the actual word
        The score codes mean
        -1: Letter is not in the word
        0: The letter is in the word but at a different place
        1: The letter is at the right place
        :param guess: The guess
        :return: A list of pairs of letters to score values
        """
        score = [(letter, -1) for letter in guess]
        for i, letter in enumerate(guess):
            if self.secret[i] == guess[i]:
                score[i] = (letter, 1)
            elif guess[i] in self.secret:
                score[i] = (letter, 0)
        return score

    def is_solved(self, word):
        return self.secret == word
