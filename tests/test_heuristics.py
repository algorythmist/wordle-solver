import unittest

from wordle.heuristics import OneStepLookaheadSolver, evaluate_guess
from wordle.wordle_solver import *
from wordle.dictionary import read_dictionary
from wordle.performace_evaluator import evaluate_solver
from wordle.wordle_scorer import LookupScorer

class HeuristicsTestCase(unittest.TestCase):

    def test_evaluate_guess(self):
        five_letter_words = read_dictionary()
        self.assertEqual(2315, len(five_letter_words))
        value = evaluate_guess('TEPID', five_letter_words)
        print(value)
        value = evaluate_guess('WORDY', five_letter_words)
        print(value)

    def test_lookahead_solver(self):
        five_letter_words = read_dictionary('full_dict.txt')
        secret_word = 'TEPID'
        scorer = Scorer()
        solver = OneStepLookaheadSolver(scorer)
        guesses = play_wordle(five_letter_words, secret_word, solver)
        guess = guesses[-1]
        self.assertEqual('TEPID', guess)
        iterations = len(guesses)
        print(f'\nFound the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

    def test_solver_repeated_letter(self):
        five_letter_words = read_dictionary()
        secret_word = 'GASSY'
        guesses = play_wordle(five_letter_words, secret_word, NaiveSolver())
        guess = guesses[-1]
        self.assertEqual(secret_word, guess)
        iterations = len(guesses)
        print(f'Found the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

