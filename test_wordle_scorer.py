import unittest
from wordle_scorer import Scorer

class ScorerTestCase(unittest.TestCase):

    def test_score(self):
        scorer = Scorer('AVAIL')
        score = scorer.score('ALTIN')
        print(score) #TODO assert



