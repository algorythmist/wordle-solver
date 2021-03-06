from math import sqrt
from typing import Callable

from wordle.dictionary import read_dictionary
from wordle.heuristics import OneStepLookaheadSolver
from wordle.wordle_scorer import Scorer
from wordle.wordle_solver import WordleSolver, random_word, play_wordle


def evaluate_solver(dictionary_filename: str,
                    trials: str,
                    solver_factory: Callable[[Scorer], WordleSolver],
                    scorer=Scorer(),
                    store_failures: str = None):
    five_letter_words = read_dictionary(dictionary_filename)
    successes = 0
    total_score = 0
    sum_of_squares = 0
    failures = []
    for i in range(trials):
        secret_word = random_word(five_letter_words)
        solver = solver_factory(scorer)
        guesses = play_wordle(five_letter_words, secret_word, solver, scorer)

        guess = guesses[-1]
        if guess == secret_word:
            successes += 1
            score = len(guesses)
            total_score += score
            sum_of_squares += score * score
        else:
            failures.append(f'{secret_word}, {guesses}')

    if store_failures:
        with open(store_failures, 'w') as f:
            f.writelines(failures)

    success_rate = float(successes) / trials
    average_score = float(total_score) / successes
    variance = (sum_of_squares / successes) - average_score * average_score
    return success_rate, average_score, sqrt(variance)


def heuristic_solver_accuracy():
    trials = 500
    success_rate, average_score, stdev = evaluate_solver('wordle_dict.txt', trials,
                                                         lambda scorer: OneStepLookaheadSolver(scorer,
                                                                                               threshold=1000),
                                                         store_failures='onestep-failures-small.txt')
    print(f'\nSuccess rate = {success_rate:.2}')
    print(f'Average Score = {average_score}')
    print(f'Standard deviation = {stdev}')


def solver_accuracy_large_dict():
    trials = 200
    success_rate, average_score, stdev = evaluate_solver('full_dict.txt', trials,
                                                         lambda scorer: OneStepLookaheadSolver(scorer,
                                                                                               threshold=400,
                                                                                               max_sample_size=1000),
                                                         store_failures='onestep-failures-full.txt')
    print(f'\nSuccess rate = {success_rate:.2}')
    print(f'Average Score = {average_score}')
    print(f'Standard deviation = {stdev}')


if __name__ == '__main__':

    #heuristic_solver_accuracy()
    # Success rate = 0.99
    # Average Score = 3.524193548387097
    # Standard deviation = 0.7455644070901363

    solver_accuracy_large_dict()
    # Success rate = 0.96
    # Average Score = 4.41036717062635
    # Standard deviation = 0.9524666596558226

