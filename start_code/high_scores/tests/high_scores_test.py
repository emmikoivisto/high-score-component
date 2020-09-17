import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [23, 2, 105, 88, 99, 41]
    
    def test_latest_score(self):
        self.assertEqual(41, latest(self.scores))
        
    def test_gets_personal_best(self):
        self.assertEqual(105, personal_best(self.scores))





    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
