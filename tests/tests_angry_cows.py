import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.angry_cows import largest_min_width_between_cows


class FindLargestMinWidht(unittest.TestCase):
    def test_largest_min_width_given_array(self):
        free_section = [0, 3, 4, 7, 10, 9]
        C = 4
        self.assertEqual(largest_min_width_between_cows(free_section, C), 3)

    def test_largest_min_width_sorted_array(self):
        free_section = [1, 2, 4, 8, 9]
        C = 3
        self.assertEqual(largest_min_width_between_cows(free_section, C), 3)

    def test_largest_min_width_single_section(self):
        free_section = [1]
        C = 1
        self.assertEqual(largest_min_width_between_cows(free_section, C), None)

    def test_largest_min_width_max_angry_cows(self):
        free_section = [1, 3, 6, 9]
        C = 100000
        self.assertEqual(largest_min_width_between_cows(free_section, C), 0)

    def test_largest_min_width_too_much_angry_cows(self):
        free_section = [1, 3, 6, 9]
        C = 100002
        self.assertEqual(largest_min_width_between_cows(free_section, C), None)


if __name__ == "__main__":
    unittest.main()
