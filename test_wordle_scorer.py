import unittest

from wordle_scorer import Scorer


class ScorerTestCase(unittest.TestCase):

    def test_score(self):
        scorer = Scorer('AVAIL')
        score = scorer.score('ALTIN')
        self.assertEquals([('A', 1), ('L', 0), ('T', -1), ('I', 1), ('N', -1)], score)
