import unittest

from wordle.wordle_scorer import *


class ScorerTestCase(unittest.TestCase):

    def test_score(self):
        scorer = Scorer('AVAIL')
        score = scorer.score('ALTIN')
        self.assertEquals([('A', 1), ('L', 0), ('T', -1), ('I', 1), ('N', -1)], score)

    def test_memory(self):
        scorer = MemoryScorer('../data/wordle_scores.pkl')
        score = scorer.score('AVAIL', 'ALIVE')
        print(score)
