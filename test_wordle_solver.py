import unittest

from wordle_solver import *


class WordleTestCase(unittest.TestCase):

    def test_dictionary(self):
        dictionary = read_dictionary()
        self.assertEqual(2315, len(dictionary))

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

    def test_filter_dictionary(self):
        five_letter_words = read_dictionary()
        new_dict = filter_dictionary(five_letter_words, [('W',-1), ('O',-1), ('R',-1), ('D',-1), ('Y',-1)])
        print(len(new_dict))

    def test_brute_force_solver(self):
        five_letter_words = read_dictionary()
        secret_word = 'TEPID'
        scorer = Scorer(secret_word)
        solver = BruteForceSolver(scorer)
        guesses = solver.solve(five_letter_words)
        guess = guesses[-1]
        self.assertEqual('TEPID', guess)
        iterations = len(guesses)
        print(f'\nFound the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

    def test_solver_accuracy(self):
        five_letter_words = read_dictionary()
        trials = 1000
        successes = 0
        total_score = 0
        for i in range(trials):
            secret_word = random_word(five_letter_words)
            scorer = Scorer(secret_word)
            # TODO: pass solver as param
            guesses = BruteForceSolver(scorer).solve(five_letter_words)

            guess = guesses[-1]
            if guess == secret_word:
                successes += 1
                total_score += len(guesses)

        success_rate = float(successes) / trials
        average_score = float(total_score) / successes
        print(f'\nSuccess rate = {success_rate:.2}')
        print(f'Average Score = {average_score}')

    def test_solver_repeated_letter(self):
        five_letter_words = read_dictionary()
        secret_word = 'GASSY'
        scorer = Scorer(secret_word)
        guesses = BruteForceSolver(scorer).solve(five_letter_words)
        guess = guesses[-1]
        self.assertEqual(secret_word, guess)
        iterations = len(guesses)
        print(f'Found the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)
