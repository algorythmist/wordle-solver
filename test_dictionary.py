import unittest

from wordle_solver import read_dictionary
from dictionary import *


class DictionaryTestCase(unittest.TestCase):

    def test_set(self):
        words = ['ABATE', 'DISCO', 'FALSE', 'NEEDY', 'WORDY']
        dictionary = SetDictionary(words)
        print(dictionary.words)

    def test_map(self):
        words = ['ABATE', 'DISCO', 'FALSE', 'NEEDY', 'WORDY']
        dictionary = MapDictionary(words)
        #print(dictionary.words)

        final = dictionary.filter({'A': 0, 'B': 1, 'E': 0, 'D': -1, 'Y': -1})
        print(final.words)

