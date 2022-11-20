import unittest

from wordle.wordle_solver import *
from wordle.dictionary import read_dictionary
from wordle.performace_evaluator import evaluate_solver


class SolverTestCase(unittest.TestCase):

    def test_all_letters_are_distinct(self):
        self.assertTrue(all_letters_are_distinct('abcd'))
        self.assertFalse(all_letters_are_distinct('abcdefa'))

    def test_has_vowels(self):
        self.assertTrue(has_vowels('LEAKY', 3))
        self.assertFalse(has_vowels('LEAKY', 2))
        self.assertFalse(has_vowels('GRAMMY', 3))

    def test_initial_guesses(self):
        five_letter_words = read_dictionary()
        guesses = initial_guesses(five_letter_words)
        self.assertEqual(192, len(guesses))
        for guess in guesses:
            self.assertTrue(all_letters_are_distinct(guess))

    def test_brute_force_solver(self):
        five_letter_words = read_dictionary()
        secret_word = 'TEPID'
        solver = NaiveSolver()
        guesses = play_wordle(five_letter_words, secret_word, solver)
        guess = guesses[-1]
        self.assertEqual('TEPID', guess)
        iterations = len(guesses)
        print(f'\nFound the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

    def test_solver_accuracy(self):
        success_rate, average_score, stdev = evaluate_solver('wordle_dict.txt', 1000,
                                                             lambda scorer: NaiveSolver())
        print(f'\nSuccess rate = {success_rate:.2}')
        print(f'Average Score = {average_score}')
        print(f'Standard deviation = {stdev}')
        self.assertTrue(success_rate >= 0.98)
        self.assertTrue(average_score < 4)

    def test_solver_accuracy_large_dictionary(self):
        success_rate, average_score, stdev = evaluate_solver('full_dict.txt', 1000,
                                                             lambda scorer: NaiveSolver())
        print(f'\nSuccess rate = {success_rate:.2}')
        print(f'Average Score = {average_score}')
        print(f'Standard deviation = {stdev}')
        self.assertTrue(success_rate >= 0.84)
        self.assertTrue(average_score < 5)

    def test_solver_repeated_letter(self):
        five_letter_words = read_dictionary()
        secret_word = 'GASSY'
        solver = NaiveSolver()
        guesses = play_wordle(five_letter_words, secret_word, solver)
        guess = guesses[-1]
        self.assertEqual(secret_word, guess)
        iterations = len(guesses)
        print(f'Found the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)
