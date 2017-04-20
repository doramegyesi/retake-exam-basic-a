import unittest
from min_max_diff import *

class TestMinMaxDiff(unittest.TestCase):
    def test_min_max_diff(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(min_max_diff(numbers), 4)

    def test_min_max_diff_empty_list(self):
        numbers = []
        self.assertEqual(min_max_diff(numbers), None)

    def test_min_max_diff_zero(self):
        numbers = [0]
        self.assertEqual(min_max_diff(numbers), 0)

if __name__ == '__main__':
    unittest.main()
