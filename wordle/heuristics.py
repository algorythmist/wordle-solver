from wordle.wordle_solver import WordleSolver, random_word, Scorer, filter_dictionary
import random


def evaluate_guess(guess, current_dictionary):
    """
    Compute the average length of the new dictionary given a guess
    :param guess:
    :param current_dictionary:
    :return:
    """
    new_length = 0
    for secret in current_dictionary:
        if secret == guess:
            continue
        scorer = Scorer()
        score = scorer.score(secret, guess)
        new_dict = filter_dictionary(current_dictionary, score)
        new_length += len(new_dict)
    return float(new_length) / len(current_dictionary)


# TODO: resolve ties
def find_best_word(dictionary, evaluate_fn, max_sample_size):
    min_penalty = 1000000
    best_word = None
    word_sample = dictionary
    if max_sample_size is not None and len(dictionary) > max_sample_size:
        word_sample = random.sample(dictionary, max_sample_size)
    for word in word_sample:
        penalty = evaluate_fn(word, dictionary)
        if penalty < min_penalty:
            min_penalty = penalty
            best_word = word
    return best_word


class OneStepLookaheadSolver(WordleSolver):

    def __init__(self, scorer: Scorer,
                 evaluate_fn=evaluate_guess,
                 threshold=200,
                 max_sample_size=None):
        self.scorer = scorer
        self.evaluate_fn = evaluate_fn
        self.threshold = threshold
        self.max_sample_size = max_sample_size

    def guess_next_word(self, words_remaining, trial):
        if trial == 0:
            return 'SLATE'
        if len(words_remaining) < self.threshold:
            return find_best_word(words_remaining, self.evaluate_fn, self.max_sample_size)
        return random_word(words_remaining)







