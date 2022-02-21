import unittest

from heuristics import OneStepLookaheadSolver, evaluate_guess
from wordle_solver import *


class HeuristicsTestCase(unittest.TestCase):

    def test_evaluate_guess(self):
        five_letter_words = read_dictionary()
        self.assertEqual(2315, len(five_letter_words))
        value = evaluate_guess('TEPID', five_letter_words)
        print(value)
        value = evaluate_guess('WORDY', five_letter_words)
        print(value)

    def test_lookahead_solver(self):
        five_letter_words = read_dictionary('words_alpha.txt')
        secret_word = 'TEPID'
        scorer = Scorer(secret_word)
        solver = OneStepLookaheadSolver(scorer)
        guesses = solver.solve(five_letter_words)
        guess = guesses[-1]
        self.assertEqual('TEPID', guess)
        iterations = len(guesses)
        print(f'\nFound the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

    def no_test_solver_accuracy(self):
        trials = 100
        success_rate, average_score = evaluate_solver('wordle_dict.txt', trials,
                                                      lambda scorer: OneStepLookaheadSolver(scorer))
        print(f'\nSuccess rate = {success_rate:.2}')
        print(f'Average Score = {average_score}')

    def no_test_solver_accuracy_large_dict(self):
        trials = 100
        success_rate, average_score = evaluate_solver('words_alpha.txt', trials,
                                                      lambda scorer: OneStepLookaheadSolver(scorer,
                                                                                            threshold=300,
                                                                                            max_sample_size=1000))
        print(f'\nSuccess rate = {success_rate:.2}')
        print(f'Average Score = {average_score}')

    # def test_solver_repeated_letter(self):
    #     five_letter_words = read_dictionary('words_alpha.txt')
    #     secret_word = 'BULLS'
    #     scorer = Scorer(secret_word)
    #     guesses = BruteForceSolver(scorer).solve(five_letter_words)
    #     guess = guesses[-1]
    #     self.assertEqual(secret_word, guess)
    #     iterations = len(guesses)
    #     print(f'Found the solution {guess} in {iterations} iterations')
    #     self.assertEqual(secret_word, guess)
