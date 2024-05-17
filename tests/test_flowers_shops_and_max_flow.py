import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.flowers_shops_and_max_flow import read_data_and_find_max_flow


class TestFlowersMaxFlow(unittest.TestCase):
    def test_farms_stores_graph(self):
        result = read_data_and_find_max_flow("roads.csv")
        self.assertEqual(result, 51)

    def test_empty_input(self):
        result = read_data_and_find_max_flow("roads_no_way.csv")
        self.assertEqual(result, 0)

    def test_wrong_input(self):
        result = read_data_and_find_max_flow("empty_roads.csv")
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
