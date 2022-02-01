import unittest

from wordle_solver import *


class WordleTestCase(unittest.TestCase):

    def test_solver(self):
        five_letter_words = read_dictionary()
        for _ in range(0, 1000):
            secret_word = random_word(five_letter_words)
            print("secret word: " + secret_word)
            guess, iterations = solve(secret_word, five_letter_words)
            print(f'Found the solution {guess} in {iterations} iterations')
            self.assertEqual(secret_word, guess)


if __name__ == '__main__':
    unittest.main()
