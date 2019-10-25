import unittest
import statistics
import get_column_stats as col
import random

class TestCalc(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(col.mean([1, 2, 3, 4, 5]),
                         statistics.mean([1, 2, 3, 4, 5]))


    def test_std(self):
        self.assertEqual(col.stdev([1, 2, 3, 4, 5]),
                         statistics.stdev([1, 2, 3, 4, 5]))

    def self_setup(self):
            self.random_list = []

            for i in range(100):
                rand_int = random.randint(1, 100)
                self.random_list.append(rand_int)

            self.calc_mean_random_list = statistics.mean(self.random_list)
            self.calc_pstdev_random_list = statistics.pstdev(self.random_list)

     def test_mean_random(self):
        file_mean = col.mean(self.random_list)
        self.assertEqual(file_mean, self.calc_mean_random_list)

    def test_stdev_random(self):
        file_stdev = col.stdev(self.random_list)
        self.assertEqual(file_stdev, self.calc_pstdev_random_list)


if __name__ == '__main__':
    unittest.main()
