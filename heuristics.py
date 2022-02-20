from wordle_solver import WordleSolver, random_word, Scorer, filter_dictionary


def evaluate_guess(guess, current_dictionary):
    """
    Compute the average length of the new dictionary given a guess
    :param guess:
    :param current_dictionary:
    :return:
    """
    new_length = 0
    for word in current_dictionary:
        if word == guess:
            continue
        # TODO: resolve ties
        scorer = Scorer(word)
        score = scorer.score(guess)
        new_dict = filter_dictionary(current_dictionary, score)
        new_length += len(new_dict)
    return float(new_length) / len(current_dictionary)


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
            return 'CRANE'
        if len(words_remaining) < self.threshold:
            return find_best_word(words_remaining, self.evaluate_fn)
        return random_word(words_remaining)







