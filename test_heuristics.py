import unittest

from dictionary import read_dictionary
from wordle_solver import *
from heuristics import OneStepLookaheadSolver, evaluate_guess


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


    # def test_solver_accuracy(self):
    #     five_letter_words = read_dictionary()
    #     trials = 50
    #     successes = 0
    #     total_score = 0
    #     for i in range(trials):
    #         secret_word = random_word(five_letter_words)
    #         scorer = Scorer(secret_word)
    #         # TODO: pass solver as param
    #         guesses = OneStepLookaheadSolver(scorer).solve(five_letter_words)
    #
    #         guess = guesses[-1]
    #         if guess == secret_word:
    #             successes += 1
    #             total_score += len(guesses)
    #
    #     success_rate = float(successes) / trials
    #     average_score = float(total_score) / successes
    #     print(f'\nSuccess rate = {success_rate:.2}')
    #     print(f'Average Score = {average_score}')