import unittest

from dictionary import *


class DictionaryTestCase(unittest.TestCase):

    def test_read_dictionary(self):
        dictionary = read_dictionary()
        self.assertEqual(2315, len(dictionary))

    def test_filter_dictionary(self):
        five_letter_words = read_dictionary()
        new_dict = filter_dictionary(five_letter_words, [('W', -1), ('O', -1), ('R', -1), ('D', -1), ('Y', -1)])
        self.assertEqual(644, len(new_dict))


    def test_set(self):
        words = ['ABATE', 'DISCO', 'FALSE', 'NEEDY', 'SKATE', 'WORDY']
        dictionary = SetDictionary(words)
        filtered_dictionary = dictionary.filter([('A', 0), ('N', -1), ('I', -1), ('M', -1), ('E', 1)])
        self.assertEqual(2, len(filtered_dictionary))
        self.assertEqual({'SKATE', 'FALSE'}, filtered_dictionary.words)


