import unittest

from wordle_solver import *


class WordleTestCase(unittest.TestCase):

    def test_dictionary(self):
        dictionary = read_dictionary()
        self.assertEqual(15918, len(dictionary))

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
        self.assertEqual(1510, len(guesses))
        for guess in guesses:
            self.assertTrue(all_letters_are_distinct(guess))

    def test_solver(self):
        five_letter_words = read_dictionary()
        secret_word = 'TEPID'
        guesses = solve(secret_word, five_letter_words)
        guess = guesses[-1]
        self.assertEqual('TEPID', guess)
        iterations = len(guesses)
        print(f'Found the solution {guess} in {iterations} iterations')
        self.assertEqual(secret_word, guess)

    # def test_solver_repeated_letter(self):
    #     five_letter_words = read_dictionary()
    #     secret_word = 'BULLS'
    #     guesses = solve(secret_word, five_letter_words)
    #     guess = guesses[-1]
    #     self.assertEqual('BULLS', guess)
    #     iterations = len(guesses)
    #     print(f'Found the solution {guess} in {iterations} iterations')
    #     self.assertEqual(secret_word, guess)


if __name__ == '__main__':
    unittest.main()
