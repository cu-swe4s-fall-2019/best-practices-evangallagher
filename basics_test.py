
import unittest
import statistics
import get_column_stats
import random

class TestCalc(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(get_column_stats.new_mean([1, 2, 3, 4, 5]),
                         statistics.mean([1, 2, 3, 4, 5]))


    def test_std(self):
        self.assertEqual(get_column_stats.new_std([1, 2, 3, 4, 5]),
                         statistics.new_std([1, 2, 3, 4, 5]))
