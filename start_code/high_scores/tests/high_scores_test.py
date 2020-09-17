import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_to_low

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [23, 2, 105, 88, 99, 41]
    
    def test_latest_score(self):
        self.assertEqual(41, latest(self.scores))
        
    def test_gets_personal_best(self):
        self.assertEqual(105, personal_best(self.scores))


    def test_top_three_from_scores(self):
        self.assertEqual([105, 99, 88], personal_top_three(self.scores))

    def test_ordered_highest_lowest(self):
        self.assertEqual([105, 99, 88, 41, 23, 2], high_to_low(self.scores))
 
    def test_top_three_when_tie(self):
        top_three = [12, 22, 45, 55, 55]
        self.assertEqual([55, 55, 45], personal_top_three(top_three))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
