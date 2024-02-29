import unittest
from find_kth_largest import find_kth_largest_el


class TestFindKthLargestEl(unittest.TestCase):

    def test_example_input_1(self):
        array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        true_value = 22
        true_index = 2
        result = find_kth_largest_el(array, k)
        self.assertEqual(result[0], true_value)
        self.assertEqual(result[1], true_index)

    def test_example_input_2(self):
        array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 1
        true_value = 42
        true_index = 6
        result = find_kth_largest_el(array, k)
        self.assertEqual(result[0], true_value)
        self.assertEqual(result[1], true_index)

    def test_with_k_out_of_range(self):
        array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = len(array) + 1
        result = find_kth_largest_el(array, k)
        self.assertIsNone(result)

    def test_empty_array(self):
        array = []
        k = 1
        result = find_kth_largest_el(array, k)
        self.assertIsNone(result)

    def test_random_array(self):
        import random

        array = random.sample(range(1, 1000), 100)
        k = 50
        true_value = sorted(array)[-k]
        result = find_kth_largest_el(array, k)
        self.assertEqual(result[0], true_value)


if __name__ == "__main__":
    unittest.main()
